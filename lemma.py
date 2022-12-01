import nltk, os
from nltk import ngrams
import string
from nltk.corpus import wordnet

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

patents = os.listdir("./patents/")
print(patents)
for patent in patents:
    print(patent)
    file=open("./patents/"+patent,'r')
    text=file.read()
    n=4
#remove punctuatiıon
    new_text = text.translate(str.maketrans('', '', string.punctuation))

#tokenizing
    words=[]
    words = new_text.split()
#get rid of capital letters
    for i in range (len(words)):
        if words[i].isupper:
            words[i]=words[i].lower()
            
#stemming
    lemmatizer = nltk.WordNetLemmatizer()
    lem=[lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in words]
#remove stop words
    with open("./eng_stop_words.txt") as t:
        stop_words = t.read().splitlines()
    clean = [w for w in lem if not w in stop_words and not w.isdigit() ]
    


    while(n>1):
#make ngram
        ngram = list(ngrams(clean, n))      
        file_write=open("./written/write" + str(n) + ".txt",'a+')
        for elem in ngram:
                for word in elem:
                    file_write.write(word)
                    if(word != elem[-1]):
                        file_write.write(" ")
                file_write.write("\n")    
        file_write.close()
        n=n-1
    file_write=open("./written/write1.txt",'a+')    
    for word in clean:
        file_write.write(word)
        file_write.write("\n")
    file_write.close()    
    
with open("./written/write1.txt") as f:
    lines1 = f.read().splitlines()    
with open("./written/write3.txt") as f:
    lines3 = f.read().splitlines()
with open("./written/write2.txt") as f:
    lines2 = f.read().splitlines()
with open("./written/write4.txt") as f:
    lines4 = f.read().splitlines()


fdist = nltk.FreqDist(lines1)
file=open("./frequency/f1.txt",'w+')
for k,v in fdist.items():
    
    file.write(str(v))
    file.write(" ")
    file.write(k)
    file.write("\n")

file.close()
fdist = nltk.FreqDist(lines2)
file=open("./frequency/f2.txt",'w+')
i=0
list2=[[None]*2for i in range(len(fdist))]
for k,v in fdist.items():
    
    list2[i][0]=v
    list2[i][1]=k
    
    
    file.write(str(v))
    file.write(" ")
    file.write(k)
    file.write("\n")
    i+=1
    
file.close()
print(list2)
fdist = nltk.FreqDist(lines3)
file=open("./frequency/f3.txt",'w+')
for k,v in fdist.items():
    
     file.write(str(v))
     file.write(" ")
     file.write(k)
     file.write("\n")    
file.close()
        
fdist = nltk.FreqDist(lines4)
file=open("./frequency/f4.txt",'w+')
for k,v in fdist.items():
        
     file.write(str(v))
     file.write(" ")
     file.write(k)
     file.write("\n")
file.close()
