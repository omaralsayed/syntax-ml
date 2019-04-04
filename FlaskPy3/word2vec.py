import gensim.downloader as api
import sys

model = api.load("glove-twitter-25")  # download the model and return as object ready for use

def find_top(query, key_list):
# query must be a string
# key list must be a list of strings such as "python for loop"
    min_dist = sys.maxsize; to_return = ""
    for key in key_list:
        key = key.lower().split()
        if "c++" in query and "c++" not in key:
            continue
        if "javascript" in query and "javascript" not in key:
            continue
        if "python" in query and "python" not in key:
            continue
        result = model.wmdistance(query, key)
        print("Analyzing {}: Association: {}".format(key, result))
        if result < min_dist:
            min_dist = result
            to_return = key
    if to_return == "":
        return None
    else:
        return " ".join(to_return)