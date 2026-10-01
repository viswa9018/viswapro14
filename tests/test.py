import re
import sys
from pathlib import Path


INDEX = Path("index.html")


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


def passed(message, points):
    print(f"PASS ({points}/50): {message}")


if not INDEX.exists():
    fail("index.html was not found.")


html = INDEX.read_text(encoding="utf-8")

# Remove CSS comments to avoid accidentally matching commented-out answers.
clean_html = re.sub(r"/\*.*?\*/", "", html, flags=re.DOTALL)


# --------------------------------------------------
# Test 1: body position relative - 10 points
# --------------------------------------------------

body_match = re.search(
    r"body\s*\{([^}]*)\}",
    clean_html,
    re.IGNORECASE | re.DOTALL
)

if not body_match:
    fail("Could not find a body CSS rule.")

body_css = body_match.group(1)

if not re.search(
    r"position\s*:\s*relative\s*;",
    body_css,
    re.IGNORECASE
):
    fail("body must have position: relative;")

passed("body uses position: relative.", 10)


# --------------------------------------------------
# Test 2: aside position absolute - 15 points
# --------------------------------------------------

aside_match = re.search(
    r"aside\s*\{([^}]*)\}",
    clean_html,
    re.IGNORECASE | re.DOTALL
)

if not aside_match:
    fail("Could not find an aside CSS rule.")

aside_css = aside_match.group(1)

if not re.search(
    r"position\s*:\s*absolute\s*;",
    aside_css,
    re.IGNORECASE
):
    fail("aside must have position: absolute;")

passed("aside uses position: absolute.", 15)


# --------------------------------------------------
# Test 3: right: 30px - 10 points
# --------------------------------------------------

if not re.search(
    r"right\s*:\s*30px\s*;",
    aside_css,
    re.IGNORECASE
):
    fail("aside must have right: 30px;")

passed("aside is positioned 30px from the right.", 10)


# --------------------------------------------------
# Test 4: top: 50px - 10 points
# --------------------------------------------------

if not re.search(
    r"top\s*:\s*50px\s*;",
    aside_css,
    re.IGNORECASE
):
    fail("aside must have top: 50px;")

passed("aside is positioned 50px from the top.", 10)


# --------------------------------------------------
# Test 5: required HTML/content - 5 points
# --------------------------------------------------

required_strings = [
    "<main>",
    "<aside>",
    "Our speakers this season",
    "Jeffrey Toobin",
    "Andrew Ross Sorkin",
    "Amy Chua",
    "Please contact us for tickets.",
    "Enter to win a free ticket!"
]

missing = []

for item in required_strings:
    if item not in html:
        missing.append(item)

if missing:
    fail(
        "Required HTML/content is missing: "
        + ", ".join(missing)
    )

passed("Required HTML structure and content are preserved.", 5)


# --------------------------------------------------
# Final result
# --------------------------------------------------

print()
print("ALL TESTS PASSED")
print("SCORE: 50/50")
sys.exit(0)
