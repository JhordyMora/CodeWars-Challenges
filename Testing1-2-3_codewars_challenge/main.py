"""
Description:

Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples:

number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""


def number(lines):
    new_list = []
    counter = 1
    for element in lines:
        new_list.append(element.replace(element, f"{counter}: {element}"))
        counter = counter + 1
    return new_list



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(number(["a", "b", "c"]))

