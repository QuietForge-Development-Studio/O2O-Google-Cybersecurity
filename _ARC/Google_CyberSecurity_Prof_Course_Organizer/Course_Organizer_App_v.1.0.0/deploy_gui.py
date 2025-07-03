import os
import json
import tkinter as tk
from tkinter import ttk, messagebox


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

def load_course_structure():
    course_file = "google_cybersecurity_course_structure.json"
    if not os.path.exists(course_file):
        messagebox.showerror("Error", f"JSON file '{course_file}' not found.")
        return None
    with open(course_file, "r") as f:
        return json.load(f)

def deploy_module(course_data, course_num):
    key = f"Course_{course_num}"
    if key not in course_data:
        messagebox.showerror("Error", f"Course {course_num} not found.")
        return
    course_info = course_data[key]
    for t_index, topic in enumerate(course_info["Topics"], start=1):
        create_topic_structure(course_num, course_info["Title"], 1, t_index, topic)
    messagebox.showinfo("Success", f"Module {course_num} deployed successfully.")

def deploy_all(course_data):
    for c_index, (course_key, course_info) in enumerate(course_data.items(), start=1):
        for t_index, topic in enumerate(course_info["Topics"], start=1):
            create_topic_structure(c_index, course_info["Title"], 1, t_index, topic)
    messagebox.showinfo("Success", "Full certificate structure deployed successfully.")

def run_gui():
    course_data = load_course_structure()
    if course_data is None:
        return

    def deploy():
        selection = mode_var.get()
        if selection == "Full Certificate":
            deploy_all(course_data)
        else:
            try:
                module_num = int(selection.split()[1])
                deploy_module(course_data, module_num)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid module selected: {e}")

    root = tk.Tk()
    root.title("Quiet Forge | Cyberstructure Builder")
    root.geometry("400x200")

    ttk.Label(root, text="📚 Choose Deployment Option:", font=("Segoe UI", 11)).pack(pady=10)

    mode_var = tk.StringVar(value="Full Certificate")
    choices = ["Full Certificate"] + [f"Module {i}" for i in range(1, 9)]
    dropdown = ttk.Combobox(root, textvariable=mode_var, values=choices, state="readonly", width=30)
    dropdown.pack(pady=5)

    ttk.Button(root, text="Generate Structure", command=deploy).pack(pady=10)
    ttk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
