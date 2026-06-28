from jinja2 import Environment, FileSystemLoader
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "template"
OUTPUT_DIR = BASE_DIR / "output"


env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=True
)


def render(template_name: str, data: dict):
    template = env.get_template(template_name)
    return template.render(**data)


def save_html(html: str, filename="resume.html"):
    path = OUTPUT_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path