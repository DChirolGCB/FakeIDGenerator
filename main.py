import json
import textwrap
import time
from random import randrange
## import tensorflow as tf
import faker
import requests
from PIL import Image, ImageFont, ImageDraw

## import deep_dream
import videoremake

fake = faker.Faker()
fnames = faker.Faker(['it_IT', 'en_US', 'fr_FR', "es_ES", "fr_CA", "fr_CH", "de_DE"])

with open('frenchcities.csv') as f:
    lines = f.read().splitlines()

with open('motseneur.txt') as eur:
    moteurs = eur.read().splitlines()

with open('demons.txt') as d:
    demons = d.read().splitlines()


def genderchoice():
    n = randrange(int(1), int(3))
    if n == 1:
        return "le"
    if n == 2:
        return "la"
    if n == 3:
        return "l'"


def animalax():
    animal = randrange(0, 15)
    g = str(genderchoice())
    if g == "le":
        tableau = open("AnimalM.json", encoding="utf-8")
    elif g == "la":
        tableau = open("AnimalF.json", encoding="utf-8")
    else:
        tableau = open("AnimalN.json", encoding="utf-8")

    words = tableau.read().splitlines()
    tableau.close()
    line = words[randrange(len(words))]
    linejson = json.loads(line)
    if animal >= 8:
        return ", dit '" + g + " " + linejson["M"] + "'"
    else:
        return ""


def dix(value):
    if value >= 9:
        return True


namegenlist1 = ["Gor", "Mit", "Pax", "Moul", "Beuz", "For", "Zir", "Ner", "Cir", "Chol", "Pex", "Sex", "Kur", "Vor",
                "Gal", "Gad",
                "Mik", "Tur", "Mok", "Pess", "Fess", "Kal", "Ir", "Loit", "Ker", "Jal", "Jol", "Mor", "Breut", "Brat",
                "Katt", "Moul", "Ber", "Pal", "Paul", "Pul", "Huss", "Hass", "Nar", "Gormit", "Rat", "Sac", "Arc",
                "Gant",
                "Sang", "Banc", "Vent", "Paon", "Cent", "Dix", "Six", "Mie", "Scie", "Lit", "Nid", "Pain", "Main",
                "Train",
                "Daim", "Faim", "Bain", "Coq", "Bol", "Pot", "Dos", "Tôt", "Cou", "Clou", "Pou", "Grue", "Jus", "Bus",
                "Pull", "Rue", "Mur", "Dur", "Pied", "Clé", "Fé", "Thé"
                ]
namegenlist2 = ["oiz", "beuz", "jix", "mol", "gara", "bul", "ren", "pil", "nol", "lam", "poire", "pom", "jet", "nnet",
                "ur", "âpre", "ger", "ala", "otu", "peplu", "klum"]
namegenlist3 = ["ol", "ère", "ope", "ez", "ot", "jule", "max", "mine", "mont", "ane", "kore", "kepec", "kule", "oure",
                "line", "aque", "uque", "trand", "are", "ique", "ock", "ute", "oute", "asse"]

len1 = len(namegenlist1)
len2 = len(namegenlist2)
len3 = len(namegenlist3)
text = ''
o = 0

for i in range(1):
    time.sleep(1)
    im = Image.open(requests.get("https://thispersondoesnotexist.com/image", stream=True).raw)
    # im = deep_dream.process_frame(in_frame)
    # im = Image.open(requests.get("https://d1m8f0nfw1jwvl.cloudfront.net/61000/", stream=True).raw)
    firstn = fnames.first_name()
    ex = str(moteurs[randrange(0, len(moteurs))])
    long = randrange(0, 10)
    particule = randrange(0, 10)
    text = str(firstn.partition(' ')[0]) + ' ' + str(
        namegenlist1[randrange(0, len1)] + namegenlist2[randrange(0, len2)])

    if dix(long):
        text = str(text) + (namegenlist3[randrange(0, len3)])
    if dix(particule):
        text = str(text) + " de " + str(lines[randrange(0, len(lines))])

    niet = animalax()
    if niet != "":
        text = str(text) + niet

    text = str(text) + ", " + ex + " de " + str(demons[randrange(0, len(demons))])
    print(text)

    draw = ImageDraw.Draw(im)
    fontsize = 50
    textimage = text
    imgfraction = 0.90

    para = textwrap.wrap(text, width=15)
    MAX_W, MAX_H = 1024, 1024

    font = ImageFont.truetype(r"C:\Users\David\Documents\Battlefield 4\twinkle\assets\Roboto-Medium-89302f17.ttf",
                              70)
    current_h, pad = 50, 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font)
        current_h += h + pad

    # Nom du fichier image
    # o = o + 1
    # nb_image = str(o)
    # final = str('output' + str(nb_image) + '.jpeg')
    im.save('test.jpeg')
    videoremake.makevideo()






    # while font.getsize(text)[0] < imgfraction*im.size[0]:
    #     fontsize += 1
    #     font = ImageFont.truetype("arial.ttf", fontsize)
    # print(imgfraction)
    # draw.text((10, 10), text, fill="yellow", font=font, align="center")
