def odds_and_evens(integers):
    odd_list = []
    even_list = []
    for num in integers:
        if num % 2 == 0:
            even_list.append(num)
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list, even_list
