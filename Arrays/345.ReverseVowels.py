def reverseVowels(string:str) -> str:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    string = list(string)
    values = []
    indexes = []

    for index, value in enumerate(string):
        if value in vowels:
            indexes.append(index)
            values.append(value)
    values = values[::-1]
    
    for i in range(len(indexes)):
        string[indexes[i]] = values[i]
        
    return "".join(string)
