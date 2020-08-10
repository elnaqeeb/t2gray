import json
import cv2 as cv
import datetime
from json import dumps


def main():
    img_path=input()
    img_Out=img_path+"new.jpg"
    try:
        img=cv.imread(img_path+".jpg")
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        cv.imwrite(img_Out,img)
        date_opp={}
        date_opp[img_Out]=str(datetime.datetime.now())
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(date_opp, f, ensure_ascii=False, indent=4)
    except:
        print("not found!!")

main()
