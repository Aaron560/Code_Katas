def double_char(s):
    output = []
    for i in s:
        output.append(i+''+i)
    return "".join(output)