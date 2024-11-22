def all_vatiants(text):
    v = len(text)
    for end_ in range(1, v + 1):
        for start_ in range(v - end_ + 1):
            yield text[start_:start_ + end_]

a = all_vatiants("abc")
for i in a:
    print(i)

