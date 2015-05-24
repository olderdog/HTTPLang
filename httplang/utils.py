import do
import setvar
import sys

lines = 0

baseVariables = {

        "URL":None,
        "TMPCOOKIE":None,
        "HTML":None,
        "HEADERS":None,
        "POSTDATA":None,

}

keywords = {

        "do":do.do,
        "set":setvar.setvar,

}


def typeDetermin(data):
    if data.startswith("$"):
        data = data[1:]
        if data in baseVariables:
            return baseVariables[data]
        else:
            sys.exit("Error on line {0}, variable ${1} is not a base variable.")

    return data
