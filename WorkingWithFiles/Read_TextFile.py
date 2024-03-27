#'r'-- Read only
#'w'-- Write Only
#'a'-- append Only
#'r+'-- Read and then Write
#'w+'-- Write and then Read
#'a+'-- append and then Read

### READ OPERATION IN TEXT FILES ###

# # Reading Contents from the Text File
# f=open('textfile.txt','r')
# for i in f:
#     print(i)


# # Reading Contetns from the Text File and appending it in a list
# l=[]
# f=open('textfile.txt','r')
# f_=f.read()
# for i in f_:
#     l.append(i)
# print(l)

# # Reading Contetns from the Text File and appending it in a list line by line
# l=[]
# f=open('textfile.txt','r')
# f_=f.readlines()
# for i in f_:
#     l.append(i)
# print(l)

# # Reading only specific number of characters from the textFile mentioned in the read() function
# f=open('textfile.txt','r')
# f_=f.read(15)
# print(f_)