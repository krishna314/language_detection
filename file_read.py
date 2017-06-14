import nltk
import os
from nltk import wordpunct_tokenize
def file_read():
    script_dir=os.path.dirname(__file__)
    print(script_dir)
    rel_path="Langauges/"
    abs_file_path=os.path.join(script_dir,rel_path)
    cwd=os.getcwd()
    item="hi"
    #filename=os.path.join(abs_file_path,item)
    item_path=os.path.join('Languages',item)
    filename=os.path.join(cwd,item_path)
    print(filename)
    try:
        file=open(filename,encoding="utf-8")
    except:
        print("Could not open file "+filename)
        quit()
    for line in file:
        str=repr(line)
       #print(str)
        word_list=wordpunct_tokenize(str)
        print(word_list)
        #print(str[2:10])

file_read()
