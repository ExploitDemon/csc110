# def get_highest_average(lists):
#     list_total = None
#     for i in range(lists):
#         if not lists[i]:  # Check if the sublist is empty
#             continue
#         for j in range(len(lists[i])):
#             list_total += lists[i][j]
#             len_of_list = len(lists[i])
#             mean = list_total / len_of_list
#     return mean
#
#
#
#
#
# def mean_list


def get_highest_average(lists):
    highest_average = None
    for sublist in lists:
        if not sublist:  # Check if the sublist is empty
            continue
        list_total = sum(sublist)
        len_of_list = len(sublist)
        mean = list_total / len_of_list

        if highest_average is None or mean > highest_average:
            highest_average = mean

    return highest_average


