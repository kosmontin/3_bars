#!/usr/bin/env python
import json
import math

def load_data(filepath='bars.json'):
    with open(filepath, encoding='utf-8') as file_handler:
        bars = json.loads(file_handler.read())
        return bars['features']


def get_biggest_bar(data):
    return max(data, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(data, longitude=37.620374, latitude=55.753556):
    return sorted(data, key=lambda bar: math.sqrt((abs(bar['geometry']['coordinates'][0] - longitude) ** 2) +
                                                  abs((bar['geometry']['coordinates'][1] - latitude) ** 2)))


if __name__ == '__main__':
    print('''
    Добро пожаловать! 
    Данный скрипт ищет в json-файле самый большой и маленький бар. 
    А так же ищет ближайший бар по заданным начальным координатам.
    Если вы видите этот текст, значит скрипт запущен с параметрами по умолчанию.
    Файл bars.json, начальные координаты: Красная Площадь.
    ''')
    print('Самый маленький бар:', get_smallest_bar(load_data())['properties']['Attributes']['Name'],
          'Количество мест: ', get_smallest_bar(load_data())['properties']['Attributes']['SeatsCount'])
    print('Самый большой бар:', get_biggest_bar(load_data())['properties']['Attributes']['Name'],
          'Количество мест: ', get_biggest_bar(load_data())['properties']['Attributes']['SeatsCount'])
    print('Ближайший бар:', get_closest_bar(load_data())[0]['properties']['Attributes']['Name'],
          '\nНаходится по адресу: ', get_closest_bar(load_data())[0]['properties']['Attributes']['Address'])
    pass
