import os
import urllib
from bs4 import BeautifulSoup
import urllib2


SUPPORT_IMAGES = (".jpg",".jpeg",".png",".gif",".tiff",".eps",)

def rmQ(fname):
    return fname.split("?")[0]

def getImgURL(src, url):
    if True in [src.endswith(support) for support in SUPPORT_IMAGES]:
        if "http" not in src:
            return url+src
        else:
            return src
    else:
        return 0

def mkdir(dirName):
    try:
        os.mkdir(dirName)
    except Exception as e:
        if dirName != "./DLImages":
            print e

def DLImages(AllImages, url, dirName):
    successNum = 0
    for img in AllImages:
        src = img.get("src")
        imgURL = getImgURL(src, url)

        if not imgURL:
            continue

        fname = src.split("/")[-1]

        if "?" in fname:
            fname = rmQ(fname)
        
        try:
            if fname in os.listdir(dirName):
                fname = fname + str(successNum)
            urllib.urlretrieve(imgURL, dirName+"/"+fname)
            print("[ Success ] %s %s" % (imgURL, fname))
            successNum += 1
        except Exception as e:
            print e
            print("[ Failed ] %s" % imgURL)

    return successNum

def main(url, dirName="./DLImages"):    
    mkdir(dirName)
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    AllImages = soup.find_all("img")
    imgNum = len(AllImages)
    successNum = DLImages(AllImages, url, dirName)

    print("%d images could be downloaded (in %d images)." % (successNum, imgNum))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python DLImage.py URL [directory]")
