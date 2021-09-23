# def duplicate_encode(word: str) -> str:
#     """ This function counts how many times each letter repeats and change it with ")" if it is more
#     then one in the word. """
#     word = word.lower()
#     list_word = [letter for letter in word]
#     dict_repetition = {}
#     dict_repetition_parentheses = {}
#     index_ = [i for i, x in enumerate(list_word) if x == "("]
#     index__ = [i for i, x in enumerate(list_word) if x == ")"]
#     if "(" in list_word:
#         letter_counter = list_word.count("(")
#         dict_repetition_parentheses["("] = letter_counter
#     if ")" in list_word:
#         letter_counter = list_word.count(")")
#         dict_repetition_parentheses[")"] = letter_counter
#     for letter in word:
#         if letter == "(" or letter == ")":
#             pass
#         letter_counter = list_word.count(letter)
#         dict_repetition[letter] = letter_counter
#
#     for key in dict_repetition.keys():
#         if dict_repetition[key] == 1:
#             word = word.replace(key, "(")
#         else:
#             word = word.replace(key, ")")
#
#     list_word_2 = [letter for letter in word]
#     for element in index_:
#         list_word_2[element] = "("
#
#     for element in index__:
#         list_word_2[element] = ")"
#
#     return "".join(list_word_2)

from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)

if __name__ == '__main__':
    # print(duplicate_encode("din"))
    # # "((("
    # print(duplicate_encode("recede"))
    # # "()()()"
    # print(duplicate_encode("Success"))
    # # ")())())", "should ignore case"
    # print(duplicate_encode("(( @"))
    # #  "))(("
    # print(duplicate_encode("PsKsgB)MdQnr( Lbkrh!yRB!Q"))
    # #  "()))()((()()((()))()())))"
    # print(duplicate_encode("PsKsgB)MdQnr( Lbkrh!yRB!Q"))
    # #  "()))()((()()((()))()())))"
    print(duplicate_encode("()W(KnfU"))
    #  ")(()(((("
