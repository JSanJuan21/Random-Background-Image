import requests

def download_image():

    api_key = "PZxXF7rZjZl5_QLUxWJUgnF6Zc8WJZCd_CGqPiiHSFo"
    url = "https://api.unsplash.com/photos/random"
    params = {
        "client_id": api_key,
        "orientation": "landscape",
        "topics": "bo8jQKTaE0Y",
        "query": "space",
    }

    response = requests.get(url, params)

    if response.status_code == 200:
        data = response.json()
        image_url = data["links"]["download"]
        img_data = requests.get(image_url).content
        with open('C:\\Users\\jorge.sanjuan\\Pictures\\background.jpg', 'wb') as handler:
            handler.write(img_data)
        
    else:
        print(f"Request failed with status code {response.status_code}")

