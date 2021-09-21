def multiplication_table(size):
    # Creation of a multiplicator list
    number_list = [element for element in range(1, size+1)]

    # Creation of the product list
    product_list = []
    for index in range(1, size+1):
        for number in number_list:
            product_list.append(index * number)

    # Subdivision of the product list
    final_list = []
    for number in range(0, size):
        final_list.append(product_list[0:size])
        del product_list[0:size]

    return final_list


if __name__ == '__main__':
    print(multiplication_table(6))
