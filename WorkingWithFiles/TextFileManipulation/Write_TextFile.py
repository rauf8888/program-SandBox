#'r'-- Read only
#'w'-- Write Only
#'a'-- append Only
#'r+'-- Read and then Write
#'w+'-- Write and then Read
#'a+'-- append and then Read

### WRITE OPERATION IN TEXT FILES ###

# # Writing contents into a text fi;e
# f=open('_textfile_.txt','w')
# f.write("dfghdjkebienegdrxhtvjyf,u ctrjucu,,i yteckcri77 tycru,,  tyrcuri kuycrki\n\n\tdfc uyebiiu iubwef o393bfhihbrg iwriufhb")
# f.close()

# # Reading the exisitng text file and storing it in a new text file with extra
# f=open('textfile.txt','r')
# f_=f.read()
# print(f_)
# w=open('_textfile_.txt','w')
# w.write(f_+" Extra Text")
# w.close()

# # Read file and write in another line by line
# f=open('textfile.txt','r')
# f_=f.readlines()
# print(f_)
# w=open('_textfile_.txt','w')
# w.write(f_)
# w.close()

# # Read file and write line by line into a file with extra text at end of each line
# f=open('textfile.txt','r')
# w=open('_textfile_.txt','w')
# f_=f.readlines()
# print(f_)
# for i in f_:
#     w.write(i+"###\n")
# w.close()

# # Read file and write down the contents of text file adding text berfore each line
# f=open('textfile.txt','r')
# w=open('_textfile_.txt','w')
# f_=f.readlines()
# print(f_)
# for i in f_:
#     w.write("rauf ===="+i)
# w.close()