from typing import Any

print('Hello, chuvak!')
print(25 * '-')
'---------------------------------------------'


def sum_columns(file_name: str) -> list[int]:
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            lst.append([num for num in map(int, line.split())])
    f.close()
    return list(map(sum, zip(*lst)))

print(sum_columns('отчет.txt'))

a = [34, 6, 55]
b = [22, 56, 77]
print(list(zip(a, b)))

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
#     f.close()
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
#     f.close()
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
#     f.close()
'---------------------------------------------'
# def print_first_and_last_line(name_files: str) -> None:
#     with open(name_files, 'r') as f:
#         res = f.readlines()
#         print(res[0].strip())
#         print(res[-1].strip())
#     f.close()
#
# print_first_and_last_line('test_2.txt')
'---------------------------------------------'
# def print_first_two_lines(name_file: str):
#     with open(name_file, 'r') as f:
#         print(f.readline().strip())
#         print(f.readline().strip())
#     f.close()
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
#     return count
#
# print(count_lines_in_file('test_2.txt'))
