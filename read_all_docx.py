"""
oct 8 2020
to read all docx file in directory
split with '။'

write for Kawi Article content
usage: python3 read_all_docx.py file_path > all_text_output

"""
import sys	#to get argv from user
import glob	#to read all file name from the directory
import docx	#to read docx file with python
import re	#to processing with patten

path = sys.argv[0]

files = glob.glob(path+"/*.docx")

for f in files:
    print("\n\nfile name => "+f+"\n\n")
    doc = docx.Document(f)
    result = [p.text for p in doc.paragraphs]
    line = ''.join(result)
    line = re.sub(r'\n',r' ',line)
    line = re.sub(r'(။)',r'\1\n',line)
    print(line)

