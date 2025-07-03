import os

# === Config ===
BASE_DIR = "Course_Notes"
COURSES = {
    "Course_1_Foundations_of_Cybersecurity": {
        "M01_What_is_Cybersecurity": {
            "files": {
                "Overview.txt": "What is cybersecurity and why does it matter?",
                "Coach_Conversation.txt": "What examples helped you visualize security concepts?"
            },
            "folders": ["Screenshots", "Coach_Conversations", "Handouts"]
        },
        "M02_Why_Cybersecurity_Matters": {
            "files": {
                "Overview.txt": "What are real-world consequences of weak cybersecurity?",
                "Key_Terms.md": "- Threat: \n- Attack Vector: "
            },
            "folders": ["Screenshots", "Coach_Conversations", "Handouts"]
        },
        "M03_Exploring_Job_Roles": {
            "files": {
                "Overview.txt": "What cybersecurity job roles stood out to you?",
                "Downloads_Notes.txt": "Summarize job aid downloads or career map PDFs."
            },
            "folders": ["Screenshots", "Coach_Conversations", "Handouts"]
        },
        "M04_Day_in_the_Life": {
            "files": {
                "Overview.txt": "Reflect on the interviews. What surprised you?",
                "Coach_Conversation.txt": "What practical advice did you find useful?"
            },
            "folders": ["Screenshots", "Coach_Conversations", "Handouts"]
        }
    },
    "Course_2_Play_It_Safe": {
        "M01_What_is_Risk": {
            "files": {
                "Overview.txt": "Define risk in cybersecurity terms. How is it calculated?",
                "Key_Terms.md": "- Risk = Threat x Vulnerability x Impact"
            },
            "folders": ["Screenshots", "Coach_Conversations", "Handouts"]
        },
        "M02_Risk_Assessment_Frameworks": {
            "files": {
                "Overview.txt": "What frameworks were introduced (NIST, ISO)?",
                "Downloads_Notes.txt": "Summarize guidance or visual worksheets from the module."
            },
            "folders": ["Screenshots", "Downloads", "Coach_Conversations", "Handouts"]
        },
        "M03_Security_Controls": {
            "files": {
                "Overview.txt": "What are examples of Preventative / Detective / Corrective controls?",
                "Coach_Conversation.txt": "Which type of control felt most useful to you, and why?"
            },
            "folders": ["Screenshots", "Downloads", "Coach_Conversations", "Handouts"]
        },
        "M04_Risk_in_Practice": {
            "files": {
                "Overview.txt": "What steps were taken in the simulated risk assessment?",
                "Downloads_Notes.txt": "Write down checklist-style steps or acronyms provided."
            },
            "folders": ["Screenshots", "Downloads", "Coach_Conversations", "Handouts"]
        }
    }
}


# === Generator ===
def create_structure(base_dir, course_dict):
    for course, modules in course_dict.items():
        for module, contents in modules.items():
            mod_path = os.path.join(base_dir, course, module)
            os.makedirs(mod_path, exist_ok=True)
            for subfolder in contents.get("folders", []):
                os.makedirs(os.path.join(mod_path, subfolder), exist_ok=True)
            for fname, prompt in contents.get("files", {}).items():
                fpath = os.path.join(mod_path, fname)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(prompt + "\n")


# === Run ===
if __name__ == "__main__":
    create_structure(BASE_DIR, COURSES)
    print(f"✅ Notes folder structure created under: {BASE_DIR}")
