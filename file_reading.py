import os
import nltk
from nltk import wordpunct_tokenize
import json
import codecs
from collections import OrderedDict
def file_read():
        item_path="C:/Users/IT/Desktop/Langauges/"
        item="bn"
        filename=item_path+item
        try:
                with open(filename,'r',encoding='utf-8') as f:
                        entry=json.load(f)
        except:
                print("Could not open file"+filename)
                quit()
        print(entry)
        for elem in entry["freq"]:
            print(elem)
    #print(entry['freq']['पंच'])

def list_files():
        f=os.listdir("C:/Users/IT/Desktop/Langauges/")
        print(f)

list_files()