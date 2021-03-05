import os
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
import re
file = open('unique_terms.txt','w')
n = 0
numerToken = 0
hashI = {}
for path, dirs, files in os.walk('/Users/ramvyas/Desktop/IS-392/Assignment-2_RamVyas/1'):
    for f in files:
        filename = os.path.join(path, f)
        n +=1
        
        with open(filename, 'r' , encoding='utf-8', errors='ignore') as myF:
            #print(myF.read())
            soup = BeautifulSoup(myF,'html.parser')
            
            text = soup.get_text()
            text = text.lower()
            text = re.sub("\[.*\]", " ", text)
            text = re.sub("[!\"#$%&'()*+\,-.·\–\--/:;<\=>?@[\]^`{|}~]", " ", text)
            text = text.replace("\\",' ')
            
            
            
            tokens = nltk.word_tokenize(text)
            p = 0
            
            
            
            for token in tokens:
                if token not in hashI:
                    hashI[token] = []
                    numerToken += 1
                    file.write(str(numerToken)+') '+token+'  ' + ' ==> Document number: '+ str(n))
                    file.write('\n')
                    
                else:
                    hashI[token].append((str(n),str(p)))
                p +=1 
file.close()
f = open('index.txt','w',encoding = 'utf-8')
#print(hashI)
for term in hashI:
    f.write(term + ' => ')
    for posting in hashI[term]:
        doc_id = str(posting[0])
        freq = str(posting[1])
        f.write('('+doc_id+', '+freq+')')
    f.write('\n')
f.close()
    
