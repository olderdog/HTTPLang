import utils

def setvar(line):
    subKeys = {

            "URL":url,
            "POST":post,
            "SESSION":session,
    }

    subKeys[line[1]](line)

def url(line):
    utils.baseVariables['URL'] = utils.typeDetermin(line[2])
    
def post(line):
    data = line[2:]
    outDict = {}
    for x in data:
        x = x.split("=")
        outDict[x[0]] = x[1]

    utils.baseVariables["POSTDATA"] = outDict

def session(line):
    pass
