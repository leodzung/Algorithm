class TrieNode:
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        # Keep track of the index of the word that ends at this node
        self.end = -1
        # Keep track of all suffixes starting from this node
        self.psuffixes = []

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        trie = TrieNode()
        # Build the reversed word trie
        for i, word in enumerate(words):
            word = word[::-1]
            curr = trie
            for j, char in enumerate(word):
                # Check if we are starting a palindrome suffix
                if word[j:] == word[j:][::-1]:
                    # This palindrome suffix belongs to word at index i
                    curr.psuffixes.append(i)
                curr = curr.next[char]
            curr.end = i
            
        ans = []
        # Traverse word trie to find palindrome combination
        for i, word in enumerate(words):
            curr = trie
            for j, char in enumerate(word):
                # If the current node is the end of a word
                if curr.end != -1:
                    # If this suffix is palindrome, we can combine word i and current word ending at j
                    if word[j:] == word[j:][::-1]:
                        ans.append([i, curr.end])
                    
                if char not in curr.next:
                    break
                curr = curr.next[char]
            # If we go through the whole word without a break    
            else: 
                # We don't want to combine a word with itself
                if curr.end != -1 and curr.end != i:
                    ans.append([i, curr.end])
                
                # We can also append any word that has a suffix at this node
                for j in curr.psuffixes:
                    ans.append([i, j])
        return ans
