#!/usr/bin/env python3.7

import os
import cv2

file = 'example.png'
img = cv2.imread(file)

def _3x1():
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0])}:{str(img.shape[0])}:0:0" -c:a copy out1.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0])}:{str(img.shape[0])}:{str(int(img.shape[0]))}:0" -c:a copy out2.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0])}:{str(img.shape[0])}:{str(int(img.shape[0]*2))}:0" -c:a copy out3.png')

def _1x1():
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0]/3)}:{str(img.shape[0]/3)}:0:0" -c:a copy out1.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0]/3)}:{str(img.shape[0]/3)}:{str(img.shape[0]/3)}:0" -c:a copy out2.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0]/3)}:{str(img.shape[0]/3)}:{str(img.shape[0]/3*2)}:0" -c:a copy out3.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0]/3)}:{str(img.shape[0]/3)}:0:{str(img.shape[0]/3)}" -c:a copy out4.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0]/3)}:{str(img.shape[0]/3)}:{str(img.shape[0]/3)}:{str(img.shape[0]/3)}" -c:a copy out5.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0]/3)}:{str(img.shape[0]/3)}:{str(img.shape[0]/3*2)}:{str(img.shape[0]/3)}" -c:a copy out6.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0]/3)}:{str(img.shape[0]/3)}:0:{str(img.shape[0]/3*2)}" -c:a copy out7.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0]/3)}:{str(img.shape[0]/3)}:{str(img.shape[0]/3)}:{str(img.shape[0]/3*2)}" -c:a copy out8.png')
    os.system(f'ffmpeg -i {file} -filter:v "crop={str(img.shape[0]/3)}:{str(img.shape[0]/3)}:{str(img.shape[0]/3*2)}:{str(img.shape[0]/3*2)}" -c:a copy out9.png')

def main():
    if (img.shape[1]) == 3*(img.shape[0]):
        _3x1()

    elif (img.shape[0]) == (img.shape[1]) and str(img.shape[0]/3).endswith(".0"):
        _1x1()
    
    else:
        print("Wrong format")
        input()

if __name__ == '__main__':
    main()
