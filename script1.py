import requests

def get_manor_ids(place_id):
	data = requests.get("https://opendomesday.org/api/1.0/place/" + str(place_id))
	place = data.json()
	if 'manors' in place.keys():
		return place['manors']
	else:
		return []

if __name__ == '__main__' :
	print(get_manor_ids(1036))

