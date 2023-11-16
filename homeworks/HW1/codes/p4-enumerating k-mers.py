
collection = 'A B C D E F'
num = 3

collection = collection.split(' ')
length = len(collection)


iterator = [0 for i in range(num)]
while True:
    res = ''
    for i in range(num):
        res += collection[iterator[i]]
    print(res)

    if iterator == [length-1 for i in range(num)]:
        break
    
    for j in range(num-1, -1, -1):
        if iterator[j] + 1 == length:
            iterator[j] = 0
            continue
        else:
            iterator[j] += 1
            break