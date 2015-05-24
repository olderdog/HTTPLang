import urllib
import utils
import sys

def do(line):
    subKeys = {

            "GET":get,
            "POST":post,

    }

    subKeys[line[1]](line)


def get(line):
    if not utils.baseVariables['URL']:
        sys.exit("Error on line {}, URL not set.".format(utils.lines))

    source = urllib.urlopen(utils.baseVariables['URL'] + line[2]).read()    
    utils.baseVariables["HTML"] = source

def post(line):
    pass
