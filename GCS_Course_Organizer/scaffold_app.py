import os
from pathlib import Path

# App name
APP_NAME = "Cybersecurity_Course_Organizer"

# Folder and file structure
structure = {
    "": ["main.py", "requirements.txt", "README.md"],
    "modules": ["gui.py", "file_generator.py", "portfolio_merger.py"],
    "data": ["course_structure.json"],
    "tests": ["test_placeholder.py"],
}

# Optional file contents
starter_files = {
    "main.py": '''# Entry point for the Cybersecurity Course Organizer

from modules.gui import run_gui

if __name__ == "__main__":
    run_gui()
''',
    "modules/gui.py": '''# GUI logic (Tkinter or Flask)

def run_gui():
    print("GUI not implemented yet.")
''',
    "modules/file_generator.py": '''# Logic for generating course folder structure

def create_course_folders(course_number, base_path):
    pass
''',
    "modules/portfolio_merger.py": '''# Logic for consolidating portfolio files

def consolidate_portfolio(source_dir, target_dir):
    pass
''',
    "data/course_structure.json": '''{
  "courses": {}
}
''',
    "tests/test_placeholder.py": '''# Placeholder test module

def test_dummy():
    assert True
''',
    "README.md": '''# Cybersecurity Course Organizer

Modular Python tool to scaffold and consolidate folders for the Google Cybersecurity Professional Certificate.
''',
    "requirements.txt": '''flask
'''
}

def create_structure(base_path):
    base = Path(base_path) / APP_NAME
    for folder, files in structure.items():
        folder_path = base / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        for file in files:
            file_path = folder_path / file
            if not file_path.exists():
                content = starter_files.get(f"{folder}/{file}".lstrip("/"), "")
                file_path.write_text(content)
    print(f"✅ Created app structure at: {base}")

# Run this script directly
if __name__ == "__main__":
    create_structure(Path.cwd())
