from core import system_controller as sc
import subprocess
import shutil

def handle_command(command):
    command = command.lower().strip()

    # Create folder
    if command.startswith("create folder"):
        path = command.replace("create folder", "").strip()
        return sc.create_folder(path)

    # Delete folder
    elif command.startswith("delete folder"):
        path = command.replace("delete folder", "").strip()
        return sc.delete_folder(path)

    # Create file
    elif command.startswith("create file"):
        path = command.replace("create file", "").strip()
        return sc.create_file(path)

    # Delete file
    elif command.startswith("delete file"):
        path = command.replace("delete file", "").strip()
        return sc.delete_file(path)

    # Open app
    elif command.startswith("open "):
        app_name = command.replace("open ", "").strip()
        app_path = shutil.which(app_name)

        if app_path:
            subprocess.Popen([app_path])
            return f"✅ Opened {app_name}"

        # Fallback mapping for common applications
        fallback_apps = {
            "firefox": "firefox",
            "chrome": "google-chrome",
            "vscode": "code",
            "code": "code",
            "terminal": "gnome-terminal",
            "calculator": "gnome-calculator",
            "files": "nautilus",
            "text editor": "gedit"
        }

        if app_name in fallback_apps:
            try:
                subprocess.Popen([fallback_apps[app_name]])
                return f"✅ Opened {app_name}"
            except FileNotFoundError:
                return f"❌ {app_name} is not installed."

        return f"❌ Could not find application: {app_name}"

    # Unknown command
    else:
        return f"❓ Unknown command: {command}"
