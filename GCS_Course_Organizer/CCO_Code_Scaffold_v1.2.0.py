# File: CCO_Code_Scaffold_v1.2.0.py

```python
# 1. Imports and Setup
import os
from pathlib import Path

# 2. Configuration: adjust as needed
# Base directory where course content lives
BASE_PATH = Path.home() / "Desktop" / "Vault_Master" / "Sandbox" / "O2O Google Cybersecurity" / "Course_Notes"

# Define modules structure: list of modules with sections and topics
COURSE_STRUCTURE = {
    "2.3": {
        "module_title": "Play It Safe",
        "sections": {
            "1": {
                "title": "IntroductionToCybersecurityTools",
                "components": [
                    ("transcript", "WelcomeToModule3"),
                    ("notes", "LogsAndSIEMTools"),
                    ("transcript", "SIEMDashboards"),
                    ("notes", "TheFutureOfSIEMTools"),
                    ("transcript", "ParisaAccessibilityAndSecurity"),
                    ("tests", "SIEMDashboardsChallenge")
                ]
            },
            # Add further sections here...
        }
    },
    # Add additional modules here...
}

# Template for markdown file
MD_TEMPLATE = """# {module}.{section}.{item:02d} {ComponentType}: {Title}

*Content goes here…*
"""

# 3. Core Functions

def create_course_structure(structure: dict, base_path: Path):
    """
    Walks the COURSE_STRUCTURE and creates folders + files
    following naming and formatting conventions.
    """
    for module_key, module in structure.items():
        module_path = base_path / f"Course_{module_key.replace('.', '_')}_{module['module_title'].replace(' ', '')}"
        module_path.mkdir(parents=True, exist_ok=True)

        for section_key, section in module["sections"].items():
            section_path = module_path / f"{module_key}.{section_key}-{section['title']}"
            section_path.mkdir(exist_ok=True)

            for idx, (comp_key, topic) in enumerate(section["components"], start=1):
                filename = f"{module_key}_{comp_key}_{topic}.md"
                filepath = section_path / filename

                if not filepath.exists():
                    # Determine the ComponentType from comp_key
                    comp_type_map = {
                        "notes": "Reading",
                        "transcript": "Video",
                        "tests": "Practice Assignment",
                        "coach": "Coach Tips"
                    }
                    component_type = comp_type_map.get(comp_key, comp_key.title())

                    # Assemble heading
                    heading = MD_TEMPLATE.format(
                        module=module_key,
                        section=section_key,
                        item=idx,
                        ComponentType=component_type,
                        Title=" ".join([word.capitalize() for word in topic.split()])
                    )
                    filepath.write_text(heading, encoding="utf-8")
                    print(f"Created: {filepath}")

# 4. Script Entry Point

if __name__ == "__main__":
    create_course_structure(COURSE_STRUCTURE, BASE_PATH)
