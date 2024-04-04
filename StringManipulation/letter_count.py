String=str(input("Enter a string:"))
frequency = {}
for i in String:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print ("Count of all characters is :\n " +  str(frequency))
