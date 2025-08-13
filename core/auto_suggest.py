import readline

# Predefined list of common user commands
SUGGESTIONS = [
    "open firefox",
    "open terminal",
    "open file manager",
    "open calculator",
    "show system info",
    "generate image",
    "create image of sunset",
    "multi agent planner",
    "exit",
    "quit",
    "clear",
    "run command ls -l",
    "run command top",
    "run command df -h",
    "open vscode",
    "open settings",
]

def completer(text, state):
    """Return autocomplete suggestions for user input."""
    matches = [cmd for cmd in SUGGESTIONS if cmd.startswith(text.lower())]
    if state < len(matches):
        return matches[state]
    else:
        return None

def enable_autocomplete():
    """Enable tab-based autocomplete for terminal input."""
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")
