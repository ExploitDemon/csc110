def concatenate(words):
    result = ""
    i = 0
    while i < len(words):
        result += words[i]
        if i != len(words) - 1:
            result += " "
        i += 1
    return result


def main():
    value = concatenate([])
    assert value == "", \
        f"expected return value was an empty string, but function returned {value}"

    value = concatenate(["", "", ""])
    assert value == "  ", \
        f"expected return value was an \"  \", but function returned {value}"

    value = concatenate(["Hi", "there"])
    assert value == "Hi there", \
        f"expected return value was an \"Hi There\", but function returned {value}"

    print("All tests passed.")


if __name__ == '__main__':
    main()
