class TrieNode:

    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.isWord = False
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.res = []

    def addWord(self, word: str) -> None:
        node: TrieNode = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.isWord = True

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for i in folder:
            x = list(i.split("/"))
            self.addWord(x)

        self._dfs(self.root, "")
        return self.res
    def _dfs(self, node, letters):
        if node.isWord:
            self.res.append(letters[1:])
            return
        for letter, child in node.children.items():
            self._dfs(child, letters+"/"+letter)
