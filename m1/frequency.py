def search_key(dictionary1, key):
    count = 0
    for i in dictionary1:
        if dictionary1[i] == key:
            count += 1
    return count
dictionary1 = {'1': 1, '2': 4, '3': 9, '4': 16}
key = int(input('Enter a key to search: '))
print(f'{key} was found {search_key(dictionary1, key)} times')