from src.loader import load_json
from src.renderer import render, save_html
from src.html_to_pdf import html_to_pdf

# this method takes the user data, uses jinja2 template to convert it HTML, 
# use the pdf method to convert it to PDF
def create_resume_pdf(data):
    html = render("template.html", data)
    html_path = save_html(html)

    pdf_path = html_to_pdf(html_path)

    print("Generated:")
    print(html_path)
    print(pdf_path)
