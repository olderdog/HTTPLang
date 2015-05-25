import urllib2
import utils
import sys
from urllib import urlencode

def do(line):
    subKeys = {

            "GET":get,
            "POST":post,

    }
    
    try:
        subKeys[line[1]](line)
    except KeyError:
        sys.exit("Do error, no such request '{0}' on line {1}".format(line[1], utils.lines))

def get(line):
    if not utils.baseVariables['URL']:
        sys.exit("Error on line {}, URL not set.".format(utils.lines))

    url = utils.baseVariables['URL'] + line[2]
    request = urllib2.Request(url)
    request = __setHeaders(request)
    data = urllib2.urlopen(request)
    source = data.read()
    try:
        tmpcookie = data.info()['set-cookie']
        utils.baseVariables['TMPCOOKIE'] = tmpcookie
    except KeyError:
        pass
    utils.baseVariables["HTML"] = source

def post(line):
    if not utils.baseVariables["URL"]:
        sys.exit("Error on line {}, URL not set.".format(utils.lines))
    
    url = utils.baseVariables["URL"] + line[2]
    request = urllib2.Request(url, urlencode(utils.baseVariables["POSTDATA"]))
    request = __setHeaders(request)
    data = urllib2.urlopen(request)
    source = data.read()
    try:
        tmpcookie = data.info()["set-cookie"]
        utils.baseVariables["TMPCOOKIE"] = tmpcookie
    except KeyError:
        pass
    utils.baseVariables["HTML"] = source
    
def __setHeaders(request):
    if utils.baseVariables["COOKIE"]:
        request.add_header("Cookie", utils.baseVariables["COOKIE"])
    if utils.baseVariables["USERAGENT"]:
        request.add_header("User-Agent", utils.baseVariables['USERAGENT'])

    return request
