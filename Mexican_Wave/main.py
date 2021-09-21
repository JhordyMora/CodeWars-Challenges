# def wave(word):
#     empty_list = []
#     for index in range(len(word)):
#         new_word = word.replace(word[index], word[index].upper())
#         empty_list.append(new_word)
#     return empty_list

# def wave(word):
#     return [word.replace(word[index], word[index].upper(), 1) for index in range(len(word))]

def wave(word: str) -> list:
    letter_list = [letter for letter in word]
    letter_list2 = letter_list.copy()
    new_list = []
    for index in range(len(letter_list)):
        if letter_list[index] == " ":
            continue
        nueva_letra = letter_list[index].upper()
        letter_list2[index] = nueva_letra
        new_list.append("".join(letter_list2))
        letter_list2 = letter_list.copy()
    return new_list


if __name__ == '__main__':
    print(wave(' gap'))
