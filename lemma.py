import nltk, os
from nltk import ngrams
from nltk import tokenize
import string
from nltk.corpus import wordnet
from operator import itemgetter

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def add_to_list(list,items):
    i=0
    for k,v in items:
        list[i][0]=int(v)
        list[i][1]=k 
        i+=1
    list=sorted(list, key=itemgetter(0),reverse=True)
    return list    
        
def write_to_file(list,file):
    for a,b in list:
        file.write(str(a))
        file.write(" ")
        file.write(b)
        file.write("\n")
    file.close    
        
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
    
fdist = nltk.FreqDist(lines1)
list1=[[None]*2for i in range(len(fdist))]
file=open("./frequency/f1.txt",'w+')  
list1=add_to_list(list1,fdist.items())
write_to_file(list1,file)
with open("./written/write2.txt") as f:
    lines2 = f.read().splitlines() 
    
fdist = nltk.FreqDist(lines2)
list1=[[None]*2for i in range(len(fdist))]
file=open("./frequency/f2.txt",'w+')  
list1=add_to_list(list1,fdist.items())
write_to_file(list1,file)

with open("./written/write3.txt") as f:
    lines3 = f.read().splitlines() 
    
fdist = nltk.FreqDist(lines3)
list1=[[None]*2for i in range(len(fdist))]
file=open("./frequency/f3.txt",'w+')  
list1=add_to_list(list1,fdist.items())
write_to_file(list1,file)

with open("./written/write4.txt") as f:
    lines4 = f.read().splitlines() 
    
fdist = nltk.FreqDist(lines4)
list1=[[None]*2for i in range(len(fdist))]
file=open("./frequency/f4.txt",'w+')  
list1=add_to_list(list1,fdist.items())
write_to_file(list1,file)









