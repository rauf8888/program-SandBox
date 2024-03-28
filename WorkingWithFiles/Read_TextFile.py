#'r'-- Read only
#'w'-- Write Only
#'a'-- append Only
#'r+'-- Read and then Write
#'w+'-- Write and then Read
#'a+'-- append and then Read

### READ OPERATION IN TEXT FILES ###

# # Reading Contents from the Text File
# f=open('textfile.txt','r') #<class '_io.TextIOWrapper'>#
# for i in f:
#     print(i) #<class 'str'>#


# # Reading Contetns from the Text File and appending it in a list
# l=[]
# f=open('textfile.txt','r') #<class '_io.TextIOWrapper'>#
# f_=f.read() #<class 'str'>#
# for i in f_:
#     l.append(i)
# print(l)

# # Reading Contetns from the Text File and appending it in a list line by line
# l=[]
# f=open('textfile.txt','r') #<class '_io.TextIOWrapper'>#
# f_=f.readlines() #<class 'list'>#
# for i in f_:
#     l.append(i)
# print(l)

# # Reading only specific number of characters from the textFile mentioned in the read() function
# f=open('textfile.txt','r') #<class '_io.TextIOWrapper'>#
# f_=f.read(15) #<class 'str'>#
# print(f_)