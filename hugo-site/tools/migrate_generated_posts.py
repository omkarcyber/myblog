from html import unescape
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

posts = [
    {
        "source": "posts/forensic_question_post/index.html",
        "target": "digital-forensics/guides/forensic-question/index.md",
        "title": "Forensic Q&A",
        "summary": "In this post, I will solve some standard forensic questions.",
        "tags": ["forensic-qa"],
        "url": "/posts/forensic_question_post/",
    },
    {
        "source": "posts/testing_markdown/index.html",
        "target": "digital-forensics/guides/testing-markdown/index.md",
        "title": "For Website Developer",
        "summary": "For website development and Markdown testing.",
        "tags": ["internal-document", "lab3"],
        "url": "/posts/testing_markdown/",
    },
    {
        "source": "category/tools/ddddfldd/index.html",
        "target": "digital-forensics/tools/ddddfldd/index.md",
        "title": "dd, dcfldd, dc3dd Data Acquisition Tools for Linux",
        "summary": "Understanding dd, dcfldd, and dc3dd commands.",
        "tags": ["data-acquisition", "linux"],
        "url": "/category/tools/ddddfldd/",
    },
    {
        "source": "category/tools/mpetool/index.html",
        "target": "digital-forensics/tools/mpetool/index.md",
        "title": "MPE+ Tool",
        "summary": "Mobile device data review tool.",
        "tags": ["mpe", "mobile-forensic"],
        "url": "/category/tools/mpetool/",
    },
    {
        "source": "category/tools/pathfinder_tool/index.html",
        "target": "digital-forensics/tools/pathfinder-tool/index.md",
        "title": "Cellebrite PathFinder Tool",
        "summary": "Forensic data analysis and visualization tool.",
        "tags": ["cellebrite", "visualization"],
        "url": "/category/tools/pathfinder_tool/",
    },
    {
        "source": "category/tools/timestomping/index.html",
        "target": "digital-forensics/tools/timestomping/index.md",
        "title": "NTFS and ext4 File Stomping",
        "summary": "Manipulating timestamps of files stored in NTFS or ext4 file systems.",
        "tags": ["lab3", "linux"],
        "url": "/category/tools/timestomping/",
    },
    {
        "source": "category/casestudy/casestudy_cellebriteufed/index.html",
        "target": "digital-forensics/case-studies/cellebrite-ufed/index.md",
        "title": "Case Study on Cellebrite UFED Tool",
        "summary": "Key evidence found by Mumbai Forensic Cell in a murder case using Cellebrite solutions.",
        "tags": ["case-study", "cellebrite", "mobile-forensic"],
        "url": "/category/casestudy/casestudy_cellebriteufed/",
    },
    {
        "source": "category/casestudy/casestudy_mpe_tool/index.html",
        "target": "digital-forensics/case-studies/mpe-tool/index.md",
        "title": "Case Study on MPE+ Tool",
        "summary": "A case study about the use of the MPE+ mobile forensic tool.",
        "tags": ["case-study", "mpe", "mobile-forensic"],
        "url": "/category/casestudy/casestudy_mpe_tool/",
    },
]


def committed_file(path):
    result = subprocess.run(
        ["git", "show", f"HEAD:{path}"],
        cwd=ROOT.parent,
        check=True,
        capture_output=True,
    )
    return result.stdout.decode("utf-8")


def extract_body(html):
    marker = '<section class="section content has-text-justified">'
    start = html.index(marker) + len(marker)
    end = html.index("</section>", start)
    return html[start:end].strip()


def front_matter(post):
    tags = ", ".join(f'"{tag}"' for tag in post["tags"])
    return (
        "---\n"
        f'title: "{post["title"]}"\n'
        f'summary: "{post["summary"]}"\n'
        f'tags: [{tags}]\n'
        f'url: "{post["url"]}"\n'
        "---\n\n"
    )


for post in posts:
    output = CONTENT / post["target"]
    output.parent.mkdir(parents=True, exist_ok=True)
    body = unescape(extract_body(committed_file(post["source"])))
    output.write_text(front_matter(post) + body + "\n", encoding="utf-8")

for path, title, summary in [
    ("digital-forensics/_index.md", "Digital Forensics", "Evidence collection, examination, forensic tools, investigations, guides, and case studies."),
    ("digital-forensics/guides/_index.md", "Guides and Q&A", "Forensic guides and practical questions and answers."),
    ("digital-forensics/tools/_index.md", "Forensic Tools", "Investigations of tools used in digital forensic work."),
    ("digital-forensics/case-studies/_index.md", "Case Studies", "Real-world forensic tool and investigation case studies."),
    ("ceh-malware-analysis/_index.md", "CEH and Malware Analysis", "Ethical hacking, reconnaissance, malware research, and analysis workflows."),
    ("soc-operations/_index.md", "SOC Operations", "Alert triage, detection engineering, incident response, and blue-team workflows."),
]:
    output = CONTENT / path
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(f'---\ntitle: "{title}"\n---\n\n{summary}\n', encoding="utf-8")

print(f"Migrated {len(posts)} generated pages into Hugo content bundles.")
