# #!/usr/bin/env python3
# import os
# import subprocess
# import time
# from chains.basic_chain import run_chain
# from chains.multi_agent_graph import run_graph


# # ✅ Configuration
# MODEL = "llama2"  # Change to gemma, mistral, deepseek-coder, etc.
# # IMAGE_TRIGGER = ["generate image", "create image", "make an image"]
# IMAGE_TRIGGER = ["generate image", "create image", "make an image"]

# # if any(trigger in user_input.lower() for trigger in IMAGE_TRIGGER):
# #     generate_image()
# #     continue

# # ✅ Paths
# BASE_DIR = os.path.expanduser("~/ai-assistant")
# LOG_FILE = os.path.join(BASE_DIR, "outputs/conversations.log")
# IMG_SCRIPT = os.path.join(BASE_DIR, "scripts/generate_image.py")


# def log_conversation(user_input, ai_response):
#     with open(LOG_FILE, "a") as log:
#         log.write(f"\n🟢 You: {user_input}\n🤖 AI: {ai_response}\n")


# def run_ollama(prompt):
#     try:
#         process = subprocess.Popen(
#             ["ollama", "run", MODEL],
#             stdin=subprocess.PIPE,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#         )
#         output, error = process.communicate(input=prompt.encode(), timeout=120)
#         return output.decode(errors="ignore")
#     except Exception as e:
#         return f"[Error running model: {e}]"


# # def generate_image():
# #     print("🎨 Generating image...")
# #     try:
# #         subprocess.run(["python3", IMG_SCRIPT], check=True)
# #         print("✅ Image saved to outputs/generated_image.png")
# #     except subprocess.CalledProcessError as e:
# #         print(f"[Image generation failed] {e}")

# def generate_image(prompt="A futuristic city at sunset with neon lights"):
#     print("🎨 Generating image...")
#     try:
#         subprocess.run(["python3", IMG_SCRIPT, prompt], check=True)
#         print("✅ Image saved to outputs/generated_image.png")
#     except subprocess.CalledProcessError as e:
#         print(f"[Image generation failed] {e}")


# # def main():
# #     print("\n🤖 AI Terminal Assistant is ready. Type 'exit' to quit.\n")

# #     while True:
# #         try:
# #             user_input = input("🟢 You: ").strip()
# #             if user_input.lower() in ["exit", "quit"]:
# #                 print("👋 Exiting. Goodbye!")
# #                 break

# #             # 🔍 Trigger image generation script
# #             if any(trigger in user_input.lower() for trigger in IMAGE_TRIGGER):
# #                 generate_image()
# #                 continue

# #             print("🤖 Thinking...")
# #             response = run_ollama(user_input)
# #             print("\n🤖 AI:\n", response.strip())
# #             log_conversation(user_input, response.strip())

# #         except KeyboardInterrupt:
# #             print("\n[Interrupted]")
# #             break
# #         except Exception as e:
# #             print(f"[Error] {e}")
# #             continue


# USE_LANGGRAPH_TRIGGER = ["multi agent", "use planner", "collaborate"]

# def main():
#     print("\n🤖 AI Terminal Assistant (LangChain + LangGraph) is ready. Type 'exit' to quit.\n")

#     while True:
#         try:
#             user_input = input("🟢 You: ").strip()
#             if user_input.lower() in ["exit", "quit"]:
#                 print("👋 Exiting. Goodbye!")
#                 break

#             # 🎨 Image generation
#             if any(trigger in user_input.lower() for trigger in IMAGE_TRIGGER):
#                 generate_image()
#                 continue

#             # 🔁 LangGraph workflow
#             if any(trigger in user_input.lower() for trigger in USE_LANGGRAPH_TRIGGER):
#                 print("🔄 Running LangGraph workflow...")
#                 response = run_graph(user_input)
#             else:
#                 print("💬 Running LangChain chain...")
#                 response = run_chain(user_input)

#             print("\n🤖 AI:\n", response.strip())
#             log_conversation(user_input, response.strip())

#         except KeyboardInterrupt:
#             print("\n[Interrupted]")
#             break
#         except Exception as e:
#             print(f"[Error] {e}")
#             continue


# if __name__ == "__main__":
#     main()
#!/usr/bin/env python3
# import os
# import subprocess
# import time
# import platform
# import shutil
# import psutil
# from chains.basic_chain import run_chain
# from chains.multi_agent_graph import run_graph

# # ✅ Configuration
# MODEL = "llama2"
# IMAGE_TRIGGER = ["generate image", "create image", "make an image"]
# USE_LANGGRAPH_TRIGGER = ["multi agent", "use planner", "collaborate"]
# OPEN_APP_TRIGGER = ["open "]
# SYSTEM_INFO_TRIGGER = ["system info", "get system info", "device info"]

# # ✅ Paths
# BASE_DIR = os.path.expanduser("~/ai-assistant")
# LOG_FILE = os.path.join(BASE_DIR, "outputs/conversations.log")
# IMG_SCRIPT = os.path.join(BASE_DIR, "scripts/generate_image.py")


# def log_conversation(user_input, ai_response):
#     with open(LOG_FILE, "a") as log:
#         log.write(f"\n🟢 You: {user_input}\n🤖 AI: {ai_response}\n")


# def run_ollama(prompt):
#     try:
#         process = subprocess.Popen(
#             ["ollama", "run", MODEL],
#             stdin=subprocess.PIPE,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#         )
#         output, error = process.communicate(input=prompt.encode(), timeout=120)
#         return output.decode(errors="ignore")
#     except Exception as e:
#         return f"[Error running model: {e}]"


# def generate_image(prompt="A futuristic city at sunset with neon lights"):
#     print("🎨 Generating image...")
#     try:
#         subprocess.run(["python3", IMG_SCRIPT, prompt], check=True)
#         print("✅ Image saved to outputs/generated_image.png")
#     except subprocess.CalledProcessError as e:
#         print(f"[Image generation failed] {e}")


# def open_app(app_name):
#     app_path = shutil.which(app_name)
#     if app_path:
#         subprocess.Popen([app_path])
#         print(f"✅ Opening {app_name}")
#         return

#     # Fallback app name mapping
#     fallback = {
#         "calculator": "gnome-calculator",
#         "terminal": "gnome-terminal",
#         "firefox": "firefox",
#         "vscode": "code",
#         "text editor": "gedit",
#         "file manager": "nautilus",
#     }

#     for key in fallback:
#         if key in app_name:
#             subprocess.Popen([fallback[key]])
#             print(f"✅ Opening {fallback[key]}")
#             return

#     print(f"❌ App '{app_name}' not found.")


# def get_system_info():
#     info = {
#         "OS": platform.system(),
#         "Version": platform.version(),
#         "Architecture": platform.machine(),
#         "Processor": platform.processor(),
#         "CPU Cores": psutil.cpu_count(logical=False),
#         "RAM": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
#         "Disk": f"{round(psutil.disk_usage('/').total / (1024**3), 2)} GB",
#     }
#     print("🖥️ System Info:")
#     for k, v in info.items():
#         print(f"{k}: {v}")


# def main():
#     print("\n🤖 AI Terminal Assistant (LangChain + LangGraph) is ready. Type 'exit' to quit.\n")

#     while True:
#         try:
#             user_input = input("🟢 You: ").strip().lower()

#             if user_input in ["exit", "quit"]:
#                 print("👋 Exiting. Goodbye!")
#                 break

#             # 🎨 Image generation
#             if any(trigger in user_input for trigger in IMAGE_TRIGGER):
#                 generate_image(user_input)
#                 continue

#             # 🔄 LangGraph
#             if any(trigger in user_input for trigger in USE_LANGGRAPH_TRIGGER):
#                 print("🔁 Running LangGraph...")
#                 response = run_graph(user_input)

#             # 📂 Open system apps
#             elif user_input.startswith("open "):
#                 app_name = user_input.replace("open ", "").strip()
#                 open_app(app_name)
#                 response = f"Trying to open '{app_name}'..."

#             # 🧠 System info
#             elif any(trigger in user_input for trigger in SYSTEM_INFO_TRIGGER):
#                 get_system_info()
#                 response = "Fetched system info."

#             # 💬 LangChain basic response
#             else:
#                 print("💬 Running LangChain chain...")
#                 response = run_chain(user_input)

#             print("\n🤖 AI:\n", response.strip())
#             log_conversation(user_input, response.strip())

#         except KeyboardInterrupt:
#             print("\n👋 Interrupted.")
#             break
#         except Exception as e:
#             print(f"[Error] {e}")
#             continue


# if __name__ == "__main__":
#     main()
#!/usr/bin/env python3
# import os
# from core.auto_suggest import enable_autocomplete
# from core.voice_input import listen_to_voice
# from core.text_to_speech import speak
# from core.system_controller import run_system_command
# from chains.basic_chain import run_chain
# from chains.multi_agent_graph import run_graph
# from scripts.generate_image import generate_image
# from core.gui_interface import start_gui
# from core.command_handler import handle_command
# from core.voice_input import listen_to_voice
# from core.text_to_speech import speak
# from core.auto_complete import get_suggestions

# IMAGE_TRIGGER = ["generate image", "create image", "make an image"]
# USE_LANGGRAPH_TRIGGER = ["multi agent", "use planner", "collaborate"]
# LOG_FILE = os.path.expanduser("~/ai-assistant/outputs/conversations.log")

# def log_conversation(user_input, ai_response):
#     with open(LOG_FILE, "a") as log:
#         log.write(f"\n🟢 You: {user_input}\n🤖 AI: {ai_response}\n")

# def terminal_mode():
#     print("\n🤖 AI Terminal Assistant is ready. Type 'exit' to quit.\n")
#     enable_autocomplete()

#     while True:
#         try:
#             user_input = input("🟢 You: ").strip()
#             if user_input.lower() in ["exit", "quit"]:
#                 print("👋 Exiting. Goodbye!")
#                 break

#             if any(trigger in user_input.lower() for trigger in IMAGE_TRIGGER):
#                 generate_image(user_input)
#                 continue

#             if "open" in user_input.lower():
#                 result = run_system_command(user_input)
#                 print("🖥️ System:", result)
#                 continue

#             if any(trigger in user_input.lower() for trigger in USE_LANGGRAPH_TRIGGER):
#                 response = run_graph(user_input)
#             else:
#                 response = run_chain(user_input)

#             print("\n🤖 AI:\n", response.strip())
#             speak(response)
#             log_conversation(user_input, response.strip())

#         except KeyboardInterrupt:
#             print("\n[Interrupted]")
#             break
#         except Exception as e:
#             print(f"[Error] {e}")
#             continue

# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) > 1 and sys.argv[1] == "gui":
#         start_gui()
#     else:
#         terminal_mode()

# import os
# import sys
# from core.auto_suggest import enable_autocomplete
# from core.auto_complete import get_suggestions
# from core.voice_input import listen_to_voice
# from core.text_to_speech import speak
# from core.system_controller import run_system_command
# from core.command_handler import handle_command
# from scripts.generate_image import generate_image
# from chains.basic_chain import run_chain
# from chains.multi_agent_graph import run_graph
# from core.gui_interface import start_gui
# from core.input_handler import handle_text  # or wherever it is
# # from core.input_handler import handle_text

# # --- Configuration ---
# USE_VOICE_INPUT = False  # Set True for voice input
# IMAGE_TRIGGER = ["generate image", "create image", "make an image"]
# USE_LANGGRAPH_TRIGGER = ["multi agent", "use planner", "collaborate"]
# LOG_FILE = os.path.expanduser("~/ai-assistant/outputs/conversations.log")

# # --- Logging ---
# def log_conversation(user_input, ai_response):
#     try:
#         with open(LOG_FILE, "a") as log:
#             log.write(f"\n🟢 You: {user_input}\n🤖 AI: {ai_response}\n")
#     except Exception as e:
#         print(f"[Log Error] {e}")

# # --- Terminal Chat Loop ---
# def terminal_mode():
#     print("\n🤖 AI Terminal Assistant is ready. Type 'exit' to quit.\n")
#     enable_autocomplete()

#     while True:
#         try:
#             if USE_VOICE_INPUT:
#                 user_input = listen_to_voice()
#                 print(f"🎙️ You said: {user_input}")
#             else:
#                 user_input = input("🟢 You: ").strip()

#             if user_input.lower() in ["exit", "quit"]:
#                 print("👋 Exiting. Goodbye!")
#                 break

#             # Autocomplete suggestion
#             suggestions = get_suggestions(user_input)
#             if suggestions:
#                 print(f"💡 Suggestions: {', '.join(suggestions)}")

#             # Handle image generation
#             if any(trigger in user_input.lower() for trigger in IMAGE_TRIGGER):
#                 generate_image(user_input)
#                 continue

#             # Handle system commands (e.g., open firefox, create folder, etc.)
#             if any(x in user_input.lower() for x in ["open ", "create", "delete", "folder", "file"]):
#                 result = handle_command(user_input)
#                 print("🖥️ System:", result)
#                 log_conversation(user_input, result)
#                 continue

#             # LangGraph agent mode
#             if any(trigger in user_input.lower() for trigger in USE_LANGGRAPH_TRIGGER):
#                 response = run_graph(user_input)
#             else:
#                 response = run_chain(user_input)

#             # Display and speak response
#             print("\n🤖 AI:\n", response.strip())
#             speak(response)
#             log_conversation(user_input, response.strip())

#         except KeyboardInterrupt:
#             print("\n[Interrupted]")
#             break
#         except Exception as e:
#             print(f"[Error] {e}")
#             continue

# # --- Entry Point ---
# if __name__ == "__main__":
#     if len(sys.argv) > 1 and sys.argv[1] == "gui":
#         start_gui()
#     else:
#         terminal_mode()

import os
import sys
from core.auto_suggest import enable_autocomplete
from core.auto_complete import get_suggestions
from core.voice_input import listen_to_voice
from core.text_to_speech import speak
from core.system_controller import run_system_command
from core.command_handler import handle_command
from scripts.generate_image import generate_image
from chains.basic_chain import run_chain
from chains.multi_agent_graph import run_graph
from core.gui_interface import start_gui

# --- Configuration ---
USE_VOICE_INPUT = False  # Set True for voice input
IMAGE_TRIGGER = ["generate image", "create image", "make an image","generate an image","generate a image","generate the image","create a image", "create an image"]
USE_LANGGRAPH_TRIGGER = ["multi agent", "use planner", "collaborate"]
LOG_FILE = os.path.expanduser("~/ai-assistant/outputs/conversations.log")

# --- Logging ---
def log_conversation(user_input, ai_response):
    try:
        with open(LOG_FILE, "a") as log:
            log.write(f"\n🟢 You: {user_input}\n🤖 AI: {ai_response}\n")
    except Exception as e:
        print(f"[Log Error] {e}")

# --- Unified Input Handling ---
def handle_text(user_input):
    u_lower = user_input.lower()

    # 1 - Image generation
    if any(trigger in u_lower for trigger in IMAGE_TRIGGER):
        return generate_image(user_input)

    # 2 - System commands (must start with these)
    if u_lower.startswith(("open ", "create ", "delete ")) or \
       u_lower in ["create folder", "delete folder", "create file", "delete file"]:
        return handle_command(user_input)

    # 3 - LangGraph triggers
    if any(trigger in u_lower for trigger in USE_LANGGRAPH_TRIGGER):
        return run_graph(user_input)

    # 4 - Default: Normal AI Q&A
    return run_chain(user_input)

# --- Terminal Chat Loop ---
def terminal_mode():
    print("\n🤖 AI Terminal Assistant is ready. Type 'exit' to quit.\n")
    enable_autocomplete()

    while True:
        try:
            # Get input
            if USE_VOICE_INPUT:
                user_input = listen_to_voice()
                print(f"🎙️ You said: {user_input}")
            else:
                user_input = input("🟢 You: ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("👋 Exiting. Goodbye!")
                break

            # Autocomplete suggestion
            suggestions = get_suggestions(user_input)
            if suggestions:
                print(f"💡 Suggestions: {', '.join(suggestions)}")

            # Process input
            response = handle_text(user_input)

            # If the handler returned nothing (e.g., for image gen), skip logging/display
            if response is None:
                continue

            # Display and speak
            if isinstance(response, str):
                print("\n🤖 AI:\n", response.strip())
                speak(response)
                log_conversation(user_input, response.strip())
            else:
                # In case functions return non-string objects
                print("\n🤖 AI:\n", str(response))
                log_conversation(user_input, str(response))

        except KeyboardInterrupt:
            print("\n[Interrupted]")
            break
        except Exception as e:
            print(f"[Error] {e}")
            continue

# --- Entry Point ---
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        start_gui()
    else:
        terminal_mode()
