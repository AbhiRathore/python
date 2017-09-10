import urllib2
import csv
import re
import cStringIO
import PIL
import requests
from PIL import Image
import pandas as pd

r = open('D:/image_url_name.csv', 'rb')
images = pd.read_csv(r)

images['status'] = ''

for i in range(0,images.shape[0]):
    req = urllib2.Request(images['url'][i],headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib2.urlopen(req)
        the_page = cStringIO.StringIO(response.read())
        w=0
        try:
            Image.open(the_page)
            images['status'][i] = 'correct'
            w=1
        except:
            images['status'][i] = 'error'
            w=0
    except:
        images['status'][i] = 'error in link'

images.to_csv('D:/image_check_out.csv')
