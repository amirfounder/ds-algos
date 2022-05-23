def get_all_perms(lst):
    if len(lst) == 0:
        return [[]]
    
    first_element = lst[0]
    elements_without_first = lst[1:]

    perms_without_first = get_all_perms(elements_without_first)
    all_perms = []

    for perm_without_first in perms_without_first:
        for position in range(len(perm_without_first) + 1):
            permutation_with_first = perm_without_first[0:position] + [first_element] + perm_without_first[position:]
            all_perms.append(permutation_with_first)

    return all_perms


def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remaining_list is
        # remaining list
        remaining_list = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remaining_list):
            l.append([m] + p)
    return l


if __name__ == '__main__':
    for perm in get_all_perms(list('abcd')):
        print(perm)
