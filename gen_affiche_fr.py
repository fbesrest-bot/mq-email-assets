"""Affiche FR pour les courriels : corrige le double symbole euro sur l'ecran du portable."""
from PIL import Image, ImageDraw, ImageFont

SRC = "/Users/francky/Documents/CLAUDE CODE/BESREST-OS/Projects/PLUGIN-DEVIS/png/Mesurez, estimez, gagnez du temps.png"
B = "/Users/francky/mq-email-assets/Poppins-Bold.ttf"

im = Image.open(SRC).convert("RGB").resize((800, 1200), Image.LANCZOS)
d = ImageDraw.Draw(im)
teal = im.getpixel((192, 572))
d.rounded_rectangle((188, 569, 308, 599), radius=5, fill=teal)
d.text((248, 584), "836 €", font=ImageFont.truetype(B, 26), fill=(255, 255, 255), anchor="mm")
im.save("mq-poster-fr.jpg", "JPEG", quality=84, optimize=True)
im.crop((120, 500, 420, 660)).resize((600, 320)).save("/tmp/apercu-fr.png")
print("ok")
