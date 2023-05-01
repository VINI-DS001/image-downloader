import urllib.request

def download_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

img_url = input("Enter the image URL to download: ")
file_name = input("Enter file name to save as: ")

download_jpg(img_url, "images/", file_name)