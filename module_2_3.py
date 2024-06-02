# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# positive_mylist = []
# for num in my_list:
#    if num >= 0:
#        positive_mylist.append(num)
#    else:
#        break
# print(positive_mylist)



my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
    i += 1
    if my_list[i] < 0:
        break
        print(my_list)






