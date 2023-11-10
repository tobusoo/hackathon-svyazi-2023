from dadata import Dadata
import json
from tg.config import *


def dadata_response(geo_lat: float, geo_lon: float, radius: int):
    dadata = Dadata(DADATA_TOKEN)
    result = dadata.geolocate(name="address", lat=geo_lat, lon=geo_lon, radius_meters=radius)
    return result


def write_response_to_json(filename: str, result):
    addresses = []
    for i in result:
        data = i['data']

        postal_code = data['postal_code']
        country = data['country']
        city = data['city']
        street = data['street']
        house = data['house']
        lat = data['geo_lat']
        lon = data['geo_lon']
        if street is None:
            continue

        address = {'country': country, 'city': city,
                   'street': street, 'house': house,
                   'postal_code': postal_code,
                   'lat': lat, 'lon': lon}

        addresses.append(address)
        print(address)

    json_data = {'suggestions': addresses}
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)


def main():
    # lat = float(input('Enter lat:')) # 55.878
    lat = 55.878
    # lon = float(input('Enter lon:')) # 37.653
    lon = 37.653
    # radius = int(input('Enter radius:')) # 50
    radius = 100
    result = dadata_response(lat, lon, radius)
    write_response_to_json('dadata_cool.json', result)


if __name__ == "__main__":
    main()