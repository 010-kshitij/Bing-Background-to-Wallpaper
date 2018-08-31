import requests
import os
import json

def set_wallpaper(file_link):
    directory_full_path = os.path.abspath("./")
    os.system("gsettings set org.gnome.desktop.background picture-uri {}/{}".format(directory_full_path, file_link))

link = "https://www.bing.com/HPImageArchive.aspx?format=js&mbl=1&idx=0&n=1&cc=in"
bing_url = "http://www.bing.com"

page = requests.get(link, "html.parser")
html = page.text

data = json.loads(html)
wallpaper = bing_url + data['images'][0]['url']

image_data = requests.get(wallpaper)
with open("wallpaper.jpg", "wb") as file:
	file.write(image_data.content)

set_wallpaper("wallpaper.jpg");
