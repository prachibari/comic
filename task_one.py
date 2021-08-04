# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 23:24:07 2021

@author: SUMEET BARI
"""

from __future__ import print_function
import json
import requests
import mysql.connector
from json import JSONEncoder
from requests.exceptions import HTTPError
from types import SimpleNamespace
import random
import json

class Comic:
      def __init__(self, title, comic_meta):
        self.comic,self.comic_meta = title, comic_meta

class Comic_Meta:
      def __init__(self, alt,num,comic_url,image,img):
        self.alt_text,self.number,self.link,self.image,self.image_link = alt,num,comic_url,image,img

class ComicEncoder(JSONEncoder):
      def default(self, o): return o.__dict__


cnx = mysql.connector.connect(user='root', password = 'P@ssw0rd',database='mydb')
cursor = cnx.cursor()

cursor.execute("SELECT comic,alt_text,num,link,image,image_link from comic_data")
comic_list=[]

for comic, alt_text,num,link,image,image_link in cursor:
    comic_meta = Comic_Meta(alt_text,num,link,image,image_link)
    comic = Comic(comic,comic_meta)
    comicJsonData = json.dumps(comic, indent =4,cls=ComicEncoder)
    #print(comicJsonData)
    comic_list.append(comicJsonData)

print(','.join(comic_list))
# Close the connection
cnx.commit()
cursor.close()
cnx.close()

