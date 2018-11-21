def massinmass(x):
    result = []
    for i in x:
        if type(i) == list:
            result.extend(massinmass(i))
        else:
            result.append(i)
    return result

xx = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

print(massinmass(xx))
