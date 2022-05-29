def convert_base_10_to_base_2(value):
    binary_repr = ''
    result = value

    while result != 0:
        binary_repr = str(result % 2) + binary_repr
        result = result // 2

    return binary_repr


if __name__ == '__main__':
    print(convert_base_10_to_base_2(16))
