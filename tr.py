import nltk, os
from nltk import ngrams
import string
from snowballstemmer import TurkishStemmer

patentler = os.listdir("./patentler/")
print(patentler)
n=4
for patent in patentler:
    file=open("./patentler/"+patent+"",'r')
    text=file.read()
   
#remove punctuatiıon
    new_text = text.translate(str.maketrans('', '', string.punctuation))

#tokenizing
    words=[]
    words = new_text.split()
#stemming
    stem = TurkishStemmer()
    stemmed = [stem.stemWord(i) for i in words]
    print(stemmed)
#remove stop words
    with open("./turkish_stop_words.txt") as t:
        stop_words = t.read().splitlines()
    clean = [w for w in stemmed if not w in stop_words and not w.isdigit() ]
    while(n>1):
#make ngram
        ngram = list(ngrams(clean, n))      
        file_write=open("./written_tr/write" + str(n) + ".txt",'w+')
        for elem in ngram:
                for word in elem:
                    file_write.write(word)
                    if(word != elem[-1]):
                        file_write.write(" ")
                file_write.write("\n")    
        file_write.close()
        n=n-1
        

with open("./written_tr/write3.txt") as f:
    lines3 = f.read().splitlines()
with open("./written_tr/write2.txt") as f:
    lines2 = f.read().splitlines()
with open("./written_tr/write4.txt") as f:
    lines4 = f.read().splitlines()
print(lines2)

fdist = nltk.FreqDist(lines2)
file=open("./frequency_tr/f2.txt",'w+')
for k,v in fdist.items():
    
    arr=[v,k]
    file.write(str(arr[0]))
    file.write(" ")
    file.write(arr[1])
    file.write("\n")
file.close()
        
fdist = nltk.FreqDist(lines3)
file=open("./frequency_tr/f3.txt",'w+')
for k,v in fdist.items():
    
    arr=[v,k]
    file.write(str(arr[0]))
    file.write(" ")
    file.write(arr[1])
    file.write("\n")    
file.close()
        
fdist = nltk.FreqDist(lines4)
file=open("./frequency_tr/f4.txt",'w+')
for k,v in fdist.items():
        
    arr=[v,k]
    file.write(str(arr[0]))
    file.write(" ")
    file.write(arr[1])
    file.write("\n")
file.close()
