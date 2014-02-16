from bs4 import BeautifulSoup
import urllib2, urllib
import sys, os


def main(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    
    os.mkdir("./"+url.split("/")[2])
    AllImages = soup.find_all("img")
    imgNum = len(AllImages)
    for img in AllImages:
        src = img.get("src")
        DLFile = src
        if "http" not in DLFile:
            DLFile = url+DLFile

        fname = src.split("/")[-1]
        if "?" in fname:
            fname = fname.split("?")[0]

        successnum = 0
        try:
            urllib.urlretrieve(DLFile, url.split("/")[2]+"/"+fname)
            print DLFile
            successnum += 1
        except:
            print DLFile+" [ Failed ]"

    print successnum, "images could be downloaded (in", imgNum, "images)."

if __name__ == "__main__":
    main(sys.argv[1])
