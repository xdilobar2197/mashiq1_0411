mashiq1_0411

#1 - masala
royhat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
royhat1 = []

for i in royhat:
    royhat1.append(i ** 2)

print(royhat1)


#2 masala
royhat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
royhat1 = []
for i in royhat:
    if i % 2 == 0:
        royhat1.append(i)

print(royhat1)



# 3 - masala
royhat = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
royhat1 = []
for i in royhat:
    if i % 2 != 0:
        royhat1.append(i)
print(royhat1)


#4 - masala
royhat =['apple', 'banana', 'pear']
print(len(royhat))

#5 - masala
royhat = list('soz')
print(royhat)



#6 - masala
royhat = [1, 2, 3, 4, 5]
royhat1 = []

for i in royhat:
    royhat1.append(i ** 3)
print(royhat1)


#9 - masala
royhat = [-5, 3, -1, 0, 7, -2]
royhat1 = []
for i in royhat:
    if i > 0:
        royhat1.append(i)
print(royhat1)

#10 - masala
son = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft_son =[]
toq_son = []

for i in son:
    if i % 2 == 0:
        juft_son.append(i)
    else:
        toq_son.append(i)

print('Juft sonlar: ', juft_son)
print('toq sonlar: ', toq_son)
