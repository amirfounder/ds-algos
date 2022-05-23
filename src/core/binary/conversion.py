from string import ascii_lowercase as alphabet


def convert_base_10_to_base_2(value):
    binary_repr = ''
    result = value

    while result != 0:
        binary_repr = str(result % 2) + binary_repr
        result = result // 2

    return binary_repr


def solution(s):
    char_map = {_s: i for i, _s in enumerate(alphabet)}
    result = []

    for char in s:
        if char == ' ':
            result.append('000000')
            continue

        is_upper = char not in char_map
        char = char.lower()

        base_10_repr = char_map.get(char)
        base_2_repr = convert_base_10_to_base_2(base_10_repr)
        base_2_repr = base_2_repr.ljust(5, '0')
        base_2_repr = ('1' if is_upper else '0') + base_2_repr

        result.append(base_2_repr)

    return ' '.join(result)


if __name__ == '__main__':
    print(solution('hello'))