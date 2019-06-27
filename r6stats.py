import requests
from bs4 import BeautifulSoup

#r6.tracker.network/profile/pc/ + username to form user stat profile url
site_url = 'https://r6.tracker.network/profile/'
platform = input('Enter your platform: pc, psn or xbox: ').lower()
username = "/" + input('Enter your Uplay username: ')
stats_url_final = site_url + platform + username
#get the data from the final url
response = (requests.get(stats_url_final)).text

#here I create a soup object
soup = BeautifulSoup(response, 'lxml')

#here I use the .select method to take the div class
stats = soup.select(".r6-season-list")


#here I create a function that gets the stats
def get_stats():
	for stat in stats:
		print(stat.text)

get_stats()