def rmQ(fname):
    return fname.split("?")[0]

def getImgURL(src, url):
    if "http" not in src:
        return url+src
    else:
        return src

def mkdir(dirName):
    import os
    try:
        os.mkdir(dirName)
        print "mkdir"
    except Exception as e:
        print e
#        pass # if dirName already exist

def DLImages(AllImages, url, dirName):
    import urllib

    successNum = 0
    for img in AllImages:
        src = img.get("src")
        imgURL = getImgURL(src, url)
        fname = src.split("/")[-1]

        if "?" in fname:
            fname = rmQ(fname)
        try:
            urllib.urlretrieve(imgURL, dirName+"/"+fname)
            print "[ Success ] " + imgURL
            successNum += 1
        except Exception as e:
            print e
            print "[ Failed ] " + imgURL        

    return successNum

def main(url, dirName="./DLImages"):
    from bs4 import BeautifulSoup
    import urllib2
    
    mkdir(dirName)
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    AllImages = soup.find_all("img")
    imgNum = len(AllImages)
    successNum = DLImages(AllImages, url, dirName)

    print successNum, "images could be downloaded (in", imgNum, "images)."

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
