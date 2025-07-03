2import os

def create_module_only_if_course_exists(course_num, module_num, base_path='.'):
    course_folder = os.path.join(base_path, f"Course_{course_num}")
    module_folder = os.path.join(course_folder, f"Module_{module_num}")

    if not os.path.exists(course_folder):
        print(f"❌ Course_{course_num} folder does not exist at {base_path}.")
        return

    # File names
    notes_file = os.path.join(module_folder, f"Notes_C{course_num}_M{module_num}.txt")
    assignments_file = os.path.join(module_folder, f"Assignments_C{course_num}_M{module_num}.txt")
    portfolio_folder = os.path.join(module_folder, "Portfolio")
    scripts_folder = os.path.join(module_folder, "Scripts")

    # Create folders
    os.makedirs(portfolio_folder, exist_ok=True)
    os.makedirs(scripts_folder, exist_ok=True)

    # Create text files
    with open(notes_file, 'w') as f:
        f.write(f"# Notes for Course {course_num}, Module {module_num}\n\n")

    with open(assignments_file, 'w') as f:
        f.write(f"# Assignments for Course {course_num}, Module {module_num}\n\n")

    print(f"✅ Module_{module_num} created in Course_{course_num}")

if __name__ == "__main__":
    try:
        course = int(input("Enter Course Number (1–8): "))
        module = int(input("Enter Module Number (1–20): "))
        base = os.getcwd()
        create_module_only_if_course_exists(course, module, base_path=base)
    except ValueError:
        print("❌ Please enter valid numeric values.")
