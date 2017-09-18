import requests

def grab_iff_imgage(url):
    response = requests.get(url)
    if not response.ok:
        print("error! link is not accessible")
        return
    if is_image(response.content):
        pass

def is_image(content):
    signatures = {
            \x42\x4d : 
    file_signature = content[:4]
    
