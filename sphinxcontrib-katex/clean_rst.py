#!/usr/bin/python
import re
import sys
import os

# Replace method
def replace_all(text, dic):
    for i, j in dic.items():
        if type(i) == str:
            text = text.replace(i, j)
        else:
            text = i.sub(j, text)
    return text


# Dictionary with our find:replace values.
reps = {
    '\\mbox': '\\text',
    '\\nonumber': '',
    '\{align\}': '{aligned}',
    re.compile(r'\{\\cal (.*?)\}'): '\\mathcal{\\1}',
    re.compile(r'\\substack\{(.*)\\\\(.*)\}', re.DOTALL): '\\scriptstyle \\1 \\\\atop\\scriptstyle \\2'
}

directory = os.listdir(os.path.dirname(os.getcwd()))
directory = [d for d in directory if ".rst" in d]

for file in directory:
    f = open(os.path.dirname(os.getcwd())+"/"+file, encoding='utf8')
    filedata = f.read()
    f.close()
    
    replacement = replace_all(filedata, reps)

    f = open(os.path.dirname(os.getcwd())+"/"+file, 'w', encoding='utf8')
    f.write(''.join(replacement))
    f.close()

"""
f = open(os.path.dirname(os.getcwd())+"/"+sys.argv[1], encoding='utf8')
filedata = f.read()
f.close()

step1 = replace_all(filedata, reps)

# Saving the finished product
f = open(os.path.dirname(os.getcwd())+"/"+sys.argv[2], 'w', encoding='utf8')
f.write(''.join(step1))
f.close()
"""