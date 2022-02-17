import re


text_infile = open("AI.txt", "r",encoding="utf-8")

text = text_infile.read()

text = re.sub('[.]',"", text)

word_list = list(text.split())

dict={}

for word in word_list:

    if word not in dict:
        dict.update({word:1})
    else:
        dict[word]+=1

print(dict)