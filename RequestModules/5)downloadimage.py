import requests
from PIL import Image
from io import BytesIO
r = requests.get("https://static-cse.canva.com/blob/996499/Sanstitre.jpg")
i = Image.open(BytesIO(r.content))
fp = open("img.jpg", "wb")
i.save(fp)
fp.close()
