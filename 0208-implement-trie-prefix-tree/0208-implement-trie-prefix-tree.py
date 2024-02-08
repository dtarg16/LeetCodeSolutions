class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        tmp = self.root

        for ch in word:
            if ch not in tmp.children:
                tmp.children[ch] = TrieNode()
            tmp = tmp.children[ch]

        tmp.is_end = True

        
    def search(self, word: str) -> bool:
        tmp = self.root
        
        for ch in word:
            if ch not in tmp.children:
                return False
            tmp = tmp.children[ch]

        return tmp.is_end
        

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root

        for ch in prefix:
            if ch not in tmp.children:
                return False
            tmp = tmp.children[ch]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)