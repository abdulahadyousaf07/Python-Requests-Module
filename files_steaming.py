import requests
from tqdm import tqdm

# url = 'https://assets.mixkit.co/active_storage/sfx/213/213.wav'
url = 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-722.exe'

r = requests.get(url , stream = True)
totalExpectedBytes = int(r.headers["Content-Length"])

bytesReceived = 0

progress_bar = tqdm(total=totalExpectedBytes , unit='iB' , unit_scale= True)

with open("winrar.exe" , "wb") as f:
    for chunk in r.iter_content(chunk_size=128):
        # print(f"{bytesReceived} received out of total {totalExpectedBytes} ")
        progress_bar.update(128)
        f.write(chunk)
        bytesReceived += 128
progress_bar.close()