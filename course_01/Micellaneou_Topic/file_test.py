# f = open('example.txt', mode='r')
# print(f.read())
# f.close()

# f = open("test.txt",'w')
# f.write("this is a first file")
# f.write("contains two lines\n")
# f.close()

# f=open("test.txt",'r')
# print(f.read())
# print(f.read(4))
# print(f.read(10 ))
# print(f.tell())

# //Renaming and deleting

import os
# os.rename("test.txt","sample.txt")
# os.remove("sample.txt")

# directory
# print(os.getcwd())
# print(os.listdir(os.getcwd()))

# os.mkdir('test')
# os.rmdir('test')


import shutil
import os
# os.mkdir('test')
# os.chdir('./test')
# f = open("testfile.txt",'w')
# f.write("hello world")
# os.chdir("../")
# os.rmdir('test')
shutil.rmtree('test')


# print(os.getcwd())
