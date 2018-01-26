import random
import pickle
from prettytable import PrettyTable
from optparse import OptionParser
import sys



def generate(rows, cols, filename):
    matrix = [[random.choice(range(100)) for i in range(cols)]for i in range(rows)]

    print('[*] Generating...')

    pickle.dumps(matrix)


    print('[*] Dump object into binary data and saving into src.pickle...')
    with open(filename, 'wb') as src:
        pickle.dump(matrix, src)
        print('[+] Saved')

    with open(filename, 'rb') as src:
        matrix = pickle.load(src)
        print('[*] Load and build table from src')

    table = PrettyTable()
    for row in matrix:
        table.add_row(row)

    print(table)
    print('[+] Ready')


if __name__ == '__main__':
    parse = OptionParser("""

        ./generate.py [options]
     
    options:
     
    -r, --rows    [::] Rows of matrix
    -c, --cols    [::] Cols of matrix
    -f, --file    [::] File to save


        """)
    parse.add_option('-r','--rows',dest='R',type='string',help='Rows of matrix')          
    parse.add_option('-c','--cols',dest='C',type='string',help='Cols of matrix')
    parse.add_option('-f','--file',dest='F',type='string', help='File to save')

    (opt,args) = parse.parse_args()
    if opt.R == None or opt.C == None or opt.F == None:
        print(parse.usage)
        exit(0)
    else:
        try:
            generate(int(opt.R), int(opt.C), opt.F)
        except Exception as err:
            print('[-] {}'.format(err))

