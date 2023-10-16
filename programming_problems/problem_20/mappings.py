def all_mappings(d):
    mappings = []
    for key, values in d.items():
        for value in values:
            mappings.append((key, value))
    return mappings
