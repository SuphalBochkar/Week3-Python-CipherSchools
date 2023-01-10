def let_counter(s):
    dic = {}
    for i in s:
        dic[i] = s.count(i)
    return dic

print(let_counter('suplso'))
