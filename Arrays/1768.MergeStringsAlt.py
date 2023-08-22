def mergeAlternately(word1: str, word2: str) -> str:
        string = ""
        
        if len(word1) == len(word2):
            for i in range(len(word1)):
                string += word1[i]
                string += word2[i]
            
        elif len(word1) > len(word2):
            word2 += " " *(len(word1) - len(word2))
            for i in range(len(word1)):
                    string += word1[i]
                    string += word2[i]
                  
        else:
            word1 += " " *(len(word2) - len(word1))
            for i in range(len(word1)):
                    string += word1[i]
                    string += word2[i]
        
        string = string.replace(" ", "")
        return string
        
                
print(mergeAlternately("stop", "li"))            
                
