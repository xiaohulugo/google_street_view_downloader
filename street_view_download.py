import os
import json
import urllib2
import sys
import time

myloc = "/home/images/"   #replace with your own location
key = "&key=" + ""        #got banned after ~100 requests with no key
position = "-34.798734,-58.468581"

def GetStreet(orientation,save_path):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

  base = "https://maps.googleapis.com/maps/api/streetview?size=13312x6656&location="
  img_url = base + position + orientation + key
  print (img_url) 

  if not os.path.exists(save_path + position):
        os.makedirs(save_path + position)

  req = urllib2.Request(img_url, headers=headers)
  raw_img = urllib2.urlopen(req).read()

  file_out = save_path + position + "/" + orientation + ".jpg"
  f = open(file_out, "wb")
  f.write(raw_img)
  f.close

orientation_set = ["&heading=0.0&pitch=0.0",
                  "&heading=60.0&pitch=0.0",
                  "&heading=120.0&pitch=0.0",
                  "&heading=180.0&pitch=0.0",
                  "&heading=240.0&pitch=0.0",
                  "&heading=300.0&pitch=0.0",
                  "&heading=360.0&pitch=0.0"]

for i in orientation_set:
  GetStreet(orientation=i,save_path=myloc)