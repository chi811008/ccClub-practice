class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True
    
    def search(self, word):
        curr = self.root
        res = ""
        i = 0
        while i < len(word):
            tmp = ""
            j = i
            while j < len(word) and word[j] in curr.children:
                tmp += word[j]
                curr = curr.children[word[j]]
                j += 1
            if tmp and curr.end_of_word == True:
                res += ("「" + tmp + "」")
                i = j
            elif tmp and self.root.children[word[i]].end_of_word == True:
                res += ("「" + word[i] + "」")
                i += 1
            else:
                res += word[i]
                i += 1
            curr = self.root
        return res

words = input().split()
# words = "I have a word Dream".split()
trie = Trie()
for word in words:
    trie.insert(word)

s = input()
while s != "end":
    print(trie.search(s))
    s = input()
# s = "'I Have a Dream' is a public speech that was delivered by American civil rights activist Martin"
# trie.search(s)