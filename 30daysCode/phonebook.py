n = int(input())
phoneBook = {}

for i in range(n):
    text = input().split(' ') # split take input and  makes a list 
    phoneBook[text[0]] = text[1]

    while True:
        # for i in range(n):
        name = str(input())
        if name in phoneBook.keys():
            print('{0}={1}'.format(name, phoneBook[name]))
        else: 
            print('not found')




# print(phoneBook.keys())

