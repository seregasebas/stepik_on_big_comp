print('Hello, chuvak!')
print(25 * '-')
'---------------------------------------------'

def file_n_lines(file_name: str, n: int) -> None:
    with open(file_name, 'r') as f:
        for i in range(n):
            print(f.readline().strip())
    f.close()

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

