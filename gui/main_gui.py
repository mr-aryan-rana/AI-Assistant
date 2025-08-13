import tkinter as tk
from tkinter import scrolledtext

def submit():
    query = entry.get()
    response = run_chain(query)  # Or use run_graph()
    chat_log.insert(tk.END, f"You: {query}\nAI: {response}\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI Assistant")

chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, width=100)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=submit)
send_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
