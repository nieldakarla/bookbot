
def main():
    book_path = "books/frankenstein.txt"
    text = book_content(book_path)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")

    char_dict_count = char_count(text)
    print(char_dict_count)
    
def book_content(book_path):
    with open(book_path) as f:
        return f.read()
    
def word_count(text):
    word_list = text.split()
    return len(word_list)

def char_count(text):
    lowered_text = text.lower()
    text_dict = {}
    for char in lowered_text:
        if char not in text_dict:
            text_dict[char] = 1
        else:
            text_dict[char] += 1
    return text_dict

main()