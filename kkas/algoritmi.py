saraksts = [2,5,8,22,23,24,98,45,6,66,]

for j in range( len(saraksts)-1):
    for i in range( len(saraksts)-1-j):
        if saraksts[i] > saraksts[i+1]:
            temp = saraksts[i]
            saraksts[i] = saraksts[i+1]
            saraksts[i+1]= temp
print(saraksts)


def meklet(list, num):
    for i in range( len(list)-1):
        if num == list[i]:
            print(num,"Eksistē",i)
            return
    print(num,"Neeksistē")    


meklet(saraksts, 23)