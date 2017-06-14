import re
from nltk import wordpunct_tokenize
import json
def ngram_calc(word,n):
    gram=[]
    return [word[i:i+n] for i in range(len(word)-n+1)]

def get_grams(filename):
    f=open(filename,'r')
    v = open(filename, 'r')
    s_file=f.readlines()
    #print(len(s_file))
    s_file=v.read().replace('\n','')
    gram_dict = {}
    words = wordpunct_tokenize(s_file)
    print(len(words))
    print(words)
    print(s_file)
    for i in range(1,4):
        tokens = ngram_calc(s_file, i)
        for token in tokens:
            if token not in gram_dict:
                gram_dict[token]=len(re.findall(token,s_file))

    print(gram_dict)
    total=0
    for key in gram_dict:
        total+=gram_dict[key]
    print(total)
    c_gram_dict={}
    c_gram_dict["freq"]=gram_dict
    print(c_gram_dict)
    put_into_json(c_gram_dict,"result_"+filename[0:2])

def put_into_json(data,fname):
    f=open(fname,'w')
    json.dump(data,f,ensure_ascii=False)
    '''for word in words:
        tokens=ngram_calc(word,1)
        for token in tokens:
            if token not in gram_dict:
                print(token)
                num=len(re.findall(token,s_file))
                gram_dict[token]=num'''





get_grams("Armenian_data")