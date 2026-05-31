# import csv
# import sys
# from typing import Any
# from string import punctuation
# import json
# import pickle
# import xml.etree.ElementTree as ET
# print('Hello, chuvak!')
# print(25 * '-')
# '---------------------------------------------'
# '---------------------------------------------'
# '---------------------------------------------'
# def recursion(element, root):
#     if isinstance(element, dict):
#         for key, value in element.items():
#             if isinstance(value, dict):
#                 tag = ET.SubElement(root, key)
#                 recursion(value, tag)
#             elif isinstance(value, list):
#                 tag = ET.SubElement(root, key)
#                 for el in value:
#                     if isinstance(el, str):
#                         tag1 = ET.SubElement(tag, key[:-1])
#                         tag1.text = str(el)
#                     else:
#                         tag1 = ET.SubElement(tag, key[:-1])
#                         recursion(el, tag1)
#             else:
#                 tag = ET.SubElement(root, key)
#                 tag.text = str(value)
#     elif isinstance(element, list):
#         for el in element:
#             tag = ET.SubElement(root, root.tag[:-1])
#             recursion(el, tag)
#
# def save_to_xml(data: dict, filename: str) -> None:
#
#     for key, value in data.items():
#         root = ET.Element(key)
#         recursion(value, root)
#
#         tree = ET.ElementTree(root)
#         ET.indent(tree)
#         tree.write(filename, encoding = 'utf-8')
#
# # data = {
# #     "user": {
# #         "name": "Anna",
# #         "age": 25,
# #         "active": True
# #     }
# # }
#
# # data = {
# #     "users": [
# #         {"name": "Neo", "role": "Chosen One"},
# #         {"name": "Trinity", "role": "Hacker"},
# #         {"name": "Morpheus", "role": "Captain"}
# #     ]
# # }
#
# # data = {
# #     "order": {
# #         "id": 501,
# #         "customer": {
# #             "name": "Bruce Wayne",
# #             "city": "Gotham"
# #         },
# #         "total": 999.99
# #     }
# # }
#
# # data = {
# #     "itinerary": {
# #         "flights": [
# #             {
# #                 "number": "SU100",
# #                 "segments": [
# #                     {"from": "BER", "to": "PAR"},
# #                     {"from": "PAR", "to": "ROM"}
# #                 ],
# #                 "passengers": [
# #                     {"type": "ADT", "fare": {"base": 300, "tax": 50}},
# #                     {"type": "CHD", "fare": {"base": 200, "tax": 20}}
# #                 ]
# #             }
# #         ]
# #     }
# # }
#
# data = {
#     "party": {
#         "name": "Debuggers Anonymous",
#         "location": {
#             "city": "Byteville",
#             "venue": "Stack Trace Hall",
#             "note": "Bring snacks & patience"
#         },
#         "guests": [
#             {
#                 "nickname": "Captain Obvious",
#                 "role": "QA Hero",
#                 "stats": {"bugs_found": 42, "coffee_cups": 7}
#             },
#             {
#                 "nickname": "Null Pointer",
#                 "role": "Backend Wizard",
#                 "stats": {"bugs_found": 13, "coffee_cups": 999}
#             },
#             {
#                 "nickname": "Sir Segfault",
#                 "role": "C++ Sorcerer",
#                 "stats": {"bugs_found": 7, "coffee_cups": 3}
#             },
#             {
#                 "nickname": "Lady Regex",
#                 "role": "Pattern Summoner",
#                 "stats": {"bugs_found": 21, "coffee_cups": 5}
#             }
#         ],
#         "playlist": [
#             "Never Gonna Give You Up",
#             "404 Not Found (Remix)",
#             "Oops... I Did It Again",
#             "Under Pressure (CPU Edition)"
#         ],
#         "rules": {
#             "rule1": "No tabs, only spaces",
#             "rule2": "If it works, don't touch it",
#             "rule3": "Blame the cache (always)"
#         }
#     }
# }
#
# save_to_xml(data, 'files/xml/final.xml')
#
# with open('files/xml/final.xml', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_financial_report(filename: str, transactions: list[dict]) -> None:
#     res = {}
#
#     for item in transactions:
#         res.setdefault(item['client'], [{"amount": [], "currency":item['currency']}])
#         res[item['client']][0]["amount"].append(item['amount'])
#
#     root = ET.Element('report')
#
#     for key, value in res.items():
#         client = ET.SubElement(root, 'client')
#         client.set('name', key)
#
#         for item in value:
#             total = ET.SubElement(client, 'total')
#             total.text = str(sum(item['amount']))
#
#             currency = ET.SubElement(client, 'currency')
#             currency.text = item['currency']
#
#             trans_s = ET.SubElement(client, 'transactions')
#             for amount in item['amount']:
#                 transaction = ET.SubElement(trans_s, 'transaction')
#                 transaction.text = str(amount)
#
#     tree = ET.ElementTree(root)
#     ET.indent(tree)
#     tree.write(filename, encoding='utf-8')
#
# transactions = [
#     {"client": "Warren Buffett", "amount": 120, "currency": "USD"},
#     {"client": "Warren Buffett", "amount": 80, "currency": "USD"},
#     {"client": "Tony Stark", "amount": 200, "currency": "EUR"}
# ]
#
# export_financial_report('files/xml/report1.xml', transactions)
#
# with open('files/xml/report1.xml', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_driver_ratings(filename: str, ratings: list[dict]) -> None:
#     dict_norm = {}
#
#     for item in ratings:
#         dict_norm.setdefault(item['driver'], [])
#         dict_norm[item['driver']].append(item['rating'])
#
#     root = ET.Element('drivers')
#
#     for key, value in dict_norm.items():
#         driver = ET.SubElement(root, 'driver')
#         driver.set('name', key)
#
#         avg_rating = ET.SubElement(driver, 'avg_rating')
#         avg_rating.text = str(round(sum(value) / len(value),1))
#
#         reviews = ET.SubElement(driver, 'reviews')
#         reviews.text = str(len(value))
#
#     tree = ET.ElementTree(root)
#     ET.indent(tree)
#     tree.write(filename, encoding='utf-8')
#
# ratings = [
#     {"driver": "Batman", "rating": 5},
#     {"driver": "Batman", "rating": 4},
#     {"driver": "Spider-Man", "rating": 3}
# ]
#
# export_driver_ratings('files/xml/drivers1.xml', ratings)
#
# with open('files/xml/drivers1.xml', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_company_structure(filename: str, departments: dict) -> None:
#     root = ET.Element('company')
#
#     for key, value in departments.items():
#         department = ET.SubElement(root, 'department')
#         department.set('name', key)
#
#         for item in value:
#             employee = ET.SubElement(department, 'employee')
#             employee.text = item
#
#     tree = ET.ElementTree(root)
#     ET.indent(tree)
#     tree.write(filename, encoding='utf-8')
#
# departments = {
#     "IT": ["Anna", "Leo"],
#     "HR": ["Maria"]
# }
#
# export_company_structure('files/xml/company1.xml', departments)
#
# with open('files/xml/company1.xml', 'r', encoding='utf-8') as file:
#     print(file.read())
'---------------------------------------------'
# def export_orders(filename, orders) -> None:
#     root = ET.Element('orders')
#
#     for item in orders:
#         order = ET.SubElement(root, 'order')
#         order.set('id', str(item['id']))
#
#         amount = ET.SubElement(order, 'amount')
#         amount.text = str(item['amount'])
#
#         currency = ET.SubElement(order, 'currency')
#         currency.text = str(item['currency'])
#
#     tree = ET.ElementTree(root)
#     ET.indent(tree)
#     tree.write(filename, encoding='utf-8')
#
# orders = [
#     {"id": 101, "amount": 250, "currency": "USD"},
#     {"id": 102, "amount": 400, "currency": "EUR"}
# ]
#
# export_orders('files/xml/orders.xml', orders)
#
# with open('files/xml/orders.xml', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_contacts(filename: str, contacts: list[dict]) -> None:
#     root = ET.Element('contacts')
#
#     for item in contacts:
#         contact = ET.SubElement(root, 'contact')
#         for key, value in item.items():
#             name = ET.SubElement(contact, key)
#             name.text = value
#
#     tree = ET.ElementTree(root)
#     ET.indent(tree)
#     tree.write(filename, encoding='utf-8')
#
# contacts = [
#     {"name": "Anna", "phone": "+374777777", "city": "Yerevan"},
#     {"name": "Leo", "phone": "+374999999", "city": "Gyumri"}
# ]
#
# export_contacts("files/xml/contacts1.xml", contacts)
#
# with open('files/xml/contacts1.xml', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def save_errors(filename: str, errors: list) -> None:
#     #корневой тег
#     root = ET.Element('errors')
#
#     for error_name in errors:
#         error = ET.SubElement(root, 'error')
#         error.text = error_name
#
#     tree = ET.ElementTree(root)
#     ET.indent(tree)
#     tree.write(filename, encoding='utf-8')
#
# errors = [
#     "Ошибка доступа: /var/data",
#     "Слишком длинный путь к файлу",
#     "Кодировка не поддерживается: cp1251",
#     "Database connection lost",
#     "Invalid token",
#     "Too many requests",
#     "Cache miss"
# ]
#
# save_errors('files/xml/errors2.xml', errors)
#
# with open('files/xml/errors2.xml', 'r', encoding='utf-8') as f:
#     print(f.read())
#
# # errors = [
# #     "File not found",
# #     "Timeout error",
# #     "Permission denied"
# # ]
# #
# # save_errors('files/xml/errors1.xml', errors)
# #
# # with open('files/xml/errors1.xml', 'r', encoding='utf-8') as f:
# #     print(f.read())
'---------------------------------------------'
# def average_fare_by_passenger_type(filename: str) -> dict:
#     res = {}
#     # Парсим xml файл
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     # проходим по номерам рейсов
#     for flight in root.findall('flight'):
#         # проходим по пассажирам:
#         for passengers in flight.findall('passengers'):
#             for passenger in passengers.findall('passenger'):
#                 key = passenger.attrib['type']
#                 for fare in passenger.findall('fare'):
#                     for base in fare.findall('base'):
#                         for tax in fare.findall('tax'):
#                             cost = float(base.text) + float(tax.text)
#                             res.setdefault(key, [])
#                             res[key].append(cost)
#
#     for key, value in res.items():
#         res[key] = round(sum(value) / len(value), 2)
#
#     return res
#
# print(average_fare_by_passenger_type('files/xml/flights_2.xml'))
'---------------------------------------------'
# def top_sellers(filename: str) -> list[tuple]:
#     res = {}
#     res_tuple = []
#
#     # Парсим xml файл
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     # обходим seller
#     for seller in root.findall('seller'):
#         id_seller = seller.attrib['id']
#
#         #обходим продукт product
#         for product in seller.findall('product'):
#             sku_product = product.attrib['sku']
#
#             #обходим review берем из атрибута оценку и ведем подсчет количества ревьшек
#             for reviews in product.findall('reviews'):
#                 for review in reviews.findall('review'):
#                     res.setdefault(id_seller, [0, []])
#                     res[id_seller][0] += 1
#                     res[id_seller][1].append(int(review.attrib['rating']))
#
#     for key, value in res.items():
#         av_rating = sum(value[1]) / len(value[1])
#         if value[0] >= 10 and av_rating >= 4.5:
#             res_tuple.append((key, round(sum(value[1])/len(value[1]),2), value[0]))
#
#     return res_tuple
#
# print(top_sellers('files/xml/market_1.xml'))
'---------------------------------------------'
# def average_distance_by_city(filename: str) -> dict:
#     res = {}
#     # Парсим xml файл
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     for trip in root.findall('trip'):
#         key = trip.find('city').text
#         res.setdefault(key, [])
#         res[key].append(int(trip.find('distance').text))
#
#     for key, values in res.items():
#         res[key] = sum(values) / len(values)
#
#     return res
#
# print(average_distance_by_city('files/xml/trips_1.xml'))
'---------------------------------------------'
# def get_heaviest_route(filename):
#
#     res = {}
#
#     # Парсим xml файл
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     for route in root.findall('route'):
#         key = route.find('from').text + route.find('to').text
#         res.setdefault(key, [route.find('from').text, route.find('to').text, 0])
#         res[key][2] += int(route.find('weight').text)
#
#     max_weight = 0
#     res_max = []
#     for key, value in res.items():
#         if value[2] > max_weight:
#             res_max = value
#             max_weight = value[2]
#
#     return tuple(res_max)
#
# print(get_heaviest_route('files/xml/routes_1.xml'))
'---------------------------------------------'
# def calculate_revenue(filename: str) -> dict:
#
#     res = {}
#
#     # Парсим xml файл
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     for booking in root.findall('booking'):
#         cost = int(booking.find('nights').text) * int(booking.find('price').text)
#         res.setdefault(booking.find('hotel').text, 0)
#         res[booking.find('hotel').text] += int(cost)
#
#     return res
#
# print(calculate_revenue('files/xml/bookings_1.xml'))
'---------------------------------------------'
# def print_courses_by_level(filename):
#     # Парсим XML-файл
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     # Проходим по всем категориям
#     for category in root.findall('category'):
#         category_name = category.get('name')
#         print(f"Категория: {category_name}")
#
#         # Проходим по всем уровням внутри категории
#         for level in category.findall('level'):
#             level_value = level.get('value')
#             print(f"  Уровень: {level_value}")
#
#             # Проходим по всем курсам внутри уровня
#             for course in level.findall('course'):
#                 title = course.find('title').text
#                 print(f"    - {title}")
#
# print_courses_by_level('files/xml/courses_2.xml')
'---------------------------------------------'
# def count_tags(filename: str) -> dict:
#
#     res = {}
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     for child in root.iter():
#         res.setdefault(child.tag, 0)
#         res[child.tag] += 1
#
#     return res
#
# print(count_tags('files/xml/test_1.xml'))
'---------------------------------------------'
# def get_active_courses(filename: str) -> None:
#
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     for course in root.iter('course'):
#         if course.attrib['active'].lower() == 'true':
#             print(f'{course.findall('title')[0].text} — {course.findall('duration')[0].text}')
#
# get_active_courses('files/xml/courses_2.xml')
'---------------------------------------------'
# def get_child_tags(filename: str, parent_tag: str) -> list:
#
#     res = []
#
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     for child in root.findall(parent_tag):
#         for t in child:
#             res.append(t.tag)
#     return res
#
# print(get_child_tags('files/xml/shops.xml', 'product'))
'---------------------------------------------'
# def get_child_tags(filename: str) -> list:
#
#     res= []
#
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     for child in root:
#         res.append(child.tag)
#
#     return res
#
# print(get_child_tags('files/xml/products.xml'))
'---------------------------------------------'
# def get_root_tag(filename: str) -> str:
#
#     tree = ET.parse(filename)
#     root = tree.getroot()
#
#     return root.tag
#
# print(get_root_tag('files/xml/courses.xml'))
'---------------------------------------------'
# # Код с рекуцрчсией, охуенный. Для любой степени ыложенности
# def rec_dict(item, file, otstup = 4):
#     indent = ' ' * otstup
#     for key, value in item.items():
#         if isinstance(value, dict):
#             file.write(f'{indent}<{key}>\n')
#             rec_dict(value, file, otstup + 2)
#             file.write(f'{indent}</{key}>\n')
#         elif isinstance(value, list):
#             file.write(f'{indent}<{key}>\n')
#             for val in value:
#                 file.write(f'{" " * (otstup+2)}<{key[:-1]}>{val}</{key[:-1]}>\n')
#             file.write(f'{indent}</{key}>\n')
#         else:
#             file.write(f'{indent}<{key}>{value}</{key}>\n')
#     return None
#
# def dict_to_xml(data: dict) -> None:
#     with open('files/xml/students.xml', 'w', encoding='utf-8') as file:
#         file.write(f'<Students>\n')
#         for s in data['Students']:
#             file.write(f'  <Student>\n')
#             rec_dict(s, file)
#             file.write(f'  </Student>\n')
#         file.write(f'</Students>\n')
#
# ## Код подобраный под задачи
# # def dict_to_xml(data: dict) -> None:
# #     with open('files/xml/students.xml', 'w', encoding='utf-8') as file:
# #         file.write(f'<Students>\n')
# #         for s in data['Students']:
# #             file.write(f'{' '*2}<Student>\n')
# #             for key, value in s.items():
# #                 if isinstance(value, list):
# #                     file.write(f'{' '*4}<{key}>\n')
# #                     for v in value:
# #                         file.write(f'{' '*6}<{key[:-1]}>{v}</{key[:-1]}>\n')
# #                     file.write(f'{' ' * 4}</{key}>\n')
# #                 elif isinstance(value, dict):
# #                     file.write(f'{' '*4}<{key}>\n')
# #                     for k, v in value.items():
# #                         if isinstance(v, list):
# #                             file.write(f'{' '*6}<{k}>\n')
# #                             for val in v:
# #                                 file.write(f'{' '*8}<{k[:-1]}>{val}</{k[:-1]}>\n')
# #                             file.write(f'{' ' * 6}</{k}>\n')
# #                         elif isinstance(v, dict):
# #                             file.write(f'{' '*6}<{k}>\n')
# #                             for keys, values in v.items():
# #                                 if isinstance(values, dict):
# #                                     file.write(f'{' '*8}<{keys}>\n')
# #                                     for kal, val in values.items():
# #
# #                                         if isinstance(val, list):
# #                                             file.write(f'{' ' * 10}<{kal}>\n')
# #                                             for vv in val:
# #                                                 file.write(f'{' '*12}<{kal[:-1]}>{vv}</{kal[:-1]}>\n')
# #                                             file.write(f'{' ' * 10}</{kal}>\n')
# #                                         else:
# #                                             file.write(f'{' '*10}<{kal}>{val}</{kal}>\n')
# #                                     file.write(f'{' ' * 8}</{keys}>\n')
# #                                 else:
# #                                     file.write(f'{' '*8}<{keys}>{values}</{keys}>\n')
# #                             file.write(f'{' ' * 6}</{k}>\n')
# #                         else:
# #                             file.write(f'{' '*6}<{k}>{v}</{k}>\n')
# #                     file.write(f'{' ' * 4}</{key}>\n')
# #                 else:
# #                     file.write(f'{' ' * 4}<{key}>{value}</{key}>\n')
# #             file.write(f'{' '*2}</Student>\n')
# #         file.write(f'</Students>')
# #
# # data = {
# #     "Students": [
# #         {
# #             "Имя": "Алиса",
# #             "Возраст": "25",
# #             "Контакты": {
# #                 "Email": "alice@mail.com",
# #                 "Телефон": "+31-000-00-00"
# #             },
# #             "Курсы": ["Python", "SQL"]
# #         }
# #     ]
# # }
#
# # data = {
# #     "Students": [
# #         {
# #             "Имя": "Neo",
# #             "Возраст": "29",
# #             "Профиль": {
# #                 "Город": "Zion",
# #                 "Навыки": ["Focus", "Dodge", "Jump"],
# #                 "Контакты": {
# #                     "Email": "neo@matrix.io",
# #                     "Телефон": "unknown"
# #                 }
# #             },
# #             "Курсы": ["Python"]
# #         }
# #     ]
# # }
#
# data = {
#     "Students": [
#         {
#             "Имя": "Neo",
#             "Возраст": "29",
#             "Профиль": {
#                 "Город": "Zion",
#                 "Статус": "Chosen One",
#                 "Контакты": {
#                     "Email": "neo@matrix.io",
#                     "Резервные": {
#                         "Email": "backup@matrix.io",
#                         "Телефоны": ["unknown", "red-phone"]
#                     }
#                 },
#                 "Навыки": ["Focus", "Dodge", "Jump"]
#             },
#             "Курсы": ["Python", "Linux", "Networking"]
#         },
#         {
#             "Имя": "Trinity",
#             "Возраст": "28",
#             "Профиль": {
#                 "Город": "Matrix",
#                 "Контакты": {
#                     "Email": "trinity@matrix.io"
#                 }
#             },
#             "Хобби": ["мотоциклы", "стрельба"],
#             "Проекты": ["Matrix", "Zion"]
#         }
#     ]
# }
#
# dict_to_xml(data)
#
# with open('files/xml/students.xml', 'r', encoding='utf-8') as file:
#     print(file.read())
'---------------------------------------------'
# def dict_to_xml(data: dict) -> None:
#     with open('files/xml/students.xml', 'w', encoding='utf-8') as file:
#         file.write(f'<Students>\n')
#         for s in data['Students']:
#             file.write(f'  <Student>\n')
#             for k,v in s.items():
#                 if isinstance(v, list):
#                     file.write(f'    <{k}>\n')
#                     for i in v:
#                         file.write(f'      <{k[:-1]}>{i}</{k[:-1]}>\n')
#                     file.write(f'    </{k}>\n')
#                 else:
#                     file.write(f'    <{k}>{v}</{k}>\n')
#             file.write(f'  </Student>\n')
#         file.write(f'</Students>\n')
#
# data = {
#     "Students": [
#         {"Имя": "Алиса", "Возраст": "25", "Курсы": ["Python", "SQL", "Git"]}
#     ]
# }
#
# dict_to_xml(data)
#
# with open('files/xml/students.xml', 'r', encoding='utf-8') as file:
#     print(file.read())
'---------------------------------------------'
# def dict_to_xml(data: dict) -> None:
#     with open('files/xml/students.xml', 'w', encoding='utf-8') as file:
#         file.write(f'<Students>\n')
#         for s in data['Students']:
#             file.write(f'  <Student>\n')
#             for k, v in s.items():
#                 file.write(f'    <{k}>{v}</{k}>\n')
#             file.write(f'  </Student>\n')
#         file.write(f'</Students>\n')
#
# data = {
#     "Students": [
#         {"Имя": "Алиса", "Возраст": "25"},
#         {"Имя": "Борис", "Возраст": "27"}
#     ]
# }
#
# dict_to_xml(data)
#
# with open("files/xml/students.xml", "r", encoding="utf-8") as file:
#     print(file.read())
'---------------------------------------------'
# def dict_to_xml(data: dict) -> None:
#     with open('files/xml/student.xml', 'w', encoding='utf-8') as file:
#         for key, value in data.items():
#             file.write(f'<{key}>\n')
#             for k, v in value.items():
#                 file.write(f'  <{k}>{v}</{k}>\n')
#             file.write(f'</{key}>')
#
# student = {
#     "Student": {
#         "Имя": "Алиса",
#         "Возраст": "25"
#     }
# }
#
# dict_to_xml(student)
#
# with open("files/xml/student.xml", "r", encoding="utf-8") as file:
#     print(file.read())
'---------------------------------------------'
# def get_login_hash(login: str) -> int:
#     return abs(hash(login))
#
# def save_state(users: dict):
#     hash_login = get_login_hash(users['login'])
#     with open(f'files/csv/save_game_{hash_login}.pkl', 'wb') as file:
#         pickle.dump(users['state'], file)
#
# def load_state(login_text: str):
#     login_hash = get_login_hash(login_text)
#     try:
#         with open(f'files/csv/save_game_{login_hash}.pkl', 'rb') as file:
#             state = pickle.load(file)
#             return state
#     except:
#         return {}
#
# user = {
#     "login": "SleepyDragon",
#     "state": {"location": (10, 20), "inventory": ["apple"], "stats": {"hp": 90}}
# }
#
# save_state(user)
# restored = load_state("SleepyDragon")
# print(restored)
#
# print(load_state("ChillPenguin"))
#
# user = {
#     "login": "skrip_kresla",
#     "state": {
#         "location": (5, 10),
#         "inventory": ["apple", "stick"],
#         "stats": {"hp": 95, "mana": 30}
#     }
# }
#
# save_state(user)
#
# hash_value = get_login_hash('skrip_kresla')
#
# with open(f"files/csv/save_game_{hash_value}.pkl", "rb") as file:
#     print(file.read())
'---------------------------------------------'
# def load_and_describe_function(filename: str) -> None:
#     with open(filename, 'rb') as f:
#         loaded_function = pickle.load(f)
#         print(f'Имя функции: {loaded_function.__name__}')
#         if loaded_function.__doc__:
#             print(f'Описание: {loaded_function.__doc__.strip()}')
#         else:
#             print('Описание: Нет описания (docstring)')
# # В Степике работает, так как там функции определны
# load_and_describe_function('files/csv/add.pkl')
'---------------------------------------------'
# def load_hobbies(filename: str) -> list:
#     with open(filename, 'rb') as f:
#         loaded = pickle.load(f)
#         return loaded
#
# print(load_hobbies('files/csv/their_hobbies.pkl'))
# '---------------------------------------------'
# def save_hobbies(filename: str, hobbies: list[str]) -> None:
#     with open(filename, 'wb') as f:
#         pickle.dump(hobbies, f)
#
# hobbies = ["Теннис", "Программирование", "Чтение"]
# save_hobbies("files/csv/their_hobbies.pkl", hobbies)
#
# with open('files/csv/their_hobbies.pkl', 'rb') as f:
#     print(f.read())
'---------------------------------------------'
# def export_order_stats(catalog_filename: str, orders_filename: str) -> None:
#     header = ['product', 'quantity_sold', 'total_revenue', 'revenue_share']
#     res = {}
#     res_csv = []
#     total = 0
#     with open(catalog_filename, 'r', encoding='utf-8') as catalog, open(orders_filename, 'r', encoding='utf-8') as orders:
#         catalog_reader = csv.DictReader(catalog)
#         orders_reader = csv.DictReader(orders)
#
#         for row in orders_reader:
#             res.setdefault(row['product_id'], {'product':'', 'quantity_sold': 0, 'total_revenue':1, 'revenue_share':[]})
#             res[row['product_id']]['quantity_sold'] += int(row['quantity'])
#
#         for row in catalog_reader:
#             res[row['id']]['product'] = row['product']
#             res[row['id']]['total_revenue'] = res[row['id']]['quantity_sold'] * int(row['price'])
#             total += res[row['id']]['total_revenue']
#
#         for k, v in res.items():
#             v['revenue_share'] = round(v['total_revenue'] / total * 100, 1)
#             res_csv.append(v)
#
#     with open('files/csv/order_stats.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=header)
#         writer.writeheader()
#         writer.writerows(sorted(res_csv, key=lambda x: x['product']))
#
# export_order_stats('files/csv/catalog.csv', 'files/csv/orders.csv')
#
# with open('files/csv/order_stats.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_catalog(data: list[dict], mapping_filename: str, output_filename: str) -> None:
#     f_name = []
#     res = [{} for _ in range(len(data))]
#     with open(mapping_filename, 'r', encoding='utf-8') as f:
#         header = json.load(f)
#     for row in range(len(data)):
#         for k,v in data[row].items():
#             if k in header:
#                 res[row][header[k]] = v
#
#         for k,v in data[row].items():
#             if k not in header:
#                 res[row][k] = v
#
#     for key in res[0].keys():
#         f_name.append(key)
#
#     with open(output_filename, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=f_name)
#         writer.writeheader()
#         writer.writerows(res)
#
# products = [
#     {"Название": "Чай зелёный", "Цена": 120, "Категория": "Напитки", "Склад": "A1"},
#     {"Название": "Мед натуральный", "Цена": 340, "Категория": "Продукты"},
#     {"Название": "Кофе арабика", "Цена": 290, "Категория": "Напитки", "Склад": "B3"}
# ]
#
# # export_catalog(products, 'files/csv/mapping.json',
# #                'files/csv/catalog_en.csv')
#
# export_catalog(products, 'files/csv/part_mapping.json',
#                'files/csv/catalog_en.csv')
#
# with open('files/csv/catalog_en.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_columns(products: list[dict], filename:str, columns:list[str]) -> None:
#     count = 0
#     for column in columns:
#         if column in products[0]:
#             count += 1
#
#     if count > 0:
#         with open(filename, 'w', newline='', encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore', restval="N/A")
#             writer.writeheader()
#             writer.writerows(products)
#     else:
#         print('Ни одна из указанных колонок не найдена.')
#
# catalog = [
#     {"product": "Чай", "category": "Напитки", "price": 100},
#     {"product": "Кофе", "category": "Напитки", "price": 200},
#     {"product": "Печенье", "category": "Сладости", "price": 150}
# ]
#
# export_columns(catalog, 'files/csv/selected.csv', ["product", "price"])
#
# try:
#     with open('files/csv/selected.csv', 'r', encoding='utf-8') as f:
#         print(f.read())
# except FileNotFoundError:
#     print('Файл selected.csv не обнаружен')
'---------------------------------------------'
# def export_column(products:list[dict], filename:str, column_name:str) -> None:
#     if column_name in products[0]:
#         with open(filename, 'w', newline='', encoding='utf-8') as file:
#             writer = csv.DictWriter(file, fieldnames=[column_name], extrasaction='ignore')
#             writer.writeheader()
#             writer.writerows(products)
#     else:
#         print(f'Колонка {column_name} отсутствует в данных.')
#
# # catalog = [
# #     {"product": "Чай", "category": "Напитки", "price": 100},
# #     {"product": "Кофе", "category": "Напитки", "price": 200},
# #     {"product": "Печенье", "category": "Сладости", "price": 150}
# # ]
#
# catalog = [
#     {"product": "Чай", "category": "Напитки", "price": 100},
#     {"product": "Кофе", "category": "Напитки", "price": 200},
#     {"product": "Сок", "category": "Напитки", "price": 150},
#     {"product": "Печенье", "category": "Сладости", "price": 90},
#     {"product": "Шоколад", "category": "Сладости", "price": 250},
#     {"product": "Сахар", "category": "Продукты", "price": 55},
#     {"product": "Соль", "category": "Продукты", "price": 30},
# ]
#
# # export_column(catalog, 'files/csv/price.csv', 'price')
# export_column(catalog, 'files/csv/quantity.csv.csv', 'quantity')
#
# # with open('files/csv/price.csv', 'r', encoding='utf-8') as f:
# #     print(f.read())
#
# try:
#     with open('files/csv/quantity.csv', 'r', encoding='utf-8') as f:
#         print(f.read())
# except FileNotFoundError:
#     print('Файл quantity.csv не обнаружен')
'---------------------------------------------'
# def save_catalog_to_csv(catalog, filename):
#     f_names = [key for key in catalog[0].keys()]
#
#     with open(filename, 'w', encoding='utf-8', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=f_names)
#         writer.writeheader()
#         writer.writerows(catalog)
#
# catalog = [
#     {"product": "Чай", "category": "Напитки", "price": 100},
#     {"product": "Кофе", "category": "Напитки", "price": 200},
#     {"product": "Печенье", "category": "Сладости", "price": 150}
# ]
#
# save_catalog_to_csv(catalog, 'files/csv/products.csv')
#
# with open('files/csv/products.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_team_stats(filename: str) -> None:
#     result = {}
#     with open(filename, 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         next(reader)
#
#         for row in reader:
#             result.setdefault(row[0], {'Команда':row[0], 'Матчи':0,'Победы':0, 'Поражения':0, 'Ничьи':0, 'Забито':0,
#                                        'Пропущено':0})
#             result.setdefault(row[1],
#                               {'Команда': row[1], 'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Ничьи': 0, 'Забито': 0,
#                                'Пропущено': 0})
#             #добавляем команде и сопернику по 1 игре
#             result[row[0]]['Матчи'] += 1
#             result[row[1]]['Матчи'] += 1
#             #пропущенные и забитые голы команды и соперника
#             result[row[0]]['Забито'] += int(row[2])
#             result[row[0]]['Пропущено'] += int(row[3])
#             result[row[1]]['Забито'] += int(row[3])
#             result[row[1]]['Пропущено'] += int(row[2])
#             #условие, если команда выиграла соперника
#             if int(row[2]) > int(row[3]):
#                 result[row[0]]['Победы'] += 1
#                 result[row[1]]['Поражения'] += 1
#             # условие, если команда проиграла сопернику
#             elif int(row[2]) < int(row[3]):
#                 result[row[0]]['Поражения'] += 1
#                 result[row[1]]['Победы'] += 1
#             else:
#                 result[row[0]]['Ничьи'] += 1
#                 result[row[1]]['Ничьи'] += 1
#
#     #создаем итоговый csv файл
#     with open('files/csv/team_stats.csv', 'w', encoding='utf-8') as f:
#         writer = csv.writer(f, delimiter=',')
#         writer.writerow(['Команда', 'Матчи', 'Победы', 'Поражения', 'Ничьи', 'Забито', 'Пропущено', 'Разница'])
#         for key, value in sorted(result.items()):
#             writer.writerow([value['Команда'], value['Матчи'], value['Победы'], value['Поражения'],
#                              value['Ничьи'], value['Забито'], value['Пропущено'], value['Забито']-value['Пропущено']])
#
# export_team_stats('files/csv/match_results.csv')
#
# with open('files/csv/team_stats.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_summary(filenames: list[str], output_filename: str) -> None:
#     customers = {}
#     res_csv = {}
#     for filename in filenames:
#         with open(f'files/csv/salary/{filename}', 'r', encoding='utf-8') as f:
#             data = json.load(f)
#             if len(data) > 0:
#                 customers.setdefault(filename.replace('.json', ''), [])
#                 for row in data:
#                     customers[filename.replace('.json', '')].append(row)
#
#     for k, v in customers.items():
#         res_csv.setdefault(k, {'department':'', 'employees':[], 'average_salary':[]})
#         for row in v:
#             res_csv[k]['department'] = k
#             res_csv[k]['employees'].append(row['name'])
#             res_csv[k]['average_salary'].append(float(row['salary']))
#
#     with open(f'files/csv/salary/{output_filename}', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f, delimiter=',')
#         writer.writerow(['department', 'employees', 'average_salary', 'min_salary', 'max_salary'])
#         for k, v in sorted(res_csv.items()):
#             writer.writerow([k, len(v['employees']), round(sum(v['average_salary'])/len(v['average_salary']), 2), round(min(v['average_salary']), 2), round(max(v['average_salary']), 2)])
#
# export_summary(['it.json', 'hr.json', 'sales.json', 'sales2.json'], 'stat_depatrments.csv')
#
# with open('files/csv/salary/stat_depatrments.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_students_to_json(students_file_name, enrollments_file_name) -> None:
#     students = {}
#     res_json = []
#     with open(students_file_name, 'r', encoding='utf-8') as s_f, open(enrollments_file_name, 'r', encoding='utf-8') as e_f:
#         s_reader = csv.reader(s_f, delimiter=':')
#         e_reader = csv.reader(e_f, delimiter=':')
#         next(s_reader)
#         next(e_reader)
#
#         for s_row in s_reader:
#             students.setdefault(s_row[0], {'id': int(s_row[0]), 'name': s_row[1], 'courses': []})
#         for e_row in e_reader:
#             students[e_row[0]]['courses'].append(e_row[1])
#
#     for k, v in students.items():
#         v['courses'] = sorted(v['courses'])
#         res_json.append(v)
#
#     with open('files/csv/student_courses.json', 'w', encoding='utf-8') as f:
#         json.dump(res_json, f, ensure_ascii=False, indent=2)
#
# export_students_to_json('files/csv/students.csv', 'files/csv/enrollments.csv')
#
# with open('files/csv/student_courses.json', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def merge_student_courses(students_file_name: str, enrollments_file_name: str) -> None:
#     students_courses = {}
#
#     with open(students_file_name, 'r', encoding='utf-8') as s_f, open(enrollments_file_name, 'r', encoding='utf-8') as e_f:
#         s_reader = csv.reader(s_f, delimiter=':')
#         next(s_reader)
#         e_reader = csv.reader(e_f, delimiter=':')
#         next(e_reader)
#
#         for s in s_reader:
#             students_courses.setdefault(s[0], {'name': "", 'courses':[]})
#             students_courses[s[0]]['name'] = s[1]
#
#         for e in e_reader:
#             students_courses[e[0]]['courses'].append(e[1])
#
#     with open('files/csv/student_courses.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f, delimiter=":")
#         writer.writerow(['name', 'courses'])
#
#         for k, v in students_courses.items():
#             if len(v['courses']) > 0:
#                 writer.writerow([v['name'], ', '.join(sorted(v['courses']))])
#             else:
#                 writer.writerow([v['name'], 'Пока нет направлений обучения'])
#
# merge_student_courses('files/csv/students.csv', 'files/csv/enrollments.csv')
#
# with open('files/csv/student_courses.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_category_summary(filename: str) -> None:
#     res = {}
#     with open(filename, 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         next(reader)
#         for row in reader:
#             res.setdefault(row[2], {'unique_customers':[], 'total_sales':[]})
#             res[row[2]]['unique_customers'].append(row[0])
#             res[row[2]]['total_sales'].append(int(row[3]))
#     with open('files/csv/category_summary.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['category', 'total_sales' ,'unique_customers'])
#         for k, v in sorted(res.items(), key=lambda x: x[0], reverse=False):
#             writer.writerow([k, sum(v['total_sales']), len(set(v['unique_customers']))])
#
# export_category_summary('files/csv/purchases.csv')
#
# with open('files/csv/category_summary.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_genre_summary(filename: str) -> None:
#     res = {}
#     res_csv = []
#     #обработка входящего файла
#     with open(filename, 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         next(reader)
#         #новый словарь с нужными данными
#         for i in reader:
#             res.setdefault(i[1], {'title':[], 'duration':[], 'rating':[]})
#             res[i[1]]['title'].append(i[0])
#             res[i[1]]['duration'].append(float(i[2]))
#             res[i[1]]['rating'].append(float(i[3]))
#
#     for k, v in sorted(res.items()):
#         res_csv.append([k, len(v['title']), round(sum(v['rating'])/len(v['rating']),1), round(sum(v['duration'])/len(v['duration']), 1)])
#
#     with open('files/csv/genre_summary.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f, delimiter=',')
#         writer.writerow(['genre','total_movies','average_rating','average_duration'])
#         writer.writerows(sorted(res_csv, key=lambda x: (-x[2], x[0])))
#
# export_genre_summary('files/csv/movies2.csv')
#
# with open('files/csv/genre_summary.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_user_stats(filename: str) -> None:
#     res = {}
#     res_csv = [['user', 'total_reviews', 'average_rating']]
#     with open(filename, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#     for i in data:
#         res.setdefault(i['user'], {'rating': [], 'comment': []})
#         res[i['user']]['rating'].append(i['rating'])
#         res[i['user']]['comment'].append(i['comment'])
#
#     for k, v in sorted(res.items()):
#         res_csv.append([k, len(v['comment']), round(sum(v['rating']) / len(v['rating']), 1)])
#
#     with open('files/csv/user_stats.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f, delimiter=',')
#         writer.writerows(res_csv)
#
# export_user_stats('files/csv/reviews2.json')
#
# with open('files/csv/user_stats.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def merge_catalogs(products_filename, prices_filename) -> None:
#     prod_list = []
#     price_list = {}
#     merge_list = []
#     with open(products_filename, 'r', encoding='utf-8') as prod, open(prices_filename, 'r', encoding='utf-8') as price:
#         reader_prod = csv.reader(prod)
#         reader_price = csv.reader(price)
#         merge_list.append(next(reader_prod) + next(reader_price)[1].split())
#         for row in reader_prod:
#             prod_list.append(row)
#         for row in reader_price:
#             price_list[row[0]] = row[1]
#
#     prices = [key for key in price_list]
#
#     for i in range(len(prod_list)):
#         if prod_list[i][0] in prices:
#             merge_list.append(prod_list[i] + price_list[prod_list[i][0]].split())
#
#     with open('files/csv/merged.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f)
#         for row in merge_list:
#             writer.writerow(row)
#
# #merge_catalogs('files/csv/products.csv', 'files/csv/prices.csv')
# #merge_catalogs('files/csv/products3.csv', 'files/csv/prices3.csv')
# merge_catalogs('files/csv/products2.csv', 'files/csv/prices2.csv')
#
# with open('files/csv/merged.csv', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def save_matrix_to_csv(matrix: list[list], filename: str) -> None:
#     with open(filename, 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f)
#         for row in matrix:
#             writer.writerow(row)
#
# mtrx = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# f_name = "files/csv/matrix.csv"
#
# save_matrix_to_csv(mtrx, f_name)
#
# with open("files/csv/matrix.csv", 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def print_movies(filename: str) -> None:
#     with open(filename, 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         next(reader)
#         for row in reader:
#             title, genre, duration, rating = row
#             print(f'Фильм: {title} | Жанр: {genre} | Длительность: {duration} мин | Рейтинг: {rating}')
#
# print_movies('files/csv/movies1.csv')
'---------------------------------------------'
# def print_columns(filename: str, columns: list[str]) -> None:
#     res_list = [[] for _ in range(len(columns))]
#     count = 0
#     na = 0
#     for column in columns:
#         with open(filename, 'r', encoding='utf-8') as file:
#             reader = csv.reader(file)
#             cols = next(reader)
#             if column in cols:
#                 for row in reader:
#                     res_list[count].append(row[cols.index(column)])
#             else:
#                 na += 1
#                 for row in reader:
#                     res_list[count].append("N/A")
#             count += 1
#     if na == len(columns):
#         print('Указанные колонки не найдены.')
#     else:
#         transported = list(zip(*res_list))
#         for row in transported:
#             print(';'.join(row))
#
# print_columns('files/csv/library_books.csv', ["fвтор", ['her'],"hейтинг"])
'---------------------------------------------'
# def print_column_values(filename: str, column_name: str) -> None:
#     with open(filename, 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         column = next(reader)
#         if column_name in column:
#             for row in reader:
#                 print(row[column.index(column_name)])
#         else:
#             print(f'Колонка "{column_name}" не найдена.')
#
# print_column_values('files/csv/library_books.csv', 'Жанр')
'---------------------------------------------'
# def print_book_titles(filename: str) -> None:
#     with open(filename, 'r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             print(row[1])
#
# print_book_titles('files/csv/books.csv')
'---------------------------------------------'
# def read_csv(filename: str, show_header=True, limit=None) -> None:
#     with open(filename, 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         if show_header:
#             if limit is not None:
#                 for i in range(limit+1):
#                     print(next(reader))
#             else:
#                 for row in reader:
#                     print(row)
#         else:
#             next(reader)
#             if limit is not None:
#                 for i in range(limit):
#                     print(next(reader))
#             else:
#                 for row in reader:
#                     print(row)
# read_csv('files/csv/books.csv', show_header=False, limit=2)
'---------------------------------------------'
# with open("files/csv/users.csv", 'r', encoding="utf-8") as f:
#     reader = csv.reader(f)
#     # for line in reader:
#     #     print(line)
#     next(reader)
#     count = 0
#     for row in reader:
#         print(row)
#         if "" in row:
#             count += 1
#     print(count)
'---------------------------------------------'
# with open('files/csv/cafe_orders.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_stats(*args) -> None:
#     total_comments = 0
#     total_likes = 0
#     total_users = 0
#     total_categories = 0
#     users = dict()
#     users_json = []
#     #Проводим десереализацию входящих json файлов
#     for arg in args:
#         #Количество обработанных файлов
#         total_categories += 1
#         with open(arg, 'r', encoding='utf-8') as f:
#             for line in json.load(f):
#                 # Количество комментариев
#                 total_comments += 1
#                 # Количество лайков
#                 total_likes += line['likes']
#                 # список уникальных юзеров с количеством их комментариев и лайков
#                 users.setdefault(line['user'], {'comments': 0, 'likes': 0})
#                 users[line['user']]['comments'] += 1
#                 users[line['user']]['likes'] += line['likes']
#     #Сортируем словарь по убыванию лайков и по алфавиту, если лайки одинаковые и
#     # создаем список user_json с требуемыми задачей значениями для users
#     for key, value in sorted(users.items(), key=lambda item: (item[1]['likes'], item[0]), reverse=True):
#         #считаем уникальныъ юзеров
#         total_users += 1
#         #создаем словарь с данными для последующей записи в json файл в ключ users
#         users_json.append({'user': key, 'comments': value['comments'], 'likes': value['likes']})
#
#     # финальный словарь для записи в json файл
#     res = {
#         "total_comments": total_comments,
#         "total_likes": total_likes,
#         "total_users": total_users,
#         "total_categories": total_categories,
#         "users": users_json
#     }
#
#     with open('files/json/exp_com_by_cat/stats.json', 'w', encoding='utf-8') as f:
#         json.dump(res, f, ensure_ascii=False, indent=2)
#
# export_stats('files/json/exp_com_by_cat/python_comments.json', 'files/json/exp_com_by_cat/javascript_comments.json')
#
# with open('files/json/exp_com_by_cat/stats.json', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_poll_results(*args):
#     new_dict = dict()
#     json_dict = dict()
#     json_file = []
#     sum_point = 0
#     #создаем словарь из язык-сумма баллов. Считаем сумму всех баллов для последующего подсчета процентов
#     for arg in args:
#         for key, value in arg.items():
#             new_dict.setdefault(key, 0)
#             new_dict[key] += value
#             sum_point += value
#     #Переворачиваем словарь и создаем с одинаковыми баллами языки
#     for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0])):
#         json_dict.setdefault(value, []).append(key)
#     #делаем структуру данных для последующей записи в json, сортировка по убыванию
#     for key, value in sorted(json_dict.items(), reverse=True):
#         json_file.append({"languages":value,
#                           "votes": key,
#                           "percent": key/sum_point*100})
#     #записываем данные в json файл
#     with open('files/json/results.json', 'w', encoding='utf-8') as f:
#         json.dump(json_file, f, ensure_ascii=False, indent=2)
#
# export_poll_results(
#     {"Python": 21, "JavaScript": 25, "C++": 10},
#     {"Python": 12, "C++": 15, "Java": 17}
# )
#
# with open('files/json/results.json', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_comments_by_category(comments) -> None:
#     res = {}
#     res_dict = {}
#
#     for comment in comments:
#         res.setdefault(comment['category'], []).append(comment)
#     for k, v in res.items():
#         for comment in v:
#             del comment['category']
#         res_dict[k] = sorted(v, key=lambda x: x['likes'], reverse=True)
#
#     for k, v in res_dict.items():
#         with open('files/json/exp_com_by_cat/' + k.lower() + '_comments.json', 'w', encoding='utf-8') as f:
#             json.dump(v, f, ensure_ascii=False, indent=2)
#
# comments = [
#     {"user": "Артем", "text": "Python — сила!", "likes": 15, "category": "Python"},
#     {"user": "Мария", "text": "Обожаю JavaScript", "likes": 10, "category": "JavaScript"},
#     {"user": "John", "text": "JS проще, чем C++", "likes": 7, "category": "JavaScript"},
#     {"user": "Alex", "text": "C++ сложный, но мощный", "likes": 12, "category": "C++"}
# ]
#
# export_comments_by_category(comments)
# print('Python'.center(12, '-'))
# with open('files/json/exp_com_by_cat/python_comments.json', 'r', encoding='utf-8') as f:
#     print(f.read())
#
# print('JavaScript'.center(12, '-'))
# with open('files/json/exp_com_by_cat/javascript_comments.json', 'r', encoding='utf-8') as f:
#     print(f.read())
#
# print('C++'.center(12, '-'))
# with open('files/json/exp_com_by_cat/c++_comments.json', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_grouped_comments(comments: list[dict], filename) -> None:
#     res = {}
#     res_dict = {}
#     for comment in comments:
#         res.setdefault(comment['category'], []).append(comment)
#
#     for k, v in res.items():
#         for comment in v:
#             del comment['category']
#         res_dict[k] = sorted(v, key=lambda x: x['likes'], reverse=True)
#
#     with open(filename, 'w', encoding='utf-8') as f:
#         json.dump(res_dict, f, ensure_ascii=False, indent=2)
# comments = [
#     {"user": "Артем", "text": "Очень классный урок!", "likes": 3, "category": "Python"},
#     {"user": "Мария", "text": "Жду продолжения курса!", "likes": 5, "category": "Python"},
#     {"user": "John", "text": "JavaScript — the best!", "likes": 8, "category": "JavaScript"},
#     {"user": "Alex", "text": "C++ слишком сложный", "likes": 3, "category": "C++"}
# ]
#
# export_grouped_comments(comments, filename='files/json/comments.json')
# with open('files/json/comments.json', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_comments(comments, filename, reverse=None):
#     with open(filename, 'w', encoding='utf-8') as f:
#         if reverse == True:
#             json.dump(sorted(comments, key=lambda x: x['likes'], reverse=True), f, ensure_ascii=False, indent=2)
#         elif reverse == False:
#             json.dump(sorted(comments, key=lambda x: x['likes']), f, ensure_ascii=False, indent=2)
#         else:
#             json.dump(comments, f, ensure_ascii=False, indent=2)
# data = [
#     {"user": "Артем", "text": "Отличный урок!", "likes": 12},
#     {"user": "Мария", "text": "Спасибо, всё понятно", "likes": 8},
#     {"user": "John", "text": "Great explanation!", "likes": 15}
# ]
#
# export_comments(data,'files/json/comments.json', True)
#
# with open('files/json/comments.json', 'r', encoding='utf-8') as f:
#     print(f.read())
# # print(sorted(data, key=lambda x: x['likes'], reverse=True))
'---------------------------------------------'
# def save_profile(compact=False, sort=False, **kwargs) -> None:
#     with open('files/json/profile_1.json', 'w', encoding='utf-8') as file:
#         if compact==False and sort==False:
#             json.dump(kwargs, file, indent=2, ensure_ascii=False)
#         elif compact==True and sort==False:
#             json.dump(kwargs, file, ensure_ascii=False)
#         elif compact==False and sort==True:
#             json.dump(kwargs, file, indent=2, sort_keys=True, ensure_ascii=False)
#         else:
#             json.dump(kwargs, file, sort_keys=True, ensure_ascii=False)
#
# # save_profile(
# #     name="Андрей",
# #     age=40,
# #     occupation="Data Engineer",
# #     country="Россия",
# #     compact=False,
# #     sort=False
# # )
#
# save_profile(
#     name="Андрей",
#     age=40,
#     occupation="Data Engineer",
#     country="Россия",
#     compact=True,
#     sort=True
# )
#
# with open('files/json/profile_1.json', 'r', encoding='utf-8') as file:
#     print(file.read())
'---------------------------------------------'
# def save_profile(dct: dict) -> None:
#     with open('files/json/profile.json', 'w', encoding='utf-8') as file:
#         json.dump(dct, file, indent=2, ensure_ascii=False)
#
# dct = {"name": "Артем", "age": 35, "hobbies": ["теннис", "чтение", "программирование"], "is_student": False}
#
# save_profile(dct)
#
# with open('files/json/profile.json', 'r', encoding='utf-8') as file:
#     # data = json.load(file)
#     # print(data)
#     print(file.read())
'---------------------------------------------'
# def find_best_manager(json_file: json) -> None:
#     sell_manager = {}
#     with open(json_file, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#
#     for manager in data:
#         for car in manager['cars']:
#             sell_manager.setdefault(manager['manager']['first_name'] + ' ' + manager['manager']['last_name'], 0)
#             sell_manager[manager['manager']['first_name'] + ' ' + manager['manager']['last_name']] += car['price']
#
#     best_manager = max(sell_manager.items(), key=lambda x: x[1])
#     print(*best_manager)
#
# find_best_manager('files/json/sales_small.json')
'---------------------------------------------'
# def decode_text(encoded: str, alphabet: json) -> None:
#     decoded_text = ''
#     with open(encoded, 'r', encoding='utf-8') as file, open(alphabet, 'r') as a_file:
#         alphabet_text = json.load(a_file)
#         for line in file:
#             for char in line:
#                 if char not in alphabet_text:
#                     decoded_text += char
#                 else:
#                     decoded_text += alphabet_text[char]
#     with open('files/json/decoded.txt', 'w', encoding = 'utf-8') as file:
#         file.write(decoded_text)
#
# # decode_text('files/json/secret.txt', 'files/json/alpha.json')
# decode_text('files/json/abracadabra.txt', 'files/json/alpha_13.json')
# with open('files/json/decoded.txt', 'r', encoding='utf-8') as file:
#     print(file.read())
'---------------------------------------------'
# def get_max_women(json_file: json) -> None:
#     max_women = 0
#     key_id = 0
#     with open(json_file, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#         res = {}
#         for d in data:
#             for p in d['people']:
#                 if p['gender'] == 'Female' and p['year'] > 1977:
#                     res.setdefault(d['id_group'], 0)
#                     res[d['id_group']] += 1
#
#         for key, value in res.items():
#             if value > max_women:
#                 max_women = value
#                 key_id = key
#     print(f'{key_id} {max_women}')
#
# get_max_women('files/json/group_people.json')
'---------------------------------------------'
# def print_sorted_people(json_string: json) -> None:
#     data = json.loads(json_string)
#     for person in sorted(data, key=lambda x: (x['age'], x['name'])):
#         print(f'{person["name"]}, {person["country"]}, {person["age"]}')
#
# people = '[{"name": "Charlie Brown", "country": "USA", "age": 25}, {"name": "Amanda Clark", "country": "Canada", "age": 25},{"name": "Alice Johnson", "country": "USA", "age": 28}, {"name": "Mark Smith", "country": "UK", "age": 35}, {"name": "Sophie Lee", "country": "Australia", "age": 22}, {"name": "Ivan Petrov", "country": "Russia", "age": 30}]'
# print_sorted_people(people)
'---------------------------------------------'
# def mark_hits(field_file: str, shots_file: str) -> None:
#     field = {}
#     name = 'ABCDEFGHIJ'
#     game = []
#     game_lst=[]
#     with (open(field_file, 'r', encoding='utf-8') as fi,
#           open(shots_file, 'r', encoding='utf-8') as sh):
#         f = fi.readlines()
#         for i in range(len(name)):
#             for j in range(len(name)):
#                 field[name[j] + str(i+1)] = f[i].split()[j]
#         for s in sh:
#             if field[s.strip()] == '~':
#                 field[s.strip()] = '•'
#             elif field[s.strip()] == '■':
#                 field[s.strip()] = 'X'
#
#         for value in field.values():
#             game += value + ' '
#
#         game_lst = [game[i:i + 20] for i in range(0, len(game), 20)]
#
#     with open('files/sea_war/updated_field.txt', 'w', encoding='utf-8') as file:
#         for lst in game_lst:
#             file.write(f'{"".join(lst)}\n')
#     return None
#
# mark_hits('files/sea_war/field_1.txt', 'files/sea_war/shots_1.txt')
# with open('files/sea_war/updated_field.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_poll_results(*args) -> None:
#     res = {}
#     res_reverse = {}
#     for dct in args:
#         for k, v in dct.items():
#             res.setdefault(k, 0)
#             res[k] += v
#     for key, value in sorted(res.items(), key=lambda x: (x[1], x[0]), reverse=False):
#         res_reverse.setdefault(value, '')
#         res_reverse[value] += key + ', '
#     with open('files/results.txt', 'w', encoding='utf-8') as f:
#         count = 1
#         f.write('Итоги общего голосования:\n')
#         for key,value in sorted(res_reverse.items(), key=lambda x: x[0], reverse=True):
#             f.write(f'{count}. {value.strip(', ')} — {key} голосов\n')
#             count += 1
#     return None
#
# export_poll_results(
#     {"Python": 12, "C++": 8, "Go": 9, "Swift": 6},
#     {"Rust": 12, "Kotlin": 8, "Ruby": 6},
#     {"Python": 3, "Go": 6, "Swift": 4, "Rust": 1},
#     {"Kotlin": 2, "Ruby": 4, "JavaScript": 7}
# )
#
# with open('files/results.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_poll_results(results: dict[str, int]) -> None:
#     with open('files/results.txt', 'w', encoding='utf-8') as file:
#         file.write('Результаты опроса:\n')
#         count = 1
#         for key, values in sorted(results.items(), key = lambda x: x[1], reverse = True ):
#             file.write(f'{count}. {key} — {values} голосов\n')
#             count += 1
#
# results = {
#     "Python": 38,
#     "JavaScript": 25,
#     "C++": 12,
#     "Java": 17
# }
# export_poll_results(results)
#
# with open('files/results.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def create_file_with_numbers(n: int) -> None:
#     with open("files/" + f'range_{n}.txt', 'w', encoding='utf-8') as f:
#         for i in range(1, n+1):
#             f.write(str(i) + '\n')
#     return None
#
# create_file_with_numbers(5)
#
# with open('files/range_5.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def save_board(n: int) -> None:
#     doska = [[] for e in range(n)]
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if count % 2 == 0:
#                 doska[i].append('#')
#             else:
#                 doska[i].append('.')
#             count += 1
#         if n % 2 == 0:
#             count += 1
#         else:
#             continue
#     with open('files/chess_board.txt', 'w', encoding='utf-8') as f:
#         for lst in doska:
#             f.write(f'{''.join(lst)}\n')
#     return None
# # save_board(5)
# save_board(10)
#
# with open('files/chess_board.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def export_song_stats(filename: str) -> None:
#     with open(filename, 'r', encoding='utf-8') as fr:
#         file = fr.readlines()
#     with open('files/stats.txt', 'w', encoding='utf-8') as fw:
#         for i, f in enumerate(file, 1):
#             fw.write(f'Строка {i}: {len(f.strip())} символов\n')
#     return None
# # export_song_stats('files/lyrics.txt')
#
# with open('files/jude.txt', 'r', encoding='utf-8') as f:
#     print(f.readlines())
#
# export_song_stats('files/jude.txt')
#
# with open('files/stats.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def clean_file(filename) -> None:
#     lst_clean = []
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             line = line.strip('\n')
#             if bool(line):
#                 lst_clean.append(line)
#     with open('files/cleaned.txt', 'w', encoding='utf-8') as f:
#         for line in lst_clean:
#             f.write(f'{line}\n')
#
# clean_file('files/star_wars.txt')
#
# with open('files/cleaned.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def remove_duplicate_lines(filename: str, output_filename: str) -> None:
#     with open(filename, 'r', encoding='utf-8') as file:
#         lst_clean = []
#         for line in file:
#             if line.strip('\n') not in lst_clean:
#                 lst_clean.append(line.strip('\n'))
#     with open(output_filename, 'w', encoding='utf-8') as f:
#         for lst in lst_clean:
#             f.write(f'{lst}\n')
#     return None
#
# remove_duplicate_lines('files/meetings.txt', 'files/cleaned_meetings.txt')
#
# with open('files/cleaned_meetings.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def reverse_lines(filename) -> None:
#     with open(filename, 'r', encoding='utf-8') as f:
#         all_lines = f.readlines()
#     with open('files/reversed.txt', 'w', encoding='utf-8') as file:
#         for line in all_lines[::-1]:
#             file.write(line.strip() + '\n')
#     return None
#
# reverse_lines('files/terminator.txt')
#
# with open('files/reversed.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def save_shopping_list(items: list[str]) -> None:
#     with open('files/shopping.txt', 'w', encoding='utf-8') as file:
#         file.write('Список покупок:\n')
#         count = 1
#         for item in items:
#             file.write(f'{count}. {item}\n')
#             count += 1
#     return None
#
# save_shopping_list(['Хлеб', 'Молоко', 'Яйца'])
#
# with open('files/shopping.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
'---------------------------------------------'
# def check_hits(shots: str, ships: str) -> int:
#     with open(shots) as f1, open(ships) as f2:
#         pif = set(f1.read().split())
#         paf = set(f2.read().split())
#     return len(pif & paf)
#
# # # def check_hits(shots_file: str, ships_file: str)-> int:
# # #     shots = []
# # #     ships = []
# # #     boom = 0
# # #     with open(shots_file, 'r', encoding='utf-8') as shoots_f:
# # #         for line in shoots_f:
# # #             shots.append(line.strip())
# # #     with open(ships_file, 'r', encoding='utf-8') as ships_f:
# # #         for line in ships_f:
# # #             ships.append(line.strip())
# # #     for shot in shots:
# # #         if shot in ships:
# # #             boom += 1
# # #     return boom
# #open(filename, 'r', encoding='utf-8') as f:
#         for line in f:
#
# # print(check_hits('files/sea_war/shots_alpha.txt', 'files/sea_war/ships_alpha.txt'))
# '---------------------------------------------'
# # def find_words_ending_with_eya(filename: str) -> None:
# #     lst_words = []
# #     with       line = line.strip().upper()
#             if line[-2:] =='ЕЯ' and line not in lst_words:
#                 lst_words.append(line)
#     for word in sorted(lst_words, key=lambda x: (len(x), x[0])):
#         print(word)
#
# find_words_ending_with_eya('files/base.txt')
'---------------------------------------------'
# def word_frequencies(filename: str) -> dict:
#     dict_words = dict()
#     with open(filename, 'r', encoding='utf-8') as f:
#         for line in f:
#             for word in line.strip().split():
#                 dict_words.setdefault(word.upper(), 0)
#                 dict_words[word.upper()] += 1
#     return dict_words
#
# print(word_frequencies('files/greeting.txt'))
'---------------------------------------------'
# def count_unique_words(filename: str) -> int:
#     words = []
#     with open(filename, 'r', encoding = 'utf-8') as f:
#         for line in f:
#             for word in line.strip().split():
#                 if word.lower() not in words:
#                     words.append(word.lower())
#     return len(words)
# print(count_unique_words('files/test_1.txt'))
'---------------------------------------------'
# def find_lines_len_more_6(file_name: str) -> int:
#     count = 0
#     with open(file_name, 'r', encoding='utf-8') as f:
#         for line in f:
#             if len(line.strip()) > 6:
#                 count += 1
#     return count
#
# print(find_lines_len_more_6('files/test3.txt'))
'---------------------------------------------'
# def get_best_student(filename: str) -> str:
#     best_student = ''
#     score = 0
#     f = open(filename, 'r', encoding='utf-8')
#     for line in f:
#         line = line.strip().split()
#         if int(line[2]) >= score:
#             score = int(line[2])
#             best_student = f'{line[1].replace(":", "")} {line[0]}'
#     f.close()
#     return best_student
#
# print(get_best_student('files/top_score_2.txt'))
'---------------------------------------------'
# print(punctuation)
#
# def longest_word_in_file(filename: str) -> str:
#     len_word = 0
#     word_res = ''
#     with open(filename, 'r', encoding='utf-8') as f:
#         for line in f:
#             if len(line) > 1:
#                 for word in line.split():
#                     word = ''.join(w for w in word if w not in punctuation)
#                     if len(word) >= len_word:
#                         len_word = len(word)
#                         word_res = word
#             else:
#                 break
#     return word_res
#
# print(longest_word_in_file('files/english_text.txt'))
'---------------------------------------------'
# def sum_columns(file_name: str) -> list[int]:
#     lst = []
#     with open(file_name, 'r') as f:
#         for line in f:
#             lst.append([num for num in map(int, line.split())])
#     return list(map(sum, zip(*lst)))
#
# print(sum_columns('отчет.txt'))
#
# a = [34, 6, 55]
# b = [22, 56, 77]
# print(list(zip(a, b)))
'---------------------------------------------'
# def remove_punctuation(text: str) -> str:
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     text_new = ''
#     for char in text:
#         if char not in punctuation:
#             text_new += char
#     return text_new
# # Пример:
# text = "Hello, World! How's it going?"
# print(remove_punctuation(text))
#
# def get_unique_words(file_name: str) -> list[str]:
#     lst = []
#     with open(file_name, 'r') as f:
#         for line in f:
#             for word in line.split():
#                 lst.append(remove_punctuation(word.lower()))
#     return sorted(set(lst))
#
# print(get_unique_words('test_2.txt'))
'---------------------------------------------'
# def most_talkative_line(file_name: str) -> str:
#     res = ''
#     len_str = 0
#     with open(file_name, 'r') as f:
#         for line in f:
#             if len(line.split()) >= len_str:
#                 res = line
#                 len_str = len(line.split())
#     return res
# print(most_talkative_line('test_2.txt'))
'---------------------------------------------'
# def print_lines_with_numbers(file: str) -> None:
#     f = open(file, 'r')
#     count = 1
#     for line in f:
#         print(f'{count}: {line.strip()}')
#         count += 1
#     f.close()
'---------------------------------------------'
# def file_n_lines(file_name: str, n: int) -> None:
#     with open(file_name, 'r') as f:
#         for i in range(n):
#             print(f.readline().strip())
'---------------------------------------------'
# def print_first_and_last_line(name_files: str) -> None:
#     with open(name_files, 'r') as f:
#         res = f.readlines()
#         print(res[0].strip())
#         print(res[-1].strip())
#
# print_first_and_last_line('test_2.txt')
'---------------------------------------------'
# def print_first_two_lines(name_file: str):
#     with open(name_file, 'r') as f:
#         print(f.readline().strip())
#         print(f.readline().strip())
#
# print_first_two_lines(name_file='test_2.txt')
'---------------------------------------------'
# def longest_palindrome(filename: str) -> str:
#     res = ''
#     with open(filename, 'r') as f:
#         for word in f.read().split():
#             if word.lower() == word[::-1].lower():§
#                 if len(word) > len(res):
#                     res = word
#     return res
#
# print(longest_palindrome('test_2.txt'))
'---------------------------------------------'
# def count_word_in_file(file_name: str, word: str) -> int:
#     with open(file_name, "r") as f:
#         return f.read().lower().count(word)
#
# print(count_word_in_file('test_1.txt', "say"))
'---------------------------------------------'
# def compare_files(file1: str, file2: str) -> bool:
#     with open(file1, "r") as f1:
#         with open(file2, "r") as f2:
#             return f1.read() == f2.read()
#
# print(compare_files('test_1.txt', 'test_2.txt'))
'---------------------------------------------'
# def print_file_content(file_name: str) -> None:
#     file = open(file_name, "r")
#     print(file.read())
#     file.close()
#
# print_file_content("test_1.txt")
'---------------------------------------------'
# def count_lines_in_file(file_name: str) -> int:
#     file = open(file_name, 'r')
#     count = 0
#     for line in file:
#         count += 1
#     file.close()
#     return count
#
# print(count_lines_in_file('test_2.txt'))
