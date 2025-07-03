// Filename: SessionAPIUtils.js
// Version: v1.0.1
// Purpose: Moderately robust API client for Coursera on-demand sessions with enhanced commenting (1:1.5 ratio)

// --- External Dependencies ------------------------------------------------
import axios from 'axios';                     // HTTP client for requests
import axiosRetry from 'axios-retry';          // Adds retry capabilities to axios
import URI from 'jsuri';                       // Simplifies URL building

// --- Configuration --------------------------------------------------------
// Base URL for all API requests; defaults to Coursera's public domain
const API_BASE = process.env.COURSE_API_BASE || 'https://www.coursera.org';
// Authorization token (e.g., JWT or OAuth2 Bearer token) for secured endpoints
const AUTH_TOKEN = process.env.COURSE_API_TOKEN;

// --- Axios Client Setup ---------------------------------------------------
// Create a shared axios instance to apply timeouts, headers, and retries globally
const apiClient = axios.create({
  baseURL: `${API_BASE}/api`,                // Prefix all calls with /api
  timeout: 10000,                            // 10-second timeout for each request
  headers: {
    'Content-Type': 'application/json',      // JSON payloads by default
    ...(AUTH_TOKEN && { Authorization: `Bearer ${AUTH_TOKEN}` }),
  },
});

// Configure retry logic: up to 3 attempts with exponential backoff
axiosRetry(apiClient, {
  retries: 3,                                   // Maximum retry attempts
  retryDelay: axiosRetry.exponentialDelay,      // Exponential back-off between retries
  retryCondition: (error) => {
    // Retry on network errors (e.g., DNS issues) or 5xx server responses
    return axiosRetry.isNetworkError(error) || axiosRetry.isRetryableError(error);
  },
});

// --- Request Helper -------------------------------------------------------
/**
 * Generic HTTP request wrapper that logs errors and returns response data.
 * @param {string} method - HTTP method (get, post, put, delete)
 * @param {string} url - Endpoint path, relative to baseURL
 * @param {object} [data] - Request payload for POST/PUT
 * @param {object} [params] - Query parameters for GET requests
 * @returns {Promise<any>} - Resolves with response data
 */
async function request(method, url, data = null, params = {}) {
  try {
    // Execute the HTTP request using axios
    const response = await apiClient.request({ method, url, data, params });
    return response.data;
  } catch (err) {
    // Log error context for easier debugging
    console.error(`[SessionAPI] ${method.toUpperCase()} ${url} failed:`, err.message);
    // Re-throw to allow upstream handling
    throw err;
  }
}

// --- URL Builder ----------------------------------------------------------
/**
 * Constructs a URL path with query parameters using jsuri
 * @param {string} path - Base API path (e.g., '/onDemandSessions.v1')
 * @param {object} query - Key/value pairs for query string
 * @returns {string} - URL string, ready for axios
 */
function buildUrl(path, query = {}) {
  const uri = new URI(`${API_BASE}/api${path}`);
  // Append each query parameter
  Object.entries(query).forEach(([key, value]) => {
    uri.addQueryParam(key, value);
  });
  // Remove the full origin to get the relative path for axios
  return uri.toString().replace(`${API_BASE}/api`, '');
}

// --- Session API Functions ------------------------------------------------
const SessionAPI = {
  /**
   * Create a new on-demand session for a course.
   * @param {string} courseId - Unique course identifier
   * @param {number} startedAt - Start timestamp in ms
   * @param {number} enrollmentEndedAt - Enrollment close timestamp in ms
   * @param {number} [endedAt] - Optional end timestamp in ms
   * @param {boolean} [isPrivate=false] - Whether session is private
   * @returns {Promise<any>} API response payload
   */
  createSession: async (courseId, startedAt, enrollmentEndedAt, endedAt = null, isPrivate = false) => {
    const payload = { courseId, startedAt, enrollmentEndedAt, isPrivate };
    if (endedAt) payload.endedAt = endedAt;    // Include end time if provided
    return request('post', '/onDemandSessions.v1', payload);
  },

  /**
   * Delete an existing on-demand session by ID.
   * @param {string} sessionId - Session identifier
   * @returns {Promise<any>} API response payload
   */
  deleteSession: async (sessionId) => {
    return request('delete', `/onDemandSessions.v1/${sessionId}`);
  },

  /**
   * Update session details. Superusers use PUT, others POST with override action.
   * @param {string} sessionId
   * @param {object} sessionData - Fields to update
   * @param {boolean} [isSuperuser=false]
   */
  updateSession: async (sessionId, sessionData, isSuperuser = false) => {
    if (isSuperuser) {
      // PUT with allowTimeChanges query for superusers
      const url = buildUrl(`/onDemandSessions.v1/${sessionId}`, { allowTimeChanges: true });
      return request('put', url, sessionData);
    }
    // Non-superusers override item availability and deadlines
    const url = buildUrl('/onDemandSessions.v1', {
      action: 'overrideItemAvailabilityAndDeadline', id: sessionId,
    });
    return request('post', url, { sessionId, ...sessionData });
  },

  /**
   * List all sessions for a course.
   * @param {string} courseId
   * @param {boolean} [includeExternallyManaged=false]
   */
  listSessions: async (courseId, includeExternallyManaged = false) => {
    const url = buildUrl('/onDemandSessions.v1', {
      q: 'allByCourse', courseId, includeExternallyManaged,
    });
    return request('get', url);
  },

  /**
   * Retrieve details for a specific session.
   * @param {string} sessionId
   */
  getSession: async (sessionId) => {
    const url = buildUrl(`/onDemandSessions.v1/${sessionId}`, {
      fields: 'moduleDeadlines,isPrivate,itemDeadlines,scheduleOverride,branchId',
    });
    return request('get', url);
  },

  /**
   * Fetch a module's metadata and linked items.
   * @param {string} courseId
   * @param {string} moduleId
   * @returns {Promise<Object>} Module details with linked item list
   */
  getModule: async (courseId, moduleId) => {
    const path = '/onDemandCourseMaterials.v2';
    const url = buildUrl(path, {
      q: 'module', courseId, moduleId, includes: 'modules',
    });
    const data = await request('get', url);
    // Extract the first linked module object
    return data.linked['onDemandCourseMaterialModules.v1'][0];
  },
};

// Named exports for easy imports elsewhere
export default SessionAPI;
export const { createSession, deleteSession, updateSession, listSessions, getSession, getModule } = SessionAPI;
