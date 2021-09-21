def duplicate_count(text: str) -> int:
    """This function counts how many repeated letter (lower and uppercase) or numbers are in a string"""

    # Creation of a comparison list with all letters and numbers and list with element of the text
    alphanumeric_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                         "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    text_list = [letter.upper() for letter in text]

    # Dictionary and counting of every repeated element in the text
    dict_letters = {}
    for element in alphanumeric_list:
        amount_letter = text_list.count(element)
        if amount_letter > 1:
            dict_letters[element] = amount_letter
    return len(dict_letters)


if __name__ == '__main__':
    print(duplicate_count(""))
    # 0
    print(duplicate_count("abcde"))
    # 0
    print(duplicate_count("abcdeaa"))
    # 1
    print(duplicate_count("abcdeaB"))
    # 2
    print(duplicate_count("Indivisibilities"))
    # 2
    print(duplicate_count("mldLOOdx1LPRcRkD9Fs5S1c6hd5AY5dyEPZnLrOtclx65h5aczTItARPOXAkUFTPLuLUln"))
    # 20
