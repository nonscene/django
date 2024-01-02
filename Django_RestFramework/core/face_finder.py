import requests

name = input("enter your profile name: ")
url = "https://instagram-profile1.p.rapidapi.com/getprofile/parth_thakkar_57}"

headers = {
	"X-RapidAPI-Key": "your api key",
	"X-RapidAPI-Host": "instagram-profile1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())