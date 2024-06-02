def find_max(wordlist):
    x = 1

def generate_wordcloud(wordlist):
    huge = 1




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

for key in list(wordlist.keys()): 
    print(key, ":", wordlist[key])




