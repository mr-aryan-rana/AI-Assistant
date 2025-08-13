def get_suggestions(user_input):
    commands = [
        "open firefox",
        "open chrome",
        "open terminal",
        "generate image of a sunset",
        "create folder named test",
        "delete file test.txt",
        "multi agent planning",
        "use planner",
        "create file hello.txt",
        "delete folder ai-files"
    ]

    user_input = user_input.lower().strip()
    return [cmd for cmd in commands if user_input in cmd]
