class Trie:
    def __init__(self):
        self.root = Node(None)

    def query_dfs(self, current, prefix, result):
        if not current:
            return

        if current.is_last:
            result.append(prefix + current.value)

        for node in current.children.values():
            self.query_dfs(node, prefix + current.value, result)

    def query(self, prefix):
        current = self.root

        for character in prefix:
            if character not in current.children:
                return []
            current = current.children[character]

        result = []
        self.query_dfs(current, prefix[:-1], result)
        return result

    def add(self, word):
        current = self.root

        for i, character in enumerate(word):

            if character not in current.children:
                current.children[character] = Node(character)

            current = current.children[character]

        current.is_last = True


class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_last = False


def main():
    trie = Trie()
    trie.add('hello')
    trie.add('hell')
    trie.add('hey')
    trie.add('hey there!')
    result = trie.query('he')
    print(result)

    trie = Trie()
    trie.add('630-799-8765')
    trie.add('630-234-2375')
    trie.add('630-543-0927')
    trie.add('630-843-0174')
    result = trie.query('630')
    print(result)


if __name__ == '__main__':
    main()
