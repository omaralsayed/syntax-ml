'''
The main function here is classify(filename, verbose=True)
It takes a filename as an argument, using the relative path,
and returns a string from the options dict.
Currently it can either classify a file as python, c++, or javascript.
This is regardless of the filename that the user has established.
'''

import re

def word_freqs(text):
    unique_words = []; unique_words_ws = []; 
    SS = "<SPLIT|HERE>"
    text = text.replace("    ",SS).replace(" ",SS).replace("\n",SS).replace("\t",SS).replace(SS+SS,SS)
    text = text.split("<SPLIT|HERE>")
    fin_text = [t for t in text if t != ""]
    total_word_count = len(fin_text)
    for word in fin_text:
        if word not in unique_words_ws:
            unique_words.append([word, 1])
            unique_words_ws.append(word)
        else:
            idx = unique_words_ws.index(word)
            unique_words[idx][1] += 1
            if unique_words[idx][1] > 12000:
                escape = True
    for i in range(len(unique_words)):
        unique_words[i][1] /= total_word_count
    unique_words.sort(key=lambda x: x[1], reverse=True)
    return unique_words

def compare(master, txt_file, verbose=False):
    loss = 0

    # generate master array
    master = open(master, "r").read()
    master = master[1:-1]
    master = re.findall('''\['(.+?)\]''',master)
    master_unique_words = []
    for portion in master:
        while len(portion) != 0 and portion[0] == '''\"''':
            portion = portion[1:]
        while len(portion) != 0 and portion[:-1] == '''\"''':
            portion = portion[0:-1]
        portion = portion.split('''', ''')
        if len(portion) == 2:
            master_unique_words.append([portion[0], float(portion[1])])

    
    # generate compare array
    compare_unique_words = word_freqs(open(txt_file, "r").read())
    master_words = []
    for m_word in master_unique_words:
        master_words.append(m_word[0])

    if len(compare_unique_words) > 100:
        compare_unique_words = compare_unique_words[0:100]
    for c_word in compare_unique_words:
        if c_word[0] in master_words:
            resid = abs(c_word[1] - master_unique_words[master_words.index(c_word[0])][1])
            resid = resid ** 2
            loss += resid
            if verbose:
                print("found: {}".format(resid))
        else:
            resid = abs(c_word[1])
            resid = resid ** 2
            loss += resid * 2
            if verbose:
                print("not found: {}".format(resid))
    if verbose:
        print("Final Loss: {}".format(loss))
    return loss

def classify(filename, verbose=False):
    filename = "data_sort.py"

    options = {"data/py_data.txt":"python", "data/js_data.txt":"javascript", "data/cc_data.txt":"c++"}

    language = options[next(iter(options))]
    import sys
    loss = sys.maxsize

    for option in options.keys():
        this_loss = compare(option, filename)
        if verbose:
            print(this_loss)
        if this_loss < loss:
            language = options[option]
            loss = this_loss
    if verbose:
        print(language)
    return language