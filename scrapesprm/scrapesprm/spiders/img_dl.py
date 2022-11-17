import json
import requests

with open("img.json") as file:

    img_data = json.loads(file.read())
    
    i = 0

    for item in img_data:

        if "img" in item.keys():

            img_url = item["img"]
            response = requests.get(img_url)

            name = img_url.split('/')
            file_name = f'{name[-1]}'

            if response.status_code == 200:
                
                with open(f'images/{file_name}', "wb") as f:
                    f.write(response.content)
                    i += 1