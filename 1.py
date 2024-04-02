import re
def decrypt_clue(text):

    pattern = r'\b(?:list|int|def|class|return|try|except|for|from|import|global|if|else|lambda|nonlocal|pass|raise|while|with|and|or|assert|break|continue|finally)\b'

    keywords = re.findall(pattern, text)

    print("kalamat kelidy dar Phyton:")
    for keyword in keywords:
        print(keyword)

file = open("1.txt", "r")
text = file.read()

decrypt_clue(text)
