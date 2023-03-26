import requests

def main():
    	data = requests.get("https://opendomesday.org/api/1.0/county/dby/")
    	dby = data.json()
    	place_ids = dby["places_in_county"]
    	print(place_ids)

if __name__ == "__main__":
    	main()
