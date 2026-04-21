from typing import Any
# from string import punctuation
import json
print('Hello, chuvak!')
print(25 * '-')
'---------------------------------------------'
'---------------------------------------------'
'---------------------------------------------'
'---------------------------------------------'
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
