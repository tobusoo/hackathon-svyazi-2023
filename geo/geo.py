import json
from dadata import Dadata
from config import *


def dadata_get_addresses(dadata: Dadata, geo_lat: float, geo_lon: float, radius: int, max_count: int):
    response = dadata.geolocate(name="address", lat=geo_lat, lon=geo_lon, radius_meters=radius, count=max_count)
    return response


def dadata_get_postal(dadata: Dadata, postal_id: str):
    response = dadata.find_by_id("postal_unit", postal_id)
    return response


def postals_to_json(dadata: Dadata, ids):
    postal_addresses = []
    count = 0
    for id in ids:
        response = dadata_get_postal(dadata, id)
        for i in response:
            address = {}
            data = i['data']

            address['address_str'] = data['address_str']
            address['postal_code'] = data['postal_code']
            address['schedule_mon'] = data['schedule_mon']
            address['schedule_tue'] = data['schedule_tue']
            address['schedule_wed'] = data['schedule_wed']
            address['schedule_thu'] = data['schedule_thu']
            address['schedule_fri'] = data['schedule_fri']
            address['schedule_sat'] = data['schedule_sat']
            address['schedule_sun'] = data['schedule_sun']
            address['geo_lat'] = data['geo_lat']
            address['geo_lon'] = data['geo_lon']
            
            map_url = generate_url_by_coord(data['geo_lon'], data['geo_lat'])
            address['map_url'] = map_url
            postal_addresses.append(address)
            count += 1

    json_data = {'count': count, 'postals': postal_addresses}
    return json_data


def addresses_to_json(response,
                        need_postal: bool = True,
                        need_country: bool = True,
                        need_city: bool = True,
                        need_street: bool = True,
                        need_house: bool = True,
                        need_coord: bool = True):
    addresses = []
    count = 0
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
        map_url = generate_url_by_coord(data['geo_lon'], data['geo_lat'])
        address['map_url'] = map_url
        addresses.append(address)
        count += 1

    json_data = {'count': count, 'adresses': addresses}
    return json_data


def find_postal_ids(response):
    ids = set()
    for i in response:
        data = i['data']
        ids.add(data['postal_code'])
    return ids



def generate_url_by_coord(lon, lat):
    return f'https://yandex.ru/maps/?ll={lon},{lat}&z=21'



def write_json(filename: str, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def lat_check(lat):
    try:
        lat = float(lat)
    except ValueError:
        print('This is not a number!')
        return False
    else:
        if 77 >= lat >= 41:
            return True
        else:
            print("Incorrect latitude!")
            return False
    finally:
        None

def lon_check(lon):
    try:
        lon = float(lon)
    except ValueError:
        print('This is not a number!')
        return False
    else:
        if type(lon) != float:
            return False
        if 169 >= lon >= 19:
            return True
        else:
            print("Incorrect longitude!")
            return False
    finally:
        None
        
def rad_check(rad):
    try:
        rad = int(rad)
    except ValueError:
        print('This is not a number!')
        return False
    else:
        if type(rad) != int:
            return False
        if rad >= 0:
            return True
        else:
            print("Incorrect radius!")
            return False
    finally:
        None        

def main():
    lat = input('Enter lat:')
    if lat_check(lat) == False:
        return
    # lat = 55.601983
    lon = input('Enter lon:')
    if lon_check(lon) == False:
        return
    # lon = 37.359486
    radius = input('Enter radius:')
    if rad_check(radius) == False:
        return
    # radius = 50
    max_count = 20
    dadata = Dadata(DADATA_TOKEN)

    response = dadata_get_addresses(dadata, lat, lon, radius, max_count)
    adresses = addresses_to_json(response)
    write_json('dadata_cool.json', adresses)

    unique_postal_ids = find_postal_ids(response)
    postals = postals_to_json(dadata, unique_postal_ids)
    write_json('dadata_postals.json', postals)


if __name__ == "__main__":
    main()
