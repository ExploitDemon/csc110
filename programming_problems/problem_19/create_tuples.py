def zip_lists(list_1, list_2, list_3):
    """
    Zips three lists into a list of tuples

    Args:
      list_1: First list
      list_2: Second list
      list_3: Third list

    Returns:
      A list of tuples where each tuple contains the elements from the
      three lists at the same index
    """

    zipped = []
    for i in range(len(list_1)):
        zipped.append((list_1[i], list_2[i], list_3[i]))

    return zipped
