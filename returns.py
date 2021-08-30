def add(a,b):
    c = a + b
    d = a - b
    if c < 0:
        return #return stops the function if there's no variable, can also return a string
    return c, d

answer = add(3,5)
print(answer[0])
print(answer[1])

added, subtracted = add(3,5)
print(added)
print(subtracted)