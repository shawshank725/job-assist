from ollama import chat
from pathlib import Path
import json
from src.loader import load_json
import copy

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

SETTINGS_FILE = DATA_DIR / "settings.json"
USER_FILE = DATA_DIR / "userdata.json"

def rewrite_description(settings, job_description, title, tech_stack, description):
    prompt = (
        settings["prompt"]
        + "\n\nJOB DESCRIPTION:\n"
        + job_description
        + "\n\nTITLE:\n"
        + title
        + "\n\nTECH STACK:\n"
        + ", ".join(tech_stack)
        + "\n\nDESCRIPTION:\n"
        + json.dumps(description, indent=2)
    )

    response = chat(
        model=settings["model_name"],
        messages=[
            {
                "role": settings["role"],
                "content": prompt,
            }
        ],
    )

    return json.loads(response["message"]["content"])

def send_jd_to_model(job_description):
    settings = load_json("settings.json")
    user_data = load_json("userdata.json")

    tailored_data = copy.deepcopy(user_data)

    for experience in tailored_data["experiences"]:
        try:
            experience["description"] = rewrite_description(
                settings,
                job_description,
                experience["role"],
                experience["tech_stack_used"],
                experience["description"],
            )
        except Exception:
            pass

    for project in tailored_data["projects"]:
        try:
            project["description"] = rewrite_description(
                settings,
                job_description,
                project["project_name"],
                project["tech_stack_used"],
                project["description"],
            )
        except Exception:
            pass

    print(tailored_data)
    return tailored_data
