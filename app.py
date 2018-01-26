import pickle
from optparse import OptionParser
from prettytable import PrettyTable
from functools import reduce




def app(filename):
    with open(filename, 'rb') as src:
        matrix = pickle.load(src)
        print('[*] Load and build table from src')

    table = PrettyTable()

    for row in matrix:
        table.add_row(row)
    print(table)

    table_result = PrettyTable()
    results = ['Result']
    for col in zip(*matrix):
        results.append(reduce(lambda a, x: a * x, col))
    table_result.add_row(results)
    print(table_result)


    







if __name__ == '__main__':
    parse = OptionParser("""

        ./app.py [options]
     
    options:
     
    -f, --file    [::] File to read pickle src

        """)
  
    parse.add_option('-f','--file',dest='F',type='string', help='File to read')

    (opt,args) = parse.parse_args()
    if opt.F == None:
        print(parse.usage)
        exit(0)
    else:
        try:
            app(opt.F)
        except Exception as err:
            print('[-] {}'.format(err))