from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# ---------- LOAD PROJECTS ----------
def load_projects():
    try:
        with open("projects.json", "r") as f:
            data = json.load(f)
            return data if data else []
    except:
        return []


# ---------- HOME ----------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    projects = load_projects()

    return templates.TemplateResponse(request,
        "index.html",
        {
            "request": request,
            "projects": projects
        }
    )


# ---------- EMAIL CONFIG ----------
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


# ---------- CONTACT ----------
@app.post("/contact")
def contact(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):

    if not EMAIL_SENDER or not EMAIL_PASSWORD:
        return JSONResponse({
            "success": False,
            "msg": "Email config missing in .env"
        })

    subject = f"New Portfolio Message from {name}"

    body = f"""
New message received:

Name: {name}
Email: {email}
Message: {message}
"""

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)

        full_message = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            EMAIL_SENDER,
            EMAIL_RECEIVER,
            full_message
        )

        server.quit()

        return JSONResponse({
            "success": True,
            "msg": "Email sent successfully!"
        })

    except Exception as e:
        return JSONResponse({
            "success": False,
            "msg": str(e)
        })