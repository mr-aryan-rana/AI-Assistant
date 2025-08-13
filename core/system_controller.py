import subprocess
import os
import shutil

def run_system_command(command):
    command = command.lower().strip()

    known_apps = {
        "firefox": "firefox",
        "chrome": "google-chrome",
        "code": "code",
        "vscode": "code",
        "terminal": "gnome-terminal",
        "calculator": "gnome-calculator",
        "files": "nautilus",
        "text editor": "gedit",
        "libreoffice": "libreoffice"
    }

    # Handle known apps (e.g., open firefox)
    if command.startswith("open "):
        app = command.replace("open ", "").strip()
        app_cmd = known_apps.get(app)
        if app_cmd:
            try:
                subprocess.Popen([app_cmd])
                return f"✅ Opening {app.capitalize()}..."
            except FileNotFoundError:
                return f"❌ {app.capitalize()} is not installed or not found."
        else:
            return f"❓ Unknown application: {app}"

    # Fallback to custom shell command
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"❌ Command failed:\n{e.output}"

def create_folder(folder_path):
    try:
        folder_path = os.path.expanduser(folder_path)
        os.makedirs(folder_path, exist_ok=True)
        return f"📁 Folder created at: {folder_path}"
    except Exception as e:
        return f"❌ Failed to create folder: {e}"

def delete_folder(folder_path):
    try:
        folder_path = os.path.expanduser(folder_path)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            return f"🗑️ Folder deleted: {folder_path}"
        else:
            return f"⚠️ Folder does not exist: {folder_path}"
    except Exception as e:
        return f"❌ Failed to delete folder: {e}"

def create_file(path):
    try:
        path = os.path.expanduser(path)
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)  # Auto-create parent folder
        with open(path, "w") as f:
            f.write("")  # Create empty file
        return f"📝 File created at: {path}"
    except Exception as e:
        return f"❌ Failed to create file: {e}"

def delete_file(file_path):
    try:
        file_path = os.path.expanduser(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"🗑️ File deleted: {file_path}"
        else:
            return f"⚠️ File does not exist: {file_path}"
    except Exception as e:
        return f"❌ Failed to delete file: {e}"
