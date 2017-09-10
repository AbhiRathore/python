import nltk
from nltk import *
import urllib2 
import requests
import re


page="http://shakespeare.mit.edu/Poetry/LoversComplaint.html"
#req = urllib2.Request(page)page_text=urllib2.urlopen(page).read()

req = urllib2.Request(page)
response = urllib2.urlopen(req)
the_page = response.read()
raw=re.sub("\\n\\n<BLOCKQUOTE>\\n","",the_page)
raw1=re.sub("<\/BLOCKQUOTE>\\n","",raw)
raw2=re.sub("<BLOCKQUOTE>","",raw1)
raw3=re.sub("</TITLE>","",re.sub("<\\BODY","",raw2))
raw4=re.sub("</BODY>","",re.sub("</BLOCKQUOTE","",re.sub("<BODY>","",raw3)))
raw5=re.sub("<HTML","",re.sub(">","",re.sub("<BR>","",re.sub("</HTML>","",raw4))))
raw6=re.sub("HEAD","",re.sub("when","",re.sub("/H1FROM","",re.sub("TITLE","",raw5))))
raw7=re.sub("THE","",re.sub("\?","",re.sub("and","",re.sub("\,!\\,\;\?and the ","",raw6))))

#words=["HEAD","TITLE","THE","H1A","<","/H1FROM"]
print raw7
tokens=word_tokenize(raw7)
#print tokens
#result = list(set(tokens) - set(words))
#print result
fdist1 = FreqDist(tokens)
#print fdist1.tabulate()
#fdist1.plot(100, cumulative=True)
