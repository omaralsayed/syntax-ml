import os

def top_10000_words(file_loc, extension):
    # gets the top 10000 words from all the files in a given location
    path = os.getcwd()
    path = os.path.join(path, file_loc)
    print(path)
    temp_f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        temp_f.extend(filenames)
    f = []
    for f_name in temp_f:
        if f_name[f_name.index('.')+1:] == extension:
            f.append(f_name)
    # FILES HAVE BEEN ACCESSED
    unique_words = []; unique_words_ws = []; escape = False; total_word_count = 0
    total_word_count = 0
    for read_f in f:
        if len(unique_words) > 50000:
            break
        try:
            text = open(os.path.join(path, read_f), "r").read()
        except UnicodeDecodeError:
            continue
        # remove comments
        SS = "<SPLIT|HERE>"
        text = text.replace("    ",SS).replace(" ",SS).replace("\n",SS).replace("\t",SS).replace(SS+SS,SS)
        text = text.split("<SPLIT|HERE>")
        fin_text = [t for t in text if t != ""]
        total_word_count += len(fin_text)
        for word in fin_text:
            if word not in unique_words_ws:
                unique_words.append([word, 1])
                unique_words_ws.append(word)
            else:
                idx = unique_words_ws.index(word)
                unique_words[idx][1] += 1
                if unique_words[idx][1] > 12000:
                    escape = True
        if escape:
            break
        print("File {}: {}".format(read_f, len(unique_words)))
    unique_words.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(unique_words)):
        unique_words[i][1] /= total_word_count
    store = open("{}_data.txt".format(extension), "w+")
    store.write(str(unique_words))



def view_data():
    imdb = keras.datasets.imdb
    (train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
    for i in range(0,5):
        print(len(train_data[i]))

top_10000_words("data/python", "py")
top_10000_words("data/cpp", "cc")
top_10000_words("data/js", "js")