"""Generate the public resume. Requires reportlab and pypdf; run from any directory."""

from pathlib import Path
from shutil import copyfile

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/siabul-hassan-resume.pdf"
PUBLIC = ROOT / "static/resume/Siabul-Hassan-Resume.pdf"
LEGACY_PUBLIC = ROOT / "static/siabul-hassan-resume.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
INK = colors.HexColor("#172b40")
TEXT = colors.HexColor("#28333e")
MUTED = colors.HexColor("#536171")
styles = {
    "name": ParagraphStyle(
        "name",
        fontName="Helvetica-Bold",
        fontSize=26,
        leading=30,
        textColor=INK,
        spaceAfter=5,
    ),
    "role": ParagraphStyle(
        "role",
        fontName="Helvetica",
        fontSize=11,
        leading=15,
        textColor=INK,
        spaceAfter=7,
    ),
    "contact": ParagraphStyle(
        "contact", fontName="Helvetica", fontSize=9, leading=13, textColor=MUTED
    ),
    "body": ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=TEXT,
        spaceAfter=3,
    ),
    "section": ParagraphStyle(
        "section",
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=14,
        textColor=INK,
        spaceBefore=12,
        spaceAfter=4,
    ),
    "project": ParagraphStyle(
        "project",
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=15,
        textColor=INK,
        spaceBefore=7,
        spaceAfter=2,
    ),
    "meta": ParagraphStyle(
        "meta",
        fontName="Helvetica",
        fontSize=9,
        leading=12.5,
        textColor=MUTED,
        spaceAfter=3,
    ),
    "bullet": ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=TEXT,
        leftIndent=10,
        firstLineIndent=-8,
        spaceAfter=2,
    ),
}


def p(text, style="body"):
    return Paragraph(text, styles[style])


def section(title):
    return [
        p(title.upper(), "section"),
        HRFlowable(
            width="100%", thickness=0.5, color=colors.HexColor("#b6c0c9"), spaceAfter=6
        ),
    ]


def project(title, repo, stack, bullets, url=None, display_url=None):
    project_url = url or f"https://github.com/HexCore99/{repo}"
    project_display = display_url or f"github.com/HexCore99/{repo}"
    return KeepTogether(
        [
            p(
                f'{title} <font name="Helvetica" size="8.5" color="#536171"> | <link href="{project_url}">{project_display}</link></font>',
                "project",
            ),
            p(stack, "meta"),
            *[p("- " + line, "bullet") for line in bullets],
        ]
    )


story = [
    p("Siabul Hassan", "name"),
    p("Software Developer | Desktop / Systems &amp; Full-Stack", "role"),
    p(
        'Tongi, Dhaka, Bangladesh | <link href="tel:+8801572923076">+880 1572-923076</link> | <link href="mailto:siabulhassan@gmail.com">siabulhassan@gmail.com</link>',
        "contact",
    ),
    p(
        '<link href="https://github.com/HexCore99/">github.com/HexCore99</link> | <link href="https://www.linkedin.com/in/siabul-hassan/">linkedin.com/in/siabul-hassan</link> | Portfolio: <link href="https://siabulhassan.xyz/">siabulhassan.xyz</link>',
        "contact",
    ),
    Spacer(1, 10),
    p(
        "Computer Science &amp; Engineering undergraduate building desktop applications, Windows utilities, and full-stack web platforms. Project work spans Rust, C++, React, and SQL-backed applications, including packaged desktop releases."
    ),
    *section("Education"),
    p("<b>B.Sc. in Computer Science &amp; Engineering</b>"),
    p("United International University | Aug 2023 - Expected 2028"),
    p("<b>CGPA:</b> 3.90 | 9th Trimester"),
    p(
        "<b>Scholarships:</b> Multiple 25% and 50% scholarships awarded during undergraduate studies."
    ),
    p(
        "<b>Relevant coursework:</b> Data Structures &amp; Algorithms, Object-Oriented Programming, Database Systems, Microprocessors."
    ),
    *section("Technical skills"),
    p("<b>Languages:</b> C, C++, Rust, JavaScript, Python, Java"),
    p(
        "<b>Desktop / systems:</b> Tauri 2, raylib, SDL3, CLI tools, Windows file-system tooling"
    ),
    p(
        "<b>Frontend:</b> React, SvelteKit, Next.js, Tailwind CSS, Zustand, Redux Toolkit"
    ),
    p("<b>Backend / data:</b> Express, Flask, SQLite, MySQL, JWT; TensorFlow/Keras"),
    *section("Selected projects"),
    project(
        "Taskora",
        "Taskora",
        "Tauri 2 / Rust / React / SQLite / Zustand",
        [
            "Built a Kanban desktop app with projects, boards, and task details in one workspace.",
            "Used a Rust backend and SQLite for on-device storage; published downloadable release builds.",
        ],
    ),
    project(
        "WhoLocks",
        "wholocks",
        "Rust / Windows / CLI and GUI",
        [
            "Built a Windows utility to identify processes locking files or folders.",
            "Added File Explorer integration and CLI and GUI workflows; published downloadable releases.",
        ],
    ),
    project(
        "QuickJudge",
        "QuickJudge",
        "React / Express / MySQL / Redux Toolkit / JWT",
        [
            "Developed an online judge and programming-contest platform with problem sets, submissions, and leaderboards.",
            "Implemented authenticated student and admin workflows with a SQL-backed application.",
        ],
    ),
    project(
        "HexSolve",
        "hexcore99.github.io",
        "C / C++ / Data Structures / Algorithms",
        [
            "Built an organized programming-solutions archive covering fundamentals, searching, sorting, linked lists, graphs, and other DSA topics.",
        ],
        url="https://hexcore99.github.io/",
        display_url="hexcore99.github.io",
    ),
    project(
        "Neural Movie Recommender",
        "neural-movie-recommender",
        "Python / TensorFlow/Keras / Flask / Next.js",
        [
            "Connected a neural collaborative filtering model to a Flask API and a Next.js interface for movie browsing and recommendations.",
        ],
    ),
]
doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=43,
    leftMargin=43,
    topMargin=35,
    bottomMargin=34,
    title="Siabul Hassan - Resume",
    author="Siabul Hassan",
    subject="Desktop, systems and full-stack software development",
)
doc.build(story)
reader = PdfReader(OUTPUT)
assert len(reader.pages) == 1, f"Expected one page, got {len(reader.pages)}"
text = reader.pages[0].extract_text()
for required in [
    "Siabul Hassan",
    "3.90",
    "WhoLocks",
    "Neural Movie Recommender",
    "1572-923076",
    "HexSolve",
    "siabulhassan.xyz",
]:
    assert required in text, required
copyfile(OUTPUT, PUBLIC)
copyfile(OUTPUT, LEGACY_PUBLIC)
print(f"Created one-page resume: {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")
print(f"Public copy: {PUBLIC}")
