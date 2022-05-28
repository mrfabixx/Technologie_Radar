from configparser import ConfigParser
import os


def config(filename='dbcon.ini', section='postgresql'): #dbcon.ini = file which contains the logininformation for the sql server
    # create a parser

    parser = ConfigParser()
    parser.read(filename)

    #get section, default (psql)
    db = {}
    #check to see if section (psql) parser exists
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    
    #return an error if param is called that is NOT listed in (init) file
    
    else:
        raise Exception('Section{0} not fount in the file {1}'.format(section, filename))

    return db
