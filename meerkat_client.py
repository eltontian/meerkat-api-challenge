import httplib

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

httpServ = httplib.HTTPConnection("https://api.meerkatapp.co", 80)
httpServ.connect()

httpServ.request('GET', "/routes")

response = httpServ.getresponse()
if response.status == httplib.OK:
    print "Output from HTML request"
    printText (response.read())

# httpServ.request('GET', '/cgi_form.cgi?name=Brad&quote=Testing.')

# response = httpServ.getresponse()
# if response.status == httplib.OK:
#     print "Output from CGI request"
#     printText (response.read())

httpServ.close()