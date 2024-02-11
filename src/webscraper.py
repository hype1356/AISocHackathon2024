from googlesearch import search
from bs4 import BeautifulSoup
import re
import requests
import lxml.etree as ET

info = []
def scrapeInformation(query):
  for j in search(query, tld="co.uk", num=5, stop=5, pause=2):
    if (re.search("gstatic",j)):
      continue
    if (re.search("\.gov",j)):
      continue
    if (re.search("\.pdf$",j)):
      continue
    source = requests.get(j).text
    soup = BeautifulSoup(source, "lxml")
    tree = ET.parse(soup.text.replace("\n", "").replace("    ", ""))
    targetTexts = tree.xpath("//P")
    for text in targetTexts:
      info += re.sub(r"\s{2,}", " ", (ET.toString(text, encoding="unicode", method="text")))
  return info
      
print(scrapeInformation("What do the ICAO requirements for dangerous goods aim to achieve?"))
