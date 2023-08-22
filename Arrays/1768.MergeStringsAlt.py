def mergeAlternately(word1: str, word2: str) -> str:
        if len(word1) == len(word2):
            for i in range(len(word1)):
                print(word1[i], end="")
                print(word2[i], end="")
        elif len(word1) > len(word2):
            word2 += " " *(len(word1) - len(word2))
            for i in range(len(word1)):
                    print(word1[i], end="")
                    print(word2[i], end="")
        else:
            word1 += " " *(len(word2) - len(word1))
            for i in range(len(word1)):
                    print(word1[i], end="")
                    print(word2[i], end="")
                
mergeAlternately("stop", "lift")                
                
