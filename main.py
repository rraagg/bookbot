def main():
    file_path = 'books/frankenstein.txt'
    text = open_file(file_path)
    if text:
        print(f'--- Begin report of {file_path} ---')
        print(f'The file {file_path} has {count_words(text)} words')
        print_report(count_characters(text))


def count_words(text):
    return len(text.split())


def count_characters(text):
    characters = {}
    for c in text:
        if c.lower() in characters:
            characters[c.lower()] = characters[c.lower()] + 1
        else:
            characters[c.lower()] = 1
    return characters


def sort_on(dict):
    return dict["count"]


def print_report(characters_dict):
    characters_list = []
    for key, value in characters_dict.items():
        new_dict = {
            "character": key,
            "count": value
        }
        characters_list.append(new_dict)
    characters_list.sort(reverse=True, key=sort_on)
    for c in characters_list:
        if c["character"].isalpha():
            print(f"The '{c["character"]}' was found '{c["count"]}' times")
    print("--- End report ---")


def open_file(file_name):
    try:
        with open(file_name) as f:
            return f.read()
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    main()