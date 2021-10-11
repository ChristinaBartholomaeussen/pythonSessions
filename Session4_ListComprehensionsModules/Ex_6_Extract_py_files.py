
# python extract.py . --todir /tmp/ --zip archive.zip
import os
import sys
import subprocess
from zipfile import ZipFile

def main(argv):
    x = os.listdir(argv[1])
    
    pylist = [i for i in x if i[-3:] == '.py']
    
    os.mkdir(argv[3])

    for i in pylist:
        subprocess.run(['cp', i, argv[3]])

    with ZipFile(argv[3]+'/archive.zip', 'w') as zf:
        for file in pylist:
            zf.write(file)


main(sys.argv)


