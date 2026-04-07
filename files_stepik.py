from typing import Any
from string import punctuation

print('Hello, chuvak!')
print(25 * '-')
'---------------------------------------------'
def clean_file(filename) -> None:
    lst_clean = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip('\n')
            if bool(line):
                lst_clean.append(line)
    with open('files/cleaned.txt', 'w', encoding='utf-8') as f:
        for line in lst_clean:
            f.write(f'{line}\n')

clean_file('files/star_wars.txt')

with open('files/cleaned.txt', 'r', encoding='utf-8') as f:
    print(f.read())
'---------------------------------------------'
def remove_duplicate_lines(filename: str, output_filename: str) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        lst_clean = []
        for line in file:
            if line.strip('\n') not in lst_clean:
                lst_clean.append(line.strip('\n'))
    with open(output_filename, 'w', encoding='utf-8') as f:
        for lst in lst_clean:
            f.write(f'{lst}\n')
    return None

remove_duplicate_lines('files/meetings.txt', 'files/cleaned_meetings.txt')

with open('files/cleaned_meetings.txt', 'r', encoding='utf-8') as f:
    print(f.read())
'---------------------------------------------'
def reverse_lines(filename) -> None:
    with open(filename, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()
    with open('files/reversed.txt', 'w', encoding='utf-8') as file:
        for line in all_lines[::-1]:
            file.write(line.strip() + '\n')
    return None

reverse_lines('files/terminator.txt')

with open('files/reversed.txt', 'r', encoding='utf-8') as f:
    print(f.read())
'---------------------------------------------'
def save_shopping_list(items: list[str]) -> None:
    with open('files/shopping.txt', 'w', encoding='utf-8') as file:
        file.write('Список покупок:\n')
        count = 1
        for item in items:
            file.write(f'{count}. {item}\n')
            count += 1
    return None

save_shopping_list(['Хлеб', 'Молоко', 'Яйца'])

with open('files/shopping.txt', 'r', encoding='utf-8') as f:
    print(f.read())
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
