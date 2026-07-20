import requests
from PIL import Image
from io import BytesIO
url = "blob:https://pinetools.com/b1362584-d533-46a9-b94d-ce7b879f8f13"
r = requests.get(url)
i = BytesIO(r.content)
fp = open("randomfile.dmg", "wb")
fp.write(i)
fp.close()