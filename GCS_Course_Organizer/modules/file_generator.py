import json
from pathlib import Path

def load_course_structure(json_path: Path) -> dict:
    """Load course definitions from a JSON file."""
    with open(json_path, "r") as f:
        data = json.load(f)
    return data.get("courses", {})

def create_course_folders(course_number: int, base_path: Path, structure_path: Path):
    """Create folders and files for a specific course."""
    courses = load_course_structure(structure_path)

    if str(course_number) not in courses:
        raise ValueError(f"Course {course_number} not found in JSON structure.")

    course = courses[str(course_number)]
    course_folder = base_path / f"Course_{course_number}_{course['name'].replace(' ', '_')}"
    course_folder.mkdir(parents=True, exist_ok=True)

    # Notes file
    notes_file = course_folder / f"Course_{course_number}_Notes.txt"
    notes_file.touch(exist_ok=True)

    # Portfolio
    if portfolio_name := course.get("portfolio"):
        portfolio_path = course_folder / "Portfolio"
        portfolio_path.mkdir(exist_ok=True)
        (portfolio_path / portfolio_name).touch(exist_ok=True)

    # Labs
    if course.get("labs"):
        labs_path = course_folder / "Labs"
        labs_path.mkdir(exist_ok=True)

    print(f"✅ Created folder for Course {course_number}: {course['name']}")
