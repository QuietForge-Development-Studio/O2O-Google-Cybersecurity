import os

def sanitize_topic_name(topic_name):
    """Sanitize topic name to be filesystem-safe."""
    return topic_name.strip().replace(" ", "_").replace("/", "-")

def create_topic_structure(course_num, module_num, topic_name, base_path='.'):
    topic_safe = sanitize_topic_name(topic_name)

    # Build full directory path
    course_folder = os.path.join(base_path, f"Course_{course_num}")
    module_folder = os.path.join(course_folder, f"Module_{module_num}")
    topic_folder = os.path.join(module_folder, topic_safe)

    os.makedirs(topic_folder, exist_ok=True)

    # Create pre-named blank text files in topic folder
    file_prefix = f"c{course_num}_m{module_num}_t{topic_safe}"
    files_to_create = [
        f"coach_{file_prefix}.txt",
        f"notes_{file_prefix}.txt",
        f"research_{file_prefix}.txt",
        f"review_{file_prefix}.txt",
        f"transcripts_{file_prefix}.txt"
    ]

    for filename in files_to_create:
        with open(os.path.join(topic_folder, filename), 'w') as f:
            pass

    # Create Assignments and Scripts folders under the topic folder
    assignments_folder = os.path.join(topic_folder, "Assignments")
    scripts_folder = os.path.join(topic_folder, "Scripts")
    os.makedirs(assignments_folder, exist_ok=True)
    os.makedirs(scripts_folder, exist_ok=True)

    # Add placeholder files in subfolders
    with open(os.path.join(assignments_folder, f"assignment_{file_prefix}.txt"), 'w') as f:
        pass
    with open(os.path.join(scripts_folder, f"script_{file_prefix}.txt"), 'w') as f:
        pass

    print(f"✅ Course_{course_num}/Module_{module_num}/{topic_safe} initialized.")

if __name__ == "__main__":
    try:
        course = int(input("Enter Course Number (1–9): "))
        module = int(input("Enter Module Number (1–20): "))
        topic = input("Enter Topic Name: ").strip()
        base = os.getcwd()
        create_topic_structure(course, module, topic, base_path=base)
    except ValueError:
        print("❌ Please enter valid numeric values.")
