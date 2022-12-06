import nltk, os
from functions import *


file_write=[] 
patents = os.listdir("./patents/")
print(patents)
for patentid in range(len(patents)):
    patent=patents[patentid]
    print(patent)
    file=open("./patents/"+patent,'r')
    text=file.read()
    n=4
    
    split_text=split_to_sentences(text)
    #print(split_text)
    
    for textid in range(len(split_text)):
        
        text=split_text[textid]

        text=remove_punctuation(text)
        
        words= split_to_words(text)
        
        words[0]=words[0].lower()

        words=simplifying_words(words)
        
        words=remove_stop_words(words)
        
        make_n_grams(words,n,patents,patentid)
        
        
files=os.listdir("./written/")
for file in files:
    with open("./written/"+file) as f:
        lines = f.read().splitlines() 
        fdist = nltk.FreqDist(lines[0:])
        arr=[[None]*2for i in range(len(fdist))]
        arr=add_to_list(arr,fdist.items())
        file=open("./frequency/"+file,'w+')
        write_to_file(arr,file)
        

