
import os
import json

def sanitize(name):
    return name.strip().replace(" ", "_").replace("/", "-")

def create_topic_structure(course_num, course_title, module_num, topic_num, topic_name, base_path='.'):
    numeric_id = f"{course_num}.{module_num}.{topic_num}"
    topic_safe = sanitize(topic_name)
    folder_name = f"{numeric_id}_{topic_safe}"

    course_folder = os.path.join(base_path, f"Course_{course_num}_{sanitize(course_title)}")
    module_folder = os.path.join(course_folder, f"Module_{module_num}")
    topic_folder = os.path.join(module_folder, folder_name)
    os.makedirs(topic_folder, exist_ok=True)

    file_prefix = f"{numeric_id}"
    base_files = [
        f"coach_{file_prefix}.txt",
        f"notes_{file_prefix}.txt",
        f"research_{file_prefix}.txt",
        f"review_{file_prefix}.txt",
        f"transcripts_{file_prefix}.txt",
        f"README_{file_prefix}.md"
    ]
    for filename in base_files:
        open(os.path.join(topic_folder, filename), 'w').close()

    for subfolder in ["Labs", "Readings", "Assignments", "Scripts"]:
        sub_path = os.path.join(topic_folder, subfolder)
        os.makedirs(sub_path, exist_ok=True)
        placeholder = os.path.join(sub_path, f"{subfolder.lower()}_{file_prefix}.txt")
        open(placeholder, 'w').close()

def load_course_structure(json_file):
    with open(json_file, "r") as f:
        return json.load(f)

def deploy_module(course_data, course_num, output_dir="."):
    key = f"Course_{course_num}"
    if key not in course_data:
        print(f"❌ Course {course_num} not found.")
        return
    course_info = course_data[key]
    for t_index, topic in enumerate(course_info["Topics"], start=1):
        create_topic_structure(course_num, course_info["Title"], 1, t_index, topic, base_path=output_dir)

def deploy_all(course_data, output_dir="."):
    for c_index, (course_key, course_info) in enumerate(course_data.items(), start=1):
        for t_index, topic in enumerate(course_info["Topics"], start=1):
            create_topic_structure(c_index, course_info["Title"], 1, t_index, topic, base_path=output_dir)

if __name__ == "__main__":
    course_file = "google_cybersecurity_course_structure.json"
    if not os.path.exists(course_file):
        print(f"❌ Required JSON file '{course_file}' not found.")
        exit(1)

    course_data = load_course_structure(course_file)

    print("\n📚 Quiet Forge | Google Cybersecurity Structure Builder")
    print("-------------------------------------------------------")
    print("1. Full Certificate Deployment")
    print("2. Single Module Deployment (1–9)")
    choice = input("Choose an option [1/2]: ").strip()

    if choice == "1":
        deploy_all(course_data)
        print("\n✅ Full certificate structure deployed successfully.")
    elif choice == "2":
        try:
            module = int(input("Enter module number (1–9): "))
            if 1 <= module <= 9:
                deploy_module(course_data, module)
                print(f"\n✅ Module {module} structure deployed successfully.")
            else:
                print("❌ Invalid module number.")
        except ValueError:
            print("❌ Please enter a valid number.")
    else:
        print("❌ Invalid choice. Exiting.")
