# take_input =  int(input())
# temp = take_input
# s = 0
# while temp != 0:
#     remainder = int(temp % 10) # 1 0
#     s = int(s*10+remainder) #1 1
#     temp = int(temp/10) #1 0
# if (take_input == s):
#     print('{0} palidrome'.format(take_input))
# else:
#     print('{0} not palidrome'.format(take_input))

n= 1

while n<100:
    take_input =  int(input())
    temp = take_input
    s = 0
    while temp != 0:
        remainder = int(temp % 10) # 1 0
        s = int(s*10+remainder) #1 1
        temp = int(temp/10) #1 0

        if (take_input == s):
            print('{0} palidrome'.format(take_input))
        else:
            print('{0} not palidrome'.format(take_input))
        n+=1
