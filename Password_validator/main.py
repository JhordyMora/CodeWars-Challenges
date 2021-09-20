def password(string: str) -> bool:
    uppercase_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                      "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]
    lowercase_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                      "q", "r", "s", "t", "u", "w", "x", "y", "z"]
    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    separate_string = [letter for letter in string]
    if len(separate_string) <= 7:
        return False

    counter_uppercase_list = 0
    counter_lowercase_list = 0
    counter_number_list = 0

    for element in uppercase_list:
        if element in string:
            counter_uppercase_list = counter_uppercase_list + 1

    for element in lowercase_list:
        if element in string:
            counter_lowercase_list = counter_lowercase_list + 1

    for element in number_list:
        if element in string:
            counter_number_list = counter_number_list + 1

    if counter_uppercase_list != 0 and counter_lowercase_list != 0 and counter_number_list != 0:
        return True
    return False


if __name__ == '__main__':
    print(password("Abcd1234"))
    # True
    print(password("Abcd123"))
    # False
    print(password("abcd1234"))
    # False
    print(password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"))
    # True
    print(password("ABCD1234"))
    # False
    print(password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"))
    # True
    print(password("!@#$%^&*()-_+={}[]|\:;?/>.<,"))
    # False
    print(password(" aA1----"))
    # True
    print(password(""))
    # False
    print(password("4aA1----"))
    # True

