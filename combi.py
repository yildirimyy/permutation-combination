def combinations(list_item, n, com_list=[]):
    # recursive cagirimda n'li seviyeye geldiysen dur
    if len(list_item) == n:
        # eger daha once boyle bir combinasyon bulunduysa ekleme
        # ornek: abcb icin iki kere bb bb gelir
        if not list_item in com_list:
            # bc yoksa combinasyon listesine ekle
            com_list.append(list_item)
            com_list.sort()

        # n elamanli derinlikte oldugun icin don
        return com_list
    else:
        # recursive olarak alt elemanlari bulmak icin
        # alt listeler ile cagirim yap
        for i in range(len(list_item)):
            sub_list = list_item[:i] + list_item[i+1:]
            com_list = combinations(sub_list, n, com_list)
    return com_list

print(combinations("123", 2, []))
print("\t")
print(combinations("abcb", 2, []))
print("\t")
# print(combinations(['A','B','C', 'B'], 2))
# print("\t")

#a[start:stop]
#a[start:]
#a[:stop]
#a[:]
# list = "abcb"
# print(list[:0] +" "+ list[1:])
# print(list[:1] +" "+ list[2:])
# print(list[:2] +" "+ list[3:])
# print(list[:3] +" "+ list[4:])
