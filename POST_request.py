import requests

# The arguments written after link is added to args{....}
# The data written after comma is added to form{....}

r = requests.post('https://httpbin.org/post?a=b' , data = {'A' : 'A'})

print(r.text)