from PIL import Image
import os

for file in os.listdir("img"):
    
    image=Image.open("img/" + file)
    image.save("img/" + file[:-4] + ".png")