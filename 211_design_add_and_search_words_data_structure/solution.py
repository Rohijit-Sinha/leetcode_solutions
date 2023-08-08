class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str, node:TrieNode = None) -> bool:
        def dfs(j, root:TrieNode):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for node in cur.children.values():
                        if dfs(i+1, node):
                            return True
                    return False
                else:
                    if c in cur.children:
                        cur = cur.children[c]
                    else:
                        return False
            return cur.endOfWord
        return dfs(0,self.root)