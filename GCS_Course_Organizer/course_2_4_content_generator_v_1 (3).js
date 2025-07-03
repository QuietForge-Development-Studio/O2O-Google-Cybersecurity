// Filename: generate_2_4_content.js
// Version: v1.1.1

import fs from 'fs/promises';
import path from 'path';
// Ensure SessionAPIUtils.js is located in the same directory as this script
import { getModule } from './SessionAPIUtils.js';

// --- CONFIGURATION -------------------------------------------------------
const BASE_DIR = 
  'C:\\Users\\lasve\\Desktop\\Vault_Master\\Sandbox\\O2O_GCS_Cert\\Course_Notes\\2 - Course_2_Play_It_Safe';
const MODULE_FOLDER = '2.4-Risk_in_Practice';
const OUTPUT_DIR = path.join(BASE_DIR, MODULE_FOLDER);
const COURSE_ID = 'COURSE_2_ID';    // Replace with actual course ID
const MODULE_ID = 'MODULE_2_4_ID';   // Replace with actual module ID

// --- HELPERS -------------------------------------------------------------
function slugify(str) {
  return str
    .toLowerCase()
    .replace(/\s+/g, '_')       // spaces → underscores
    .replace(/[^a-z0-9_]/g, ''); // strip invalid chars
}

async function ensureDir(dir) {
  await fs.mkdir(dir, { recursive: true });
}

// Generate banded notes or transcripts
async function generateBandFile(items, filename) {
  const lines = [`# ${filename.replace('.md','')}`, ''];

  items.forEach((item, i) => {
    const topicIndex = `2.4.1.${i+1}`;
    lines.push(`// ========== ${topicIndex} – ${item.name.toUpperCase()} ==========:`, '');

    if (item.subtopics && item.subtopics.length) {
      item.subtopics.forEach((sub, j) => {
        const subIndex = `${topicIndex}.${j+1}`;
        lines.push(`// --- ${subIndex} – ${sub}`, '');
      });
    }
  });

  await fs.writeFile(path.join(OUTPUT_DIR, filename), lines.join('\n') + '\n');
}

// --- MAIN ----------------------------------------------------------------
async function generateContent() {
  await ensureDir(OUTPUT_DIR);
  await ensureDir(path.join(OUTPUT_DIR, 'Handouts'));
  await ensureDir(path.join(OUTPUT_DIR, 'Activities'));
  await ensureDir(path.join(OUTPUT_DIR, 'Assets'));

  let module;
  try {
    module = await getModule(COURSE_ID, MODULE_ID);
  } catch (err) {
    console.error('Error loading module:', err);
    return;
  }

  const items = (module.items || []).map((it) => {
    const linkedSubs = module.linked?.['onDemandCourseItemSubtitles.v1'] || [];
    const subList = linkedSubs
      .filter((sub) => sub.courseItemId === it.id)
      .map((sub) => sub.name);
    return { name: it.name, subtopics: subList };
  });

  await generateBandFile(items, '2.4.1_notes.md');
  await generateBandFile(items, '2.4.1_transcripts.md');

  await fs.writeFile(path.join(OUTPUT_DIR, 'Handouts', '2.4_glossary.md'), '// Consolidated glossary entries\n');
  await fs.writeFile(
    path.join(OUTPUT_DIR, 'Handouts', '2.4.1_practice_exercises.md'),
    '# Practice Exercises\n\n1. /* Add exercise here */\n'
  );

  await fs.writeFile(
    path.join(OUTPUT_DIR, 'Activities', '2.4.1_tests.md'),
    '# Test: \n\n1. /* Add test prompts here */\n'
  );
  await fs.writeFile(
    path.join(OUTPUT_DIR, 'Activities', '2.4.1_coach.md'),
    '# Coach Prompts: \n\n- /* Add coaching questions here */\n'
  );

  await fs.writeFile(path.join(OUTPUT_DIR, 'Assets', '2.4.1_diagram1.png'), '');
  await fs.writeFile(path.join(OUTPUT_DIR, 'Assets', '2.4_module_flowchart.png'), '');

  console.log('2.4-Risk_in_Practice scaffold complete');
}

generateContent().catch(console.error);
