def permutations(list):
    #Listede eleman olup olmadiginin kontrolu
    if len(list) == 0:
        return []
    #Listede 1 eleman varsa sonuc 1
    if len(list) == 1:
        return list

    # Listede 1'den fazla eleman varsa permutasyonu bul
    perm_list = [] # o anki permutasyonu tutan liste
    for i in range(len(list)):
       m = list[i]
       sub_list = list[:i] + list[i+1:]
       for p in permutations(sub_list):
           perm_list.append(m + p)
    return perm_list

print(permutations(list('123')))
print("\t")
print(permutations(list('abc')))
print("\t")
