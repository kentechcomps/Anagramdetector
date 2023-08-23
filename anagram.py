class Anagram:
    def __init__(self , word):
        self.word = word

    def match(self , anagram_list):
        matches = []    
        sortedw = sorted(self.word)

        for anagramitem in anagram_list:
            anagramitem_lower = anagramitem.lower()  # Convert anagramitem to lowercase for case-insensitive matching
            if anagramitem_lower != self.word and sorted(anagramitem_lower) == sortedw:
                matches.append(anagramitem)
        
        return matches
    

anagrammeth = Anagram("listen")
anagrammeth.match(['enlists', 'google', 'inlets', 'banana'])
