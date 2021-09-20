"""
Description:
Kevin is noticing his space run out! Write a function that removes the spaces from the values
and returns an array showing the space decreasing. For example, running this function on the array
['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace'].
"""

def spacey(array):
    new_list = []
    string = ""
    for element in array:
        string = string + element
        new_list.append(string)
    return new_list


if __name__ == '__main__':
    spacey(['kevin', 'has', 'no', 'space'])
    spacey(['this', 'cheese', 'has', 'no', 'holes'])
