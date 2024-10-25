async def answer_render(data):
    a, b, v, g = 0, 0, 0, 0
    for i in data:
        if data[i] == 'А':
            a += 1
        elif data[i] == 'Б':
            b += 1
        elif data[i] == 'В':
            v += 1
        elif data[i] == 'Г':
            g += 1
            
    variables = {'a': a, 'b': b, 'c': v, 'd': g}
    max_key = max(variables, key=variables.get)
    return  max_key