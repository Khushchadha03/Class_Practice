from utils import Word_Frequency_Analyzer

Line = "The Cat and the bat ran fast and the cat danced"
Analyzer = Word_Frequency_Analyzer(Line)

print("Frequencies:", Analyzer.count_frequencies())
print("Most Frequent Word:", Analyzer.most_frequent_word())
print("Find 'cat':", Analyzer.find_Word("cat"))
print("Anagrams of 'cat':", Analyzer.find_anagrams("cat"))
