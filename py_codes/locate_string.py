import os
import sys

'''
5 minutes to create this script
this script is using to find a file with a string.
is like "| grep" :)
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
    f.close()

 
    if count_strikes == 0:
        print "file: %s - No matchs" % (file_name)


if __name__ == "__main__":
    if sys.argv[1] == "help" and len(sys.argv) == 2:
        print "python locate_string.py [dir] word all"
        print "python locate_string.py [dir] word '[\"ext1\", \"ext2\"]"

    elif len(sys.argv) == 4:
        dir = sys.argv[1]
        string_to_match = sys.argv[2]
        ext_list = eval(sys.argv[3])

        elementos_dir = lista_dir(dir)

        for i in elementos_dir:
            if sys.argv[3] == "all":
                filter_in_file(dir+i,string_to_match)

            else:
                for ext in ext_list:
                    if ext in i:
                        filter_in_file(dir+i,string_to_match)
