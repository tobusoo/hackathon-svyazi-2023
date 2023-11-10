import json
from dadata import Dadata
from config import *


def dadata_get_addresses(dadata: Dadata, geo_lat: float, geo_lon: float, radius: int, max_count: int):
    response = dadata.geolocate(name="address", lat=geo_lat, lon=geo_lon, radius_meters=radius, count=max_count)
    return response


def dadata_get_postal(dadata: Dadata, postal_id: str):
    response = dadata.find_by_id("postal_unit", postal_id)
    return response

def find_postal_ids(response):
    ids = set()
    for i in response:
        data = i['data']
        ids.add(data['postal_code'])
    return ids

def write_respons_to_json(filename: str, response,
                            need_postal: bool = True,
                            need_country: bool = True,
                            need_city: bool = True,
                            need_street: bool = True,
                            need_house: bool = True,
                            need_coord: bool = True):
    addresses = []
    for i in response:
        data = i['data']
        address = {}

        if need_postal:
            address['postal_code'] = data['postal_code']
        if need_country:
            address['country'] = data['country']
        if need_city:
            address['city'] = data['city']
        if need_street:
            address['street'] = data['street']
        if need_house:
            address['house'] = data['house']
        if need_coord:
            address['geo_lat'] = data['geo_lat']
            address['geo_lon'] = data['geo_lon']

        addresses.append(address)
        print(address)

    json_data = {'suggestions': addresses}
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)


def main():
    # lat = float(input('Enter lat:')) # 55.878
    lat = 55.012895
    # lon = float(input('Enter lon:')) # 37.653
    lon = 82.951024
    # radius = int(input('Enter radius:')) # 50
    radius = 1000
    max_count = 20
    dadata = Dadata(DADATA_TOKEN)
    response = dadata_get_addresses(dadata, lat, lon, radius, max_count)
    # write_response_to_json('dadata_cool.json', response)
    unique_postal_ids = find_postal_ids(response)
    for id in unique_postal_ids:
        print(dadata_get_postal(dadata, id))

if __name__ == "__main__":
    main()
