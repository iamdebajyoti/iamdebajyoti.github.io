from PIL import Image
import random
import requests

url="https://www.shutterstock.com/shutterstock/photos/2513436989/display_1500/stock-photo-red-rose-background-valentine-s-flower-design-space-2513436989.jpg"
file_name="red_rose1.jpg"

response=requests.get(url, stream=True)

with open(file_name, "wb") as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)


i=Image.open(file_name)
p=i.load()

for _ in range(3000):
    x,y=random.randint(0,i.width-1),random.randint(0,i.height-1)
    p[x,y]=(255,0,0)

i.show()

