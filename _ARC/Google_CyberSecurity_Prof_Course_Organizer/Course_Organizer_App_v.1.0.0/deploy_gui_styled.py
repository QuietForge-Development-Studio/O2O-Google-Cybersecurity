import os
import json
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Color and font styling
PRIMARY_COLOR = '#8E44AD'
BG_COLOR = '#1E1E2F'
TEXT_COLOR = '#F2F2F2'
BUTTON_COLOR = '#9B59B6'
HOVER_COLOR = '#B57EDC'
FONT = ('Segoe UI', 11)

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
    try:
        with open("google_cybersecurity_course_structure.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", "google_cybersecurity_course_structure.json not found.")
        return None

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
    if not course_data:
        return

    root = tk.Tk()
    root.title("Quiet Forge | Cyberstructure Builder")
    root.configure(bg=BG_COLOR)
    root.geometry("460x300")
    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TLabel", background=BG_COLOR, foreground=TEXT_COLOR, font=FONT)
    style.configure("TButton", font=FONT, padding=6)
    style.map("TButton", background=[('active', HOVER_COLOR), ('!active', BUTTON_COLOR)])
    style.configure("TCombobox", fieldbackground=BG_COLOR, background=BG_COLOR, foreground=TEXT_COLOR)

    # Load logo
    try:
        logo_img = Image.open("logo.png")
        logo_img = logo_img.resize((64, 64), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = ttk.Label(root, image=logo)
        logo_label.image = logo
        logo_label.pack(pady=(10, 0))
    except Exception:
        ttk.Label(root, text="🧠 Gary is loading caffeine...", anchor="center").pack(pady=(10, 0))

    ttk.Label(root, text="📚 Choose Deployment Option:").pack(pady=(15, 5))

    mode_var = tk.StringVar(value="Full Certificate")
    options = ["Full Certificate"] + [f"Module {i}" for i in range(1, 9)]
    dropdown = ttk.Combobox(root, textvariable=mode_var, values=options, state="readonly", width=35)
    dropdown.pack(pady=5)

    ttk.Button(root, text="🚀 Generate Structure", command=lambda: deploy_all(course_data) if mode_var.get() == "Full Certificate" else deploy_module(course_data, int(mode_var.get().split()[1]))).pack(pady=10)
    ttk.Button(root, text="❌ Exit", command=root.destroy).pack()

    root.mainloop()

if __name__ == "__main__":
    run_gui()
