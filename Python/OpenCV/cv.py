# -*- coding: UTF-8 -*-
# 
import cv2
import matplotlib.pyplot as plt

def main():

    img = cv2.imread('la.jpg')
    cv2.imshow('la', img)

    # ネガポジ変換
    mono = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('la-mono', mono)

    # キー入力を待って終了
    cv2.waitKey(0)
    cv2.destroyAllwindows()

if __name__ == "__main__":
    main()
