is_done = False
all_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
while not is_done:
    formatter = input("Choose a formatter: ")
    if formatter == '!done':
        is_done = True
        break
    elif formatter == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif formatter not in all_formatters:
        print("Unknown formatting type or command")
    elif formatter in all_formatters:
        is_done = False
