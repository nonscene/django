import requests

name = input("enter your profile name: ")
url = "https://instagram-profile1.p.rapidapi.com/getprofile/{name}"

headers = {
	"X-RapidAPI-Key": "9d15186cbfmsh29b566f03a7e51cp13db8ajsn7e9d9a2e34f9",
	"X-RapidAPI-Host": "instagram-profile1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())