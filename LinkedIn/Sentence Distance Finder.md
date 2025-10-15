```python
from collections import defaultdict

class SentenceDistanceFinder:
    """
    This class will be given a list of words (such as might be tokenized
    from a paragraph of text), and will provide a method that takes two
    words and returns the shortest distance (in words) between those two
    words in the provided text.
 
    ::
      finder = SentenceDistanceFinder(["the", "quick", "brown", "fox", "quick"])
      assert finder.distance("fox", "the") == 3
      assert finder.distance("quick", "fox") == 1
      assert finder.distance("astro", "fox") = -1
 
    "quick" appears twice in the input. There are two possible distance values for "quick" and "fox":
        (3 - 1) = 2 and (4 - 3) = 1.
 
    Since we have to return the shortest distance between the two words we return 1.
 
    """
    def __init__(self, words):
        # Implementation here
        self.words = words
        self.words_indices = self.get_words_indices(self.words)
    
    def get_words_indices(self, words):
        words_indices = defaultdict(list)
        for index, word in enumerate(words):
            if word in words:
                words_indices[word].append(index)
        return words_indices

    def get_min_distance(self, word1_indices, word2_indices):
        min_distance = float('inf')
        word1_index = 0
        word2_index = 0

        while word1_index < len(word1_indices) and word2_index < len(word2_indices):
            val1 = word1_indices[word1_index]
            val2 = word2_indices[word2_index]

            if abs(val1-val2) < min_distance:
                min_distance = abs(val1-val2)
            
            if val1 < val2:
                word1_index += 1
            else:
                word2_index += 1
            
            word1_index = min(word1_index, len(word1_indices))
            word2_index = min(word2_index, len(word2_indices))
        
        return min_distance
         
    def distance(self, wordOne, wordTwo):
        # Implementation here
        if wordOne not in self.words_indices or wordTwo not in self.words_indices:
            return -1

        word1_indices = self.words_indices[wordOne]
        word2_indices = self.words_indices[wordTwo]

        min_distance = self.get_min_distance(word1_indices, word2_indices)

        return min_distance
```
