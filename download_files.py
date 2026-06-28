import requests
from PIL import Image
from io import BytesIO

url = 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-722.exe'

r = requests.get(url)

fp = open("winrar.exe" , "wb")
fp.write(r.content)
fp.close