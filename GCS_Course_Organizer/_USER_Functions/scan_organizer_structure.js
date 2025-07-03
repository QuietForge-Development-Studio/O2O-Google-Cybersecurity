// Filename: scan_organizer_structure.js
// Version: v1.0.0
// Purpose: Identify empty/placeholder files and missing imports in the organizer app

import fs from 'fs';
import path from 'path';

// Configuration: path to your organizer app folder
const BASE_DIR = process.argv[2] || 
  'C:/Users/lasve/Desktop/Vault_Master/Sandbox/O2O_GCS_Cert/GCS_Course_Organizer';

const placeholderPatterns = [
  /TODO/i,
  /\/\*\s*Add /i,
  /placeholder/i
];

const importRegex = /import\s+[^'";]+['"](\.{1,2}\/[^'";]+)['"]/g;

let brokenImports = [];
let emptyFiles = [];
let placeholderFiles = [];

function walkDir(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (let entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walkDir(fullPath);
    } else {
      analyzeFile(fullPath);
    }
  }
}

function analyzeFile(filePath) {
  const stat = fs.statSync(filePath);
  if (stat.size === 0) {
    emptyFiles.push(filePath);
  }
  const ext = path.extname(filePath).toLowerCase();
  if (['.js', '.jsx', '.ts', '.tsx', '.md'].includes(ext)) {
    const content = fs.readFileSync(filePath, 'utf8');
    // Check placeholders
    if (placeholderPatterns.some((re) => re.test(content))) {
      placeholderFiles.push(filePath);
    }
    // Check imports
    if (ext === '.js' || ext === '.jsx' || ext === '.ts' || ext === '.tsx') {
      let match;
      while ((match = importRegex.exec(content))) {
        const importPath = match[1];
        const resolved = path.resolve(path.dirname(filePath), importPath);
        if (!fs.existsSync(resolved) && !fs.existsSync(resolved + '.js')) {
          brokenImports.push({ file: filePath, import: importPath });
        }
      }
    }
  }
}

// Run scanner
walkDir(BASE_DIR);

// Output results
console.log('\n=== Empty Files ===');
emptyFiles.forEach(f => console.log(f));

console.log('\n=== Placeholder Files ===');
placeholderFiles.forEach(f => console.log(f));

console.log('\n=== Broken Imports ===');
brokenImports.forEach(b => console.log(`${b.file} → ${b.import}`));

console.log('\nScan complete.');
