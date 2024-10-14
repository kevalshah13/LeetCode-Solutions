class TrieNode:
    def __init__(self):
        self.children={}
        self.End=False

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()  # Create a new node only if it doesn't exist
            curr = curr.children[c]  # Move to the next node
        curr.End = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        curr=self.root

        for c in word:
            if(c not in curr.children):
                return False
            curr=curr.children[c]
        return curr.End

    def startsWith(self, prefix: str) -> bool:
        curr=self.root

        for c in prefix:
            if(c not in curr.children):
                return False
            curr=curr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)