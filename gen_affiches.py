"""Declinaisons de l'affiche US (monnaie + m2) pour les courriels de prospection."""
from PIL import Image, ImageDraw, ImageFont

SRC = "/Users/francky/Documents/CLAUDE CODE/BESREST-OS/Projects/PLUGIN-DEVIS/png/Affiche Measured Quote pour le marché américain.png"
B = "/Users/francky/mq-email-assets/Poppins-Bold.ttf"


def make(area, money, rate, out):
    im = Image.open(SRC).convert("RGB")
    if im.size != (1024, 1536):
        im = im.resize((1024, 1536), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    scr = im.getpixel((296, 690)); teal = im.getpixel((240, 735)); band = im.getpixel((438, 1296))
    d.rectangle((298, 682, 412, 722), fill=scr)
    d.text((356, 702), f"{area} m²", font=ImageFont.truetype(B, 30), fill=(20, 24, 32), anchor="mm")
    d.rounded_rectangle((238, 729, 398, 769), radius=6, fill=teal)
    d.text((318, 750), f"{money}1,000", font=ImageFont.truetype(B, 36), fill=(255, 255, 255), anchor="mm")
    d.rectangle((432, 1272, 948, 1332), fill=band)
    d.text((690, 1302), f"{area} m² × {money}{rate}/m² = {money}1,000", font=ImageFont.truetype(B, 40), fill=(15, 20, 30), anchor="mm")
    im.save(out, "JPEG", quality=82, optimize=True)


make(40, "£", 25, "mq-poster-uk.jpg")
make(40, "€", 25, "mq-poster-eu.jpg")
make(40, "$", 25, "mq-poster-au.jpg")
print("ok")
