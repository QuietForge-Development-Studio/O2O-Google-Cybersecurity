GCS_Course_Organizer/
├── src/
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main.py               # entrypoint that boots CourseOrganizerApp
│   │   ├── sidebar/              # ← Core Feature 2 lives here
│   │   │   ├── __init__.py
│   │   │   ├── sidebar.py        # Sidebar widget implementation
│   │   │   ├── sidebar.css       # (if you add styling files or themes)
│   │   │   └── test_sidebar.py   # unit tests for the sidebar
│   │   └── detail_pane/          # placeholder for later features
│   │       └── __init__.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── course_api.py         # fetch_course_list, fetch_modules
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── note_tracker.py
│   │   ├── transcript_fetcher.py
│   │   ├── glossary_matcher.py
│   │   └── badge_engine.py
│   └── models/
│       ├── __init__.py
│       ├── course.py             # Course, Module, Element dataclasses
│       └── progress.py           # ElementProgress schema
└── requirements.txt

