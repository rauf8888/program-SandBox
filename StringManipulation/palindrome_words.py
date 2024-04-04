a=str(input("Enter a Sentence: "))
a_=a.lower()
word=a_.split()
palcount=0
b=[]
for i in word:
    i_=i[::-1]
    if i_==i:
        palcount+=1  
        b.append(i_)  
print("Total number of palindrome in this sentence is : ",palcount)
for j in b:
    print(j)
