from playwright.sync_api import sync_playwright
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"


def html_to_pdf(html_path: Path, pdf_name="resume.pdf"):
    pdf_path = OUTPUT_DIR / pdf_name

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(f"file:///{html_path.resolve()}", wait_until="networkidle")

        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={
                "top": "0.5cm",
                "bottom": "0.5cm",
                "left": "0.5cm",
                "right": "0.5cm",
            }
        )

        browser.close()

    return pdf_path