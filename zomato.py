import requests
import re
from requests import *
import xml.etree.ElementTree as ET
import re
import json
import urllib2
from bs4 import BeautifulSoup


url1= ("https://www.zomato.com")
l_1=urllib2.urlopen(url1,timeout=60)
#root1 = ET.fromstring((l_1.text.encode("utf-8")))
soup = BeautifulSoup(l_1)
soup.title





