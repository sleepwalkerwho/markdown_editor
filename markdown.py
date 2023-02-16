def print_text(all):
    print(all)


def plain_text(text):
    return text


def bold_text(text):
    return f"**{text}**"


def italic_text(text):
    return f"*{text}*"


def inline_code(text):
    return f"`{text}`"


def link(text, url):
    return f"[{text}]({url})"


def header(text, level):
    return f"{level * '#'} {text}\n"


def new_line():
    return "\n"


all_text = ""
is_done = False
all_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line"]
while not is_done:
    formatter = input("Choose a formatter: ")
    if formatter == '!done':
        is_done = True
        break
    elif formatter == "!help":
        print("Available formatters: plain bold italic header link inline-code new-line")
        print("Special commands: !help !done")
    if formatter not in all_formatters:
        print("Unknown formatting type or command")
    else:
        if formatter == 'link':
            label = input("Label: ")
            url = input("URL: ")
            all_text += link(label, url)
            print_text(all_text)
        if formatter == 'header':
            flag = True
            while flag:
                level = int(input("Level: "))
                if 1 < level < 6:
                    flag = False
                    text = input("Text: ")
                    all_text += header(text, level)
                    print_text(all_text)
                else:
                    print("The level should be within the range of 1 to 6")
                    flag = True
        if formatter == 'new-line':
            all_text += new_line()
            print_text(all_text)
        if formatter == "plain":
            text = input("Text: ")
            all_text += plain_text(text)
            print_text(all_text)
        if formatter == 'bold':
            text = input("Text: ")
            all_text += bold_text(text)
            print_text(all_text)
        if formatter == 'italic':
            text = input("Text: ")
            all_text += italic_text(text)
            print_text(all_text)
        if formatter == 'inline-code':
            text = input("Text: ")
            all_text += inline_code(text)
            print_text(all_text)
