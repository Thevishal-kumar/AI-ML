double  = lambda x:x**2
# print(double(5))

lst = [1,2,3,4,5]
new_lst = list(map(lambda x:x**2,lst))
print(new_lst)

new_lst = list(filter(lambda x:(x%2==0),lst))
print(new_lst)