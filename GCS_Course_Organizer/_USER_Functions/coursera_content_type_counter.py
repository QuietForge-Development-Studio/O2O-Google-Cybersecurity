import sys                         # ← add this
import requests
from bs4 import BeautifulSoup
import json
import time

# Corrected list of the 9 GCP Cybersecurity courses
COURSE_URLS = [
    "https://www.coursera.org/learn/foundations-of-cybersecurity",
    "https://www.coursera.org/learn/network-security",         # ← fixed
    "https://www.coursera.org/learn/linux-security",
    "https://www.coursera.org/learn/python-for-cybersecurity",
    "https://www.coursera.org/learn/incident-response",
    "https://www.coursera.org/learn/computer-forensics",       # renamed
    "https://www.coursera.org/learn/security-controls",
    "https://www.coursera.org/learn/siem-in-cybersecurity",    # check exact slug
    "https://www.coursera.org/learn/security-practicum"
]

def get_content_types_from_course(url):
    types = []
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    for label in soup.select("span.content-type-label"):
        txt = label.get_text(strip=True)
        if txt:
            types.append(txt)

    for li in soup.select("li.syllabus-item"):
        aria = li.get("aria-label", "")
        if ":" in aria:
            t = aria.split(":",1)[0].strip()
            types.append(t)

    return types

def main():
    all_counts = {}
    for url in COURSE_URLS:
        time.sleep(1)
        try:
            course_types = get_content_types_from_course(url)
        except Exception as e:
            print(f"⚠️ failed to parse {url}: {e}", file=sys.stderr)
            continue

        for t in course_types:
            all_counts[t] = all_counts.get(t, 0) + 1

    result = {
        "types": sorted(all_counts.keys()),
        "counts": all_counts
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
# This script counts the types of content in the specified Coursera courses.
# It fetches the course pages, extracts content types, and aggregates the counts.