import md5

'''
2 functions:
_generate_md5 --> generae a md5 from a file
_check_md5 --> check check if is a valid md5
'''

def _generate_md5(file_name_source):
    '''
    recieves:
    file_name_source -> file to generate a md5 file

    generate a md5 file with name file_name_source.md5
    
    '''
    try:
        f = open(file_name_source, 'r')
    except:
        print "error to open file_name_source %s @ generate_md5 func" \
                                                  % file_name_source

    
    line = f.readline()
    m = md5.new()
    while line:
        m.update(line)
        line = f.readline()
        
    f.close()
    md5_string = m.hexdigest()

    if "." in file_name_source:
        md5_file_name = file_name_source.replace(".", "_")+".md5"
    else:
        md5_file_name = file_name_source+".md5"

    try:
        f = open(md5_file_name, "w")
    except:
        print "error to open md5_file %s" % md5_file
        

    try:
        f.write(md5_string)
    except:
        print "error to write md5_file %s @ generate_md5 function" \
                                                        % md5_file
        
    f.close()


def _check_md5(file_2_check, md5_file):
    '''
    recieves:
    file_2_check -> file to check 

    return True if file_2_check match with the md5 file
    return False if file_2_check do not match with the md5 file
    '''

    try:
        f = open(file_2_check, 'r')
    except:
        print "error to open file_2_check %s @ check_md5 function" \
                                                  % file_2_check
        
    
    line = f.readline()
    m = md5.new()
    while line:
        m.update(line)
        line = f.readline()
        
    f.close()
    md5_string = m.hexdigest()


    try:
        f = open(md5_file, 'r')
    except:
        print "error to open md5_file %s @ check_md5 funcion" \
                                                % md5_file
                

    line = f.readline()
    f.close()
    if line == md5_string:
        return True
    else:
        return False
    

   



if __name__ == "__main__":
    pass
