'''
Filename: c:\Users\ocdav\source\repos\IDgenerator\main.py
Path: c:\Users\ocdav\source\repos\IDgenerator
Created Date: Wednesday, December 15th 2021, 12:46:57 pm
Author: David Chirol

Copyright (c) 2022 Your Company
'''

import requests
import json
import textwrap
import os
import numpy as np
import cv2 as cv
import time
from PIL import ImageFont, ImageDraw, Image, ImageEnhance, ImageFilter, ImageOps
import skimage
from skimage import data, io, filters
import random
from random import randrange
from faker import Faker

def ReplacePixelsInImage(image, pixels, tolerance):
    ret = image.copy()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if (image.getpixel((x, y))[0] >= pixels[0]-tolerance and image.getpixel((x, y))[0] <= pixels[0]+tolerance and
                image.getpixel((x, y))[1] >= pixels[1]-tolerance and image.getpixel((x, y))[1] <= pixels[1]+tolerance and
                image.getpixel((x, y))[2] >= pixels[2]-tolerance and image.getpixel((x, y))[2] <= pixels[2]+tolerance):
                ret.putpixel((x, y), (0, 0, 0, 0))
    return ret

def GenerateID(number):
    fake = Faker()
    fake = Faker(['fr_FR', "it_IT"])
    genre = random.choice("F""M")
    fnamenumbers = randrange(1,3)
    fname = fake.first_name()
    i = 0

    while i < fnamenumbers:
        fname += " " + fake.first_name()
        i += 1

    ##IMG PREP
    img = Image.open("ID.png").convert('RGBA')
    draw = ImageDraw.Draw(img)  
    font = ImageFont.truetype("OCR B Std Regular.otf", 30)

    ##PHOTO
    photo = Image.open(requests.get("https://thispersondoesnotexist.com/image", stream=True).raw).convert('RGBA')
    size = 466, 600
    photo.thumbnail(size, Image.ANTIALIAS)
    ##photo = photo.convert('L')
    photo = ImageOps.crop(photo, (0, 0, 25, 10))
    img.paste(photo, [-100, 145])


    ##LAST NAME
    draw.text((450, 150), fake.last_name(), font=font, fill=(0,30,200,255))

    ##FIRST NAMES
    draw.text((510, 247), fname, font=font, fill=(0,30,200,255))  

    ##GENDER
    draw.text((450, 330), genre, font=font, fill=(0,30,200,255)) 

    ##DATE
    draw.text((793, 332), str(fake.date_of_birth()), font=font, fill=(0,30,200,255)) 

    ##DATE
    draw.text((400, 375), str(fake.city()), font=font, fill=(0,30,200,255)) 

    ##CARD NUMBER
    draw.text((500, 95), fake.ssn(), font=font, fill=(0,30,200,255)) 

    ##HEIGHT
    draw.text((467, 413), str(random.randrange(145, 200)) + "cm", font=font, fill=(0,30,200,255)) 

    ##SIGNATURE
    sign = Image.open('.\\signaturedb\\' + random.choice(os.listdir("signaturedb"))).convert('RGBA')
    sign = ReplacePixelsInImage(sign, (255, 255, 255), 45)
    basewidth = 400
    wpercent = (basewidth/float(sign.size[0]))
    hsize = int((float(sign.size[1])*float(wpercent)))
    sign = sign.resize((basewidth,hsize), Image.ANTIALIAS)

    img.paste(sign, (526, 415), sign)
    img.paste((0,30,200), (526, 415), sign)
    img.save("ID_" + str(number) + ".png", format='PNG')
    
for i in range(0, 5):
    GenerateID(i)
