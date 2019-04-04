import os
import sys
import codecs
# python data_sort.py data/python py
walk_dir = sys.argv[1]

repo = os.path.abspath(sys.argv[1])
extensions = []
for arg in sys.argv[2:]:
    extensions += [str(arg)]
id = 0

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)

    for subdir in subdirs:
        print('\t- subdirectory ' + subdir)

    for filename in files:
        file_path = os.path.join(root, filename)
        if file_path[-2:] in extensions:
            print(file_path)
        # print('\t- file %s (full path: %s)' % (filename, file_path))

            with open(file_path, 'r', encoding="latin-1") as f:
                f_content = f.read()
            w = open(str(repo) + "\{}.{}".format(str(id), file_path[-2:]), "w+", encoding="latin-1")
            w.write(str(f_content))
            w.close()
            id += 1