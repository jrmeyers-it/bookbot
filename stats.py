def total_word_count(book):
    words = book.split()
    word_count = len(words)
    return f"{word_count} words found in the document"

def count_letters(book):
    lowercase_book = book.lower()
    letter_count = {}
    for char in lowercase_book:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1
    return letter_count

def sort_on_num(dict):
    return dict["num"]

def report_book_letter_count(book):
    letter_count_list = []
    lowercase_book = book.lower()
    for char in lowercase_book:
        if (char.isalpha()):
            if (len(letter_count_list) == 0):
                letter_count_list.append({"char": char, "num": 1})
            else:
                index_found = -1
                for i in range(0, len(letter_count_list), 1):
                    if (char == letter_count_list[i]["char"]):
                        index_found = i
                        break
                if (index_found == -1):
                    letter_count_list.append({"char": char, "num": 1})
                else:
                    letter_count_list[index_found]["num"] += 1
    letter_count_list.sort(reverse=True, key=sort_on_num)
    
    return letter_count_list
