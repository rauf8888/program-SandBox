string = input("Enter a Line : ")
count={}

words = string.split()
print(words)
for i in words:
    count[i] = count.get(i, 0) + 1
    print(count)
print('Word Frequency')
for key in count.keys():
    print(key, count[key])
