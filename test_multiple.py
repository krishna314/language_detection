import os
import subprocess
import sys

import re

from nltk import wordpunct_tokenize

f=open("language1.txt",'r')
k=0
for line in f:
    sys.stdout = open('result%s.txt' % k , 'w')
    k+=1
    subprocess.check_call(['python3', 'lang_detect.py'+line], \
                          stdout=sys.stdout, stderr=subprocess.STDOUT)


    def results():
        print("hello")

    def main_test(sms):
        '''
        Used to take a input and predict the language(s) it is likely to be
        :return:
        '''
        regex = re.compile("[0-9.,?!:;'-=]")
        sms = regex.sub("", sms)
        # print(sms)
        words = wordpunct_tokenize(sms)
        words = [word.lower() for word in words]
        return results(words)


def check_file(fname):
    fname = 'language1.txt'
    cwd = os.getcwd()
    item_path = os.path.join(cwd, fname)
    f_read = open(item_path, "r")
    f_write = open("Test_Results", "w")
    for line in f_read:
        print(line)
        res = main_test(line)
        fres = line + "  " + res + "\n\n"
        f_write.write(fres)