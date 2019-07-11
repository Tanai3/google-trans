# coding: utf-8
#
# Reference
# https://qiita.com/Sh1ma/items/e099b10c683cb0aaae83
# 
# Windows 改行コード\r\n
# Linux   改行コード\n 

import sys
import requests
import time

argvs = sys.argv
argc = len(argvs)

def usage():
    print("usage: google-translate.py INPUTFILE OUTPUTFILE")
    sys.exit()
    
def google_translate(sentence):
    url = "https://translate.google.com/translate_a/single"

    headers = {
        "Host": "translate.google.com",
        "Accept": "*/*",
        "Cookie": "",
        "User-Agent": "GoogleTranslate/5.9.59004 (iPhone; iOS 10.2; ja; iPhone9,1)",
        "Accept-Language": "ja-jp",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }
    # sentence = " ".join(argvs[1:])
    params = {
        "client": "it",
        "dt": ["t", "rmt", "bd", "rms", "qca", "ss", "md", "ld", "ex"],
        "otf": "2",
        "dj": "1",
        "q": sentence,
        "hl": "ja",
        "ie": "UTF-8",
        "oe": "UTF-8",
        "sl": "en",
        "tl": "ja",
    }
    res = requests.get(
        url=url,
        headers=headers,
        params=params,
    )
    res = res.json()
    return(res["sentences"][0]["trans"])

    

if __name__ == '__main__':
    if not len(sys.argv[1:]):
        usage()

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    with open(inputfile,"r") as f:
        Allf = f.read()
        # text = Allf.replace('\n',' ')
        # text = text.replace('. ','.\n')
        # split_text = Allf.replace("-\n", "").replace("\n", " ").replace(". ", ".\n ").split("\n")
        # split_text = text.split("\n")
        # split_text = Allf.replace("Fig. ", "Fig.").replace("\n", " ").replace(". ", ".\n ").split("\n")
        split_text = Allf.replace("Fig. ", "Fig.").replace(". ", ".\n ").split("\n")
        # split_text = Allf.split("\n")
        
    with open(outputfile,"w") as f:
        for s in range(len(split_text)):
            f.write(split_text[s])
            print(split_text[s])
            f.write('\n')
            ret = google_translate(split_text[s])
            f.write(ret)
            print(ret)
            f.write('\n\n')
            print("%d/%d" % ((s+1),len(split_text)))
            time.sleep(3)
        
