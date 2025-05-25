# brute force 
import random
# l1 = list(range(100))
# random.shuffle(l1)

# l2 = list(range(50))
# random.shuffle(l2)

# cnt=0
# for i in l1:
#     for j in l2:
#         if i==j:
#             # print(i)
#             cnt +=1
# print(cnt)


# hashtable
l1 = list(range(100))
random.shuffle(l1)
l2 = list(range(50))
random.shuffle(l2)

smallList = {}
for ele in l2:
    smallList[ele] = 1; 
    

cnt=0
for i in l1:
    if smallList.get(i) != None: 
        print(i)
        cnt += 1
print("Number of common elements:", cnt)


