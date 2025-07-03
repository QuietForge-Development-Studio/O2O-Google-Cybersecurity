import os

def create_module_structure(course_num, module_num, base_path='.'):
    course_folder = os.path.join(base_path, f"Course_{course_num}")
    module_folder = os.path.join(course_folder, f"Module_{module_num}")

    # Ensure course/module folders exist
    os.makedirs(module_folder, exist_ok=True)

    # Create pre-named blank text files
    files_to_create = [
        f"coach_c{course_num}_m{module_num}.txt",
        f"notes_c{course_num}_m{module_num}.txt",
        f"research_c{course_num}_m{module_num}.txt",
        f"review_c{course_num}_m{module_num}.txt",
        f"transcripts_c{course_num}_m{module_num}.txt",
    ]

    for filename in files_to_create:
        path = os.path.join(module_folder, filename)
        with open(path, 'w') as f:
            pass  # Empty file

    # Create Assignments and Scripts folders + placeholder text files
    assignments_folder = os.path.join(module_folder, "Assignments")
    scripts_folder = os.path.join(module_folder, "Scripts")

    os.makedirs(assignments_folder, exist_ok=True)
    os.makedirs(scripts_folder, exist_ok=True)

    # Add empty placeholder text files to those folders
    with open(os.path.join(assignments_folder, f"assignment_c{course_num}_m{module_num}.txt"), 'w') as f:
        pass

    with open(os.path.join(scripts_folder, f"script_c{course_num}_m{module_num}.txt"), 'w') as f:
        pass

    print(f"✅ Course_{course_num}/Module_{module_num} initialized with standard files and folders.")

if __name__ == "__main__":
    try:
        course = int(input("Enter Course Number (1–9): "))
        module = int(input("Enter Module Number (1–20): "))
        base = os.getcwd()
        create_module_structure(course, module, base_path=base)
    except ValueError:
        print("❌ Please enter valid numeric values.")
