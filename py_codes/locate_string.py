import os
import sys

'''
5 minutes to create this script
this script is using to find a file with a string.
is lique  "| grep" :)
'''

def lista_dir(diretorio):          
    lista = []
    for filename in os.listdir(diretorio):
        lista.append(str(filename))
    return lista


def filter_in_file(file_name, string_to_match):
    f = open(file_name, 'r')
    i = f.readline()
    line = 1
    count_strikes = 0
    while i:
        if string_to_match in i:
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> file: %s - line:%s" % (file_name,line)
            line = line + 1
            count_strikes = count_strikes + 1
            i = f.readline()
        else:
            line = line + 1
            i = f.readline()
    
    if count_strikes == 0:
        print "file: %s - No matchs" % (file_name)


if __name__ == "__main__":
    dir = sys.argv[1]
    string_to_match = sys.argv[2]

    #print dir
    #print string_to_match
    elementos_dir = lista_dir(dir)

    for i in elementos_dir:
        if ".js" in i or ".php" in i or ".html" in i:
            filter_in_file(dir+i,string_to_match)


