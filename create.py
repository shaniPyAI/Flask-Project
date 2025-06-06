import os

PROJECT_NAME = "Flask_Pwa_project"

os.makedirs(PROJECT_NAME, exist_ok=True)

os.makedirs(os.path.join(PROJECT_NAME, "app"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_NAME, "instance"), exist_ok=True)

with open(os.path.join(PROJECT_NAME, "run.py"), "w") as f:
    f.write("#run.py\n")
    f.write("from app import create_app\n")
    f.write("app = create_app()\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    app.run(debug=True)\n")

os.makedirs(os.path.join(PROJECT_NAME, "app", "static"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_NAME, "app", "static", "css"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_NAME, "app", "static", "js"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_NAME, "app", "static", "media", "images"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_NAME, "app", "static", "media", "videos"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_NAME, "app", "static", "fonts"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_NAME, "app", "templates"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_NAME, "app", "utiles"), exist_ok=True)

with open(os.path.join(PROJECT_NAME, "app", "templates", "index.html"), "w") as f:
    f.write("#index.html\n")
    f.write("<!DOCTYPE html>\n<html lang=\"fa\" dir=\"rtl\" manifest=\"/manifest.json\">\n")
    f.write("<head><meta charset=\"UTF-8\"><title>Flask_Pwa_project</title></head>\n")
    f.write("<body><h1>Flask_Pwa_project</h1></body>\n</html>\n")

with open(os.path.join(PROJECT_NAME, "app", "static", "css", "styles.css"), "w") as f:
    f.write("#styles.css\n")
with open(os.path.join(PROJECT_NAME, "app", "static", "js", "main.js"), "w") as f:
    f.write("#main.js\n")
with open(os.path.join(PROJECT_NAME, "app", "static", "manifest.json"), "w") as f:
    f.write("#manifest.json\n")
    f.write('{"name": "Flask_Pwa_project", "short_name": "Flask_Pwa_project", "start_url": "/", "display": "standalone"}\n')
with open(os.path.join(PROJECT_NAME, "app", "static", "service-worker.js"), "w") as f:
    f.write("#service-worker.js\n")
    f.write("self.addEventListener('install', (event) => {});\n")

with open(os.path.join(PROJECT_NAME, "app", "utiles", "__init__.py"), "w") as f:
    f.write("#__init__.py\n")
with open(os.path.join(PROJECT_NAME, "app", "utiles", "config.py"), "w") as f:
    f.write("#config.py\n")
    f.write("class Config:\n    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/users.db'\n    SQLALCHEMY_TRACK_MODIFICATIONS = False\n")
with open(os.path.join(PROJECT_NAME, "app", "utiles", "models.py"), "w") as f:
    f.write("#models.py\n")
    f.write("from flask_sqlalchemy import SQLAlchemy\n")
    f.write("db = SQLAlchemy()\n")
    f.write("class User(db.Model):\n    id = db.Column(db.Integer, primary_key=True)\n    first_name = db.Column(db.String(50), nullable=False)\n    last_name = db.Column(db.String(50), nullable=False)\n    email = db.Column(db.String(120), unique=True, nullable=False)\n    mobile = db.Column(db.String(15), nullable=False)\n    status = db.Column(db.String(10), nullable=False)\n    password = db.Column(db.String(128), nullable=False)\n    created_at = db.Column(db.DateTime, server_default=db.func.now())\n")
with open(os.path.join(PROJECT_NAME, "app", "utiles", "routes.py"), "w") as f:
    f.write("#routes.py\n")
with open(os.path.join(PROJECT_NAME, "app", "utiles", "auth.py"), "w") as f:
    f.write("#auth.py\n")
with open(os.path.join(PROJECT_NAME, "app", "utiles", "view.py"), "w") as f:
    f.write("#view.py\n")

print(f"The  {PROJECT_NAME} Project was complated successfuly ")
