import requests
from PIL import Image
from io import BytesIO

r = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXYmnqOEJK8e45ibziy63AIs9543yXqUaVsWSxdCSQnwEXgVEFJoVY8JWXc143AKhDtBCZQVWf2OyXeOKQzU7Zku8KN4_xpv_ehRKAMw&s=10')

i = Image.open(BytesIO(r.content))
fp = open("img.jpg" , "wb")
i.save(fp)
fp.close