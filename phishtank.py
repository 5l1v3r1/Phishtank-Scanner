#!/usr/bin/python

import sys, getopt
from bs4 import BeautifulSoup
import urllib3

Victim = ""
Page2Scan = ""
totalvictim = 0
totalscan = 0

def main(argv):
   global Victim
   global Page2Scan
   try:
      opts, args = getopt.getopt(argv,"hv:p:",["victim=","Page2Scan="])
   except getopt.GetoptError:
      print ("test.py -v <Victim> -p <Page2Scan>")
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ("test.py -v <Victim> -p <Page2Scan>")
         sys.exit()
      elif opt in ("-v", "--victim"):
         Victim = arg
      elif opt in ("-p", "--page"):
        Page2Scan = arg
   print ("Victim is:", Victim)
   print ("Page to scan:", Page2Scan)
   print ("")

if __name__ == "__main__":
   main(sys.argv[1:])

for count in range(0,int(Page2Scan)):
	url = "https://www.phishtank.com/phish_search.php?page=%d" % count
	

	http = urllib3.PoolManager()
	response = http.request('GET', url)
	table = BeautifulSoup(response.data.decode('utf-8'),features="lxml")

	
	for tr in table.find_all('tr')[1:]:
		tds = tr.find_all('td')
		totalscan = totalscan + 1 
		if len(tds) == 5:
			Id = tds[0].find(text=True)
			UrlPhishing = tds[1].find(text=True)
			Submitted = tds[2].find(text=True)
			Valid = tds[3].find(text=True)
			Online = tds[4].find(text=True)
			if Victim in UrlPhishing:
				print("\t Phishing identified on url: " + UrlPhishing) 
				print("Found %d" % totalvictim + " cases of phishing on %d" % totalscan + " suspected phishes.")
				totalvictim = totalvictim + 1
				
if (totalvictim > 0):
	print("Found %d" % totalvictim + " cases of phishing on %d" % totalscan + " suspected phishes.")
