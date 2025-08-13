import tkinter as tk
from tkinter import scrolledtext
from core.voice_input import listen_to_voice
from core.text_to_speech import speak
from core.system_controller import run_system_command
from chains.basic_chain import run_chain
from chains.multi_agent_graph import run_graph

IMAGE_TRIGGER = ["generate image", "create image", "make an image"]
USE_LANGGRAPH_TRIGGER = ["multi agent", "use planner", "collaborate"]

class AIAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Assistant")

        self.chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
        self.chat_log.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=70)
        self.entry.pack(side=tk.LEFT, padx=10, pady=10)
        self.entry.bind("<Return>", self.process_text_input)

        self.send_button = tk.Button(root, text="Send", command=self.process_text_input)
        self.send_button.pack(side=tk.LEFT)

        self.voice_button = tk.Button(root, text="🎤 Speak", command=self.process_voice_input)
        self.voice_button.pack(side=tk.LEFT)

    def display(self, sender, message):
        self.chat_log.insert(tk.END, f"{sender}: {message}\n")
        self.chat_log.see(tk.END)

    def process_text_input(self, event=None):
        user_input = self.entry.get().strip()
        if user_input:
            self.entry.delete(0, tk.END)
            self.respond(user_input)

    def process_voice_input(self):
        self.display("🟢 You (Voice)", "Listening...")
        user_input = listen_to_voice()
        self.display("🟢 You", user_input)
        self.respond(user_input)

    def respond(self, user_input):
        if any(trigger in user_input.lower() for trigger in IMAGE_TRIGGER):
            from scripts.generate_image import generate_image
            generate_image(user_input)
            self.display("🤖 AI", "Image generated and saved to outputs.")
            return

        if "open" in user_input.lower():
            result = run_system_command(user_input)
            self.display("🖥️ System", result)
            return

        if any(trigger in user_input.lower() for trigger in USE_LANGGRAPH_TRIGGER):
            response = run_graph(user_input)
        else:
            response = run_chain(user_input)

        self.display("🤖 AI", response)
        speak(response)

def start_gui():
    root = tk.Tk()
    gui = AIAssistantGUI(root)
    root.mainloop()

if __name__ == "__main__":
    start_gui()