class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.root = self

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = WordDictionary()
            
            current = current.children[char]
        current.end_of_word = True


    
class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.root = self

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = WordDictionary()

            current = current.children[char]

        current.end_of_word = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.end_of_word

            char = word[i]

            if char == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            if char not in node.children:
                return False

            return dfs(node.children[char], i + 1)

        return dfs(self.root, 0)

