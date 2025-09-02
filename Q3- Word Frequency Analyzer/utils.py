from typing import List, Dict

class Word_Frequency_Analyzer:
    def __init__(self, text: str) -> None:
        self.words: List[str] = text.lower().split()
        self.freq: Dict[str, int] = self.find_count_frequencies()

    def find_count_frequencies(self) -> Dict[str, int]:
        freq = {}
        for word in self.words:
            freq[word] = freq.get(word, 0) + 1
        return freq
    
    def count_frequencies(self) -> Dict[str, int]:
        return self.freq

    def most_frequent_word(self) -> str:
        return max(self.freq, key=self.freq.get)
    
    def find_Word(self, word: str) -> bool:
        return self.check_recursive(self.words, word.lower())
    
    def check_recursive(self, word_list: List[str], target: str) -> bool:
        if not word_list:
            return False
        if word_list[0] == target:
            return True
        return self.check_recursive(word_list[1:], target)
    
    def find_anagrams(self, word: str) -> List[str]:
        word = word.lower()
        sorted_target = sorted(word)
        anagram = []
        for w in set(self.words):
            if w != word and sorted(w) == sorted_target:
                anagram.append(w)
        return anagram
