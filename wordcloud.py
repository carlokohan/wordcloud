import operator

def generate_wordcloud(wordlist):
    wordcloud = {}
    huge_word = max(wordlist, key=wordlist.get)
    wordcloud[huge_word] = 'Huge'
    huge_count = wordlist[huge_word]

    for key in list(wordlist.keys()): 
        if wordlist[key] >= (0.6 * huge_count):
            wordcloud[key] = 'Big'
        elif wordlist[key] >= (0.3 * huge_count):
            wordcloud[key] = 'Normal'
        elif wordlist[key] > 1:
            wordcloud[key] = 'Small'

    return wordcloud

text = open("files/words.txt", "r") 

wordlist = dict() 

for line in text: 
    line = line.strip() 
    line = line.lower() 
    word = line.strip()

    if word in wordlist:
        wordlist[word] = wordlist[word] + 1
    else: 
        wordlist[word] = 1

wordcloud = generate_wordcloud(wordlist)
for key in list(wordcloud.keys()): 
    print(key, ":", wordcloud[key])




