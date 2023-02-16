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


def ordered_list(rows):
    result = ""
    for i in range(rows):
        row_num = input(f"Row #{i + 1}: ")
        result += f"{i + 1}. {row_num}\n"
    return result


def unordered_list(rows):
    result = ""
    for i in range(rows):
        row_num = input(f"Row #{i + 1}: ")
        result += f"* {row_num}\n"
    return result

all_text = ""
is_done = False
all_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]
while not is_done:
    formatter = input("Choose a formatter: ")
    if formatter == '!done':
        is_done = True
        break
    elif formatter == "!help":
        print("Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list")
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
            #all_text.append(new_line())
            print_text(all_text)
        if formatter == "plain":
            text = input("Text: ")
            all_text += plain_text(text)
            #all_text.append(plain_text(text))
            print_text(all_text)
        if formatter == 'bold':
            text = input("Text: ")
            all_text += bold_text(text)
            #print(bold_text(text))
            #all_text.append(bold_text(text))
            print_text(all_text)
        if formatter == 'italic':
            text = input("Text: ")
            all_text += italic_text(text)
            #all_text.append(italic_text(text))
            print_text(all_text)
        if formatter == 'inline-code':
            text = input("Text: ")
            #all_text.append(inline_code(text))
            all_text += inline_code(text)
            print_text(all_text)
        if formatter == "ordered-list":
            flag = True
            while flag:
                nums = int(input("Number of rows: "))
                if nums > 0:
                    all_text += ordered_list(nums)
                    print(all_text)
                    flag = False
                else:
                    print("The number of rows should be greater than zero")
                    flag = True
        if formatter == "unordered-list":
            flag = True
            while flag:
                nums = int(input("Number of rows: "))
                if nums > 0:
                    all_text += unordered_list(nums)
                    print(all_text)
                    flag = False
                else:
                    print("The number of rows should be greater than zero")
                    flag = True
