import requests

# The following code can write the source code of site into file below
data = requests.get("https://www.google.com");
with open ("index.html" , 'w') as f:
    f.write(data.text)