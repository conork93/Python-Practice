#Conor Kennedy
#7/31/17

#Write a function that receives a list of numbers and returns only the even elements.


def even_numbers(a_list):
    return[x for x in a_list if x % 2==0]

a_list = [5, 4, 3, 2, 1]

x = even_numbers(a_list)

print (x)
