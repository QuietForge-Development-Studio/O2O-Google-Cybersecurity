from pathlib import Path
from modules.file_generator import create_course_folders

# Fix path to course_structure.json
create_course_folders(
    course_number=1,
    base_path=Path.cwd() / "Student_Folders",
    structure_path=Path(__file__).parent / "data" / "course_structure.json"   # ✅ CORRECT path now
)
