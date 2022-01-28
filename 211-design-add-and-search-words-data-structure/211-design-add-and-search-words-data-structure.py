class WordDictionary:

    def __init__(self):
        self.root = dict()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = dict()
            node = node[letter]
        node['is_word'] = True

    def rec_search(self, word, root):
        if len(root) == 0:
            return len(word) == 0
        if len(word) == 0:
            return root.get('is_word', False)

        first_letter = word[0]
        next_word = word[1::]
        if first_letter == '.':
            for letter in root:
                if letter != 'is_word':
                    if self.rec_search(next_word, root[letter]):
                        return True
            return False
        else:
            if first_letter in root:
                return self.rec_search(next_word, root[first_letter])
            else:
                return False

    def search(self, word: str) -> bool:
        x = self.rec_search(word, self.root)
        return x

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)