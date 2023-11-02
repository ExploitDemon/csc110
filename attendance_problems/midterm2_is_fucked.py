# def remove_evens(lst):
#     i = 0
#     while i < len(lst):
#         if lst[i] % 2 == 0:
#             lst.pop(i)
#         else:
#             i += 1
#     return lst
#
#
# def main():
#     test_list = [1, 2, 2, 1, 3]
#     assert remove_evens(test_list) == [1, 1, 3]
#
#     test_list = [1, 2, 4, 4, 1, 3, 4]
#     assert remove_evens(test_list) == [1, 1, 3]
#
#     test_list = []
#     assert remove_evens(test_list) == []
#
#
# main()


# def update(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] < 0:
#             numbers[i] = -1
#         if numbers[i] > 0:
#             numbers[i] = 3
#         if numbers[i] == 0:
#             numbers[i] = "ZERO"
#     return numbers
