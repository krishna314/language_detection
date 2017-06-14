import sys
import nltk
import json
import os
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import defaultdict
from nltk.corpus import udhr
import collections
import re
from sortedcontainers import SortedDict
from collections import OrderedDict
#print(stopwords.fileids())
N_LIMIT=4



def lang_ratio_calculator(sms):
    '''Intial language model which used stopwords to determine the likelihood of langauges in NLTK corpus
       Parameters : sms=single lined or multi lined strings input
       Usage : press enter after entering last text line to execute
       returns a Multi lined string seperated by newline characters'''
    language_ratios={}
    tokens=wordpunct_tokenize(sms)
    print(tokens)
    words=[word.lower() for word in tokens]
    for lang in stopwords.fileids():
        stopwords_set = set(stopwords.words(lang))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        language_ratios[lang] = len(common_elements)
    print(language_ratios)
    max_words_lang = max(language_ratios, key=language_ratios.get)
    print(max_words_lang)
def sms_input():
    '''Used to take multiple lines as input'''
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return text

def find_bigrams(input_list):
    '''
    Used to find all bigrams and return them as a list of tokens
    :param input_list=single line or multi lined string
    :return= all bigrams present in input list:
    '''
    bigram_list = []
    for i in range(len(input_list)-1):
        bigram_list.append((input_list[i], input_list[i+1]))
    return bigram_list

def ngram_calc(word,n):
    '''
    Used to find the nth gram in a word or lines of strings
    :param word:single or multi line string as input
    :param n: the order of the gram that is required
    :return: all the nth grams returend as list of tokens
    '''
    gram=[]
    return [word[i:i+n] for i in range(len(word)-n+1)]




def intial_values(list):
    ''' Creates a dictionary of language file names and their corresponding scores set as 0
    :param list:initial list of languages
    '''
    dict=dict.fromkeys(list,0)


def list_files():
    '''
    Used to list all files in Language directory
    :return: list of files
    '''
    cwd=os.getcwd()
    f=os.path.join(cwd,'Languages')
    list = os.listdir(f)
    return list


def file_read(language):
    '''
    Used to read the file of specified language
    :param language:Name of file whose language is to be read
    :return: gram tokens of that language as a list
    '''
    total=0
    words=[]
    cwd = os.getcwd()
    item_path = os.path.join(cwd,"Languages")
    item = language
    filename = os.path.join(item_path,item)
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            entry = json.load(f)
    except:
        print("Could not open file" + filename)
        quit()
    lang_coff=0
    words_freq={}
    for elem in entry["freq"]:
        words.append(elem)
        words_freq[elem]=entry["freq"][elem]

    #print("lang= "+language+" ")
    #print(words_freq)
    return words_freq

def load_library(language_list):
    '''
    Reads all languages of language_list into a single dictionary with languages and their corresponding grams present as tokens
    :param language_list:List of all languages to be read
    :return: Dictionary of languages and their corresponding grams as tokens
    '''
    d=dict();
    # d = defaultdict(language_list)
    for lang in language_list:
            d[lang]=file_read(lang)
    return d

def print_lang(language_list,lang):
    '''

    :param language_list:
    :param lang:
    :return:
    '''
    d=load_library(language_list)
    print(d[lang])

def intersect(a, b):
    '''
    Used to find common elements between two lists or any other data structures
    :param a: list/data structure passed
    :param b: list/data structure passed
    :return: common elements between the two lists/data structures
    '''
    return list(set(a) & set(b))

def token_prob(list,lang,library):
        '''
        used to calculate the probability associated with list of grams passed for the selected language
        :param list: list of tokens passed that is common with the language selected
        :param lang: the language whose probability is to be calculated
        :param library: Dictionary containing all languages their corresponding grams and frequencies
        :return: Probability of selected language
        '''
        total = 0
        words = []
        for elem in library[lang]:
            total+=library[lang][elem]
        prob = 0
        for token in list:
            if token in library[lang]:
                prob +=((library[lang][token]/total)*10)
        return prob

def results(words):
    '''
     used to return the langauge with highes likelihood
    :param words: list of words
    :return: a string containing the most likely languages
    '''
    merged_gram_list = []
    for word in words:
        for i in range(1, N_LIMIT):
            gram = ngram_calc(word, i)
            merged_gram_list += gram
    lang_prob = {}
    library = load_library(list_files())
    for lang in library:
        i_list = intersect(library[lang], merged_gram_list)
        lang_prob[lang] = token_prob(i_list, lang,library)
        #print("{} {}".format(lang, lang_prob[lang]))

    sorted_lang_prob = [(lang, lang_prob[lang]) for lang in sorted(lang_prob, key=lang_prob.get, reverse=True)]
    #print(sorted_lang_prob)
    k = 0
    lang_full_conv = conversion()
    res=""
    if sorted_lang_prob[0][1]==0:
        res="Unknown Langauge"
    elif sorted_lang_prob[1][1]==0 or sorted_lang_prob[0][1]-sorted_lang_prob[1][1]>0.3:
        res += "Language is most probably {} ({}) ".format(lang_full_conv[sorted_lang_prob[0][0]],sorted_lang_prob[0][0] )
    else:
        for lang_obj in sorted_lang_prob:
            if lang_obj[1] != 0:
                res+="lang {} ({}) and likelihood is {} ".format(lang_full_conv[lang_obj[0]], lang_obj[0], lang_obj[1])
            k += 1
            if (k == 3):
                break

    return res

def main():
        '''
        Used to take a input and predict the language(s) it is likely to be
        :return:
        '''
        sms=input()
        regex = re.compile("[0-9.,?!:;'-=]")
        sms=regex.sub("",sms)
        words=wordpunct_tokenize(sms)
        words=[word.lower() for word in words]
        print(results(words))


def conversion():
    '''
    Used to convert iso code/filename of language to its full form
    :return:Returns the dictionary of filenames/iso codes and their corresponding full forms
    '''
    lang_full_conv={'ar':'Arabic','bg':'Bulgarian','bn':'Bengali','ca':'Catalan','cs':'Czech','dv':'divehi'
        ,'da':'Danish','de':'German','el':'Greek','en':'English','es':'Spanish','et':'Estonian','fa':'Farsi','fi':'Finnish','fr':'French','gu':'Gujrati','he':'Hebrew','hy':'Armenian'
        ,'hi':'Hindi','hr':'Croatian','hu':'Hungarian','id':'Indonesian','it':'Italian','ja':'Japanese','ko':'Korean','lt':'Lithuian','lv':'Latvian','mk':'Macedonian'
        ,'ml':'Malyalam','my':'Burmese','nl':'Dutch','no':'Norwegian','ne':'Nepali','pa':'Punjabi','pl':'Polish','pt':'Portugese','ps':'Pashto','ro':'Romanian','ru':'Russian','si':'Sinhalese','sq':'Albanian',
               'sv':'Swedish','ta':'Tamil','te':'Telgu','th':'Thai','tl':'Tagalog','tr':'Turkish','uk':'Ukranian','ur':'Urdu',
               'vi':'Vietnamese','zh-cn':'Simple Chinese','zh-tw':'Traditional Chinese','jpn2':'Japanese'
               }
    print(len(lang_full_conv))
    return lang_full_conv







main()