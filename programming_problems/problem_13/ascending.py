# def stop_ascending(numbers):
#     if not numbers:
#         return None
#     for i in range(1, len(numbers)):
#         if numbers[i] <= numbers[i - 1]:
#             return i
#     return len(numbers)
#
#
# def main():
#     print(stop_ascending([]))  # None
#     print(stop_ascending([1, 2, 3]))  # 3
#     print(stop_ascending([1, 2, 3, 1, 5]))  # 3
#
#
# if __name__ == '__main__':
#     main()


def stop_ascending(numbers):
    i = 1
    while i < len(numbers):
        if numbers[i] <= numbers[i-1]:
            return i
        i += 1
    return len(numbers)

def main():
    print(stop_ascending([])) # None
    print(stop_ascending([1, 2, 3])) # 3
    print(stop_ascending([1, 2, 3, 1, 5])) # 3

if __name__ == '__main__':
    main()
