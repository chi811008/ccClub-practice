class TrieNode:
    def __init__(self):
        self.children = dict() #{"a": TrieNode (p)}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word: #apple
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True
    
    def search(self, word):
        res = ""
        i = 0
        curr = self.root 
        while i < len(word): # application 
            tmp = "" # "apple"
            j = i
            p = -1
            while j < len(word) and word[j] in curr.children:
                if curr.end_of_word == True:
                    p = j
                    print(p)
                tmp += word[j]
                curr = curr.children[word[j]]
                j += 1
            if tmp and curr.end_of_word == True:
                res += "「" + tmp + "」"
                i = j
            elif tmp and (curr.end_of_word == False) and (p != -1):
                res += "「" + tmp[:p - i] + "」"
                i = p
            else:
                res += word[i]
                i += 1
            curr = self.root
        return res

trie = Trie()

for word in input().split():
    trie.insert(word)               

s = input()
while s != "end":
    print(trie.search(s))
    s = input()