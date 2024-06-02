import operator
import os

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


path = './files/'
dir_list = os.listdir(path)
wordlist = dict() 

if len(dir_list) < 5:
    print('Less than 5 files. exiting.')
    quit()

for file_name in dir_list:
    text = open("files/" + file_name, "r") 

    for line in text: 
        line = line.strip() 
        line = line.lower() 
        word = line.strip()

        if word in wordlist:
            wordlist[word] = wordlist[word] + 1
        else: 
            wordlist[word] = 1

wordcloud = generate_wordcloud(wordlist)
sorted_wordlist = dict(sorted(wordlist.items(), key=lambda item: item[1], reverse=True))

file_ptr = open("output.txt", "w")

for key in list(wordcloud.keys()): 
    print(key, " : ", wordlist[key] , " : ", wordcloud[key])
    file_ptr.write(key + "\t" + str(wordlist[key]) + "\t" + wordcloud[key] + "\n")

file_ptr.close()



