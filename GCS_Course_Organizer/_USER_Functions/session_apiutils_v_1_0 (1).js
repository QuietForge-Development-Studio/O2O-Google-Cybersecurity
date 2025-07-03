// Filename: SessionAPIUtils.js
// Version: v1.1.0
// Purpose: Robust API client for Coursera on-demand sessions with full endpoint coverage and enhanced comments

// --- External Dependencies ------------------------------------------------
import axios from 'axios';                     // Promise-based HTTP client
import axiosRetry from 'axios-retry';          // Retry logic for axios
import URI from 'jsuri';                       // URL builder with query param support
import dotenv from 'dotenv';                   // Loads .env file into process.env

dotenv.config();  // Load environment variables from .env

// --- Configuration --------------------------------------------------------
// Base URL for API calls; override with COURSE_API_BASE in .env if needed
const API_BASE = process.env.COURSE_API_BASE || 'https://www.coursera.org';
// Auth token (JWT/OAuth2) for secured endpoints; required for non-public calls
const AUTH_TOKEN = process.env.COURSE_API_TOKEN;

// Validate critical env vars early
if (!AUTH_TOKEN) {
  console.warn('⚠️  Warning: COURSE_API_TOKEN is not set. Authenticated endpoints may fail.');
}

// --- Axios Client Setup ---------------------------------------------------
const apiClient = axios.create({
  baseURL: `${API_BASE}/api`,                // All calls under /api
  timeout: 10000,                            // 10 seconds per request
  headers: {
    'Content-Type': 'application/json',      // JSON by default
    ...(AUTH_TOKEN && { Authorization: `Bearer ${AUTH_TOKEN}` }),
  },
});

// Retry on network issues or 5xx responses, up to 3 attempts
axiosRetry(apiClient, {
  retries: 3,
  retryDelay: axiosRetry.exponentialDelay,
  retryCondition: (error) => axiosRetry.isNetworkError(error) || axiosRetry.isRetryableError(error),
});

// --- Request Helper -------------------------------------------------------
/**
 * Wraps axios requests with consistent error logging
 * @param {string} method - HTTP verb
 * @param {string} url - Relative endpoint path
 * @param {object} [data] - Request body
 * @param {object} [params] - Query parameters
 * @returns {Promise<any>} - Response data
 */
async function request(method, url, data = null, params = {}) {
  try {
    const response = await apiClient.request({ method, url, data, params });
    return response.data;
  } catch (error) {
    console.error(`[SessionAPI] ${method.toUpperCase()} ${url} failed:`, error.response?.status, error.message);
    throw error;
  }
}

// --- URL Builder ----------------------------------------------------------
/**
 * Builds an endpoint path with query parameters
 * @param {string} path - e.g. '/onDemandSessions.v1'
 * @param {object} [query] - Key/value map
 * @returns {string} - URL string for axios
 */
function buildUrl(path, query = {}) {
  const uri = new URI(`${API_BASE}/api${path}`);
  Object.entries(query).forEach(([key, value]) => uri.addQueryParam(key, value));
  return uri.toString().replace(`${API_BASE}/api`, '');
}

// --- Session API Methods --------------------------------------------------
const SessionAPI = {
  /** Create a new session */
  createSession: (courseId, startedAt, enrollmentEndedAt, endedAt = null, isPrivate = false) => {
    const payload = { courseId, startedAt, enrollmentEndedAt, isPrivate };
    if (endedAt) payload.endedAt = endedAt;
    return request('post', '/onDemandSessions.v1', payload);
  },

  /** Delete session by ID */
  deleteSession: (sessionId) => request('delete', `/onDemandSessions.v1/${sessionId}`),

  /** Update session */
  updateSession: (sessionId, sessionData, isSuperuser = false) => {
    if (isSuperuser) {
      const url = buildUrl(`/onDemandSessions.v1/${sessionId}`, { allowTimeChanges: true });
      return request('put', url, sessionData);
    }
    const url = buildUrl('/onDemandSessions.v1', { action: 'overrideItemAvailabilityAndDeadline', id: sessionId });
    return request('post', url, { sessionId, ...sessionData });
  },

  /** List sessions for a course */
  listSessions: (courseId, includeExternallyManaged = false) => {
    const url = buildUrl('/onDemandSessions.v1', { q: 'allByCourse', courseId, includeExternallyManaged });
    return request('get', url);
  },

  /** Get a single session */
  getSession: (sessionId) => {
    const url = buildUrl(`/onDemandSessions.v1/${sessionId}`, { fields: 'moduleDeadlines,isPrivate,itemDeadlines,scheduleOverride,branchId' });
    return request('get', url);
  },

  /** Get current open session */
  currentOpenSession: (courseId) => {
    const url = buildUrl('/onDemandSessions.v1', { q: 'currentOpenByCourse', courseId });
    return request('get', url);
  },

  /** Create scheduled sessions */
  createScheduledSessions: (courseId, sessionsCountOverride = 1) => {
    return request('post', '/onDemandSessionAutoCreations.v1', { courseId, sessionsCountOverride });
  },

  /** Clear all sessions */
  clearAllSessions: (courseId) => {
    const url = buildUrl('/api/authoringSessionSetup.v1', { action: 'clearPublicSessions', courseId });
    return request('post', url);
  },

  /** Setup sessions with first start date */
  setupSessions: (courseId, firstSessionStartsOn) => request('post', '/authoringSessionSetup.v1', { courseId, firstSessionStartsOn }),

  /** Fetch module with linked items */
  getModule: async (courseId, moduleId) => {
    const url = buildUrl('/onDemandCourseMaterials.v2', { q: 'module', courseId, moduleId, includes: 'modules' });
    const data = await request('get', url);
    return data.linked['onDemandCourseMaterialModules.v1'][0];
  },

  /** Update learner schedule */
  updateLearnerItemSchedule: ({ sessionId, userId, sessionOverrides }) => {
    const url = buildUrl(`/sessionMembershipPersonalizedSchedules.v1/${userId}~${sessionId}`, { fields: 'timedItemLocks,itemDeadlines' });
    return request('patch', url, sessionOverrides);
  },

  /** Get learner schedule */
  getLearnerItemSchedule: ({ sessionId, userId }) => {
    const url = buildUrl(`/sessionMembershipPersonalizedSchedules.v1/${userId}~${sessionId}`, { fields: 'timedItemLocks,itemDeadlines' });
    return request('get', url);
  },
};

// Export
export default SessionAPI;
export const { createSession, deleteSession, updateSession, listSessions, getSession, currentOpenSession, createScheduledSessions, clearAllSessions, setupSessions, getModule, updateLearnerItemSchedule, getLearnerItemSchedule } = SessionAPI;
