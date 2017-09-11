def grab_iff_photo(url):
    import requests
    response = requests.head(url)
    content_type = response.headers.get('content-type')
    if content_type.startswith('image'):
        image = requests.get(url)
        with open(url.split('/')[-1], 'wb') as image_file:
            image_file.write(requests.get(url).content)

grab_iff_photo("https://dgplug.org/assets/img/header.png")
