
def main():
    book_path = "books/frankenstein.txt"
    text = book_content(book_path)

    num_words = word_count(text)
    print(f"--- Begin report of {book_path} ---\n")
    print(f"{num_words} words found in the document\n")

    char_dict_count = char_count(text)

    for item in alpha_dict(char_dict_count):
        print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End of {book_path} report ---")

def book_content(book_path):
    with open(book_path) as f:
        return f.read()
    
def word_count(text):
    return len(text.split())

def char_count(text):
    lowered_text = text.lower()
    text_dict = {}
    for char in lowered_text:
        if char not in text_dict:
            text_dict[char] = 1
        else:
            text_dict[char] += 1
    return text_dict
def alpha_dict(char_dict_count):
    dict_list = [{"char": k, "num": v} for k, v in char_dict_count.items()]
    dict_list.sort(key=lambda x: x["num"], reverse=True)
    alpha_list = []
    for char in dict_list:
        if char["char"].isalpha():
            alpha_list.append(char)
    return alpha_list    


main()
