class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words =0
        
        for i in sentences:
            max_words = max(max_words, len(i.split()))
        return max_words
