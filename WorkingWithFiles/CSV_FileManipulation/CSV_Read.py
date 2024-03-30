import csv
import pprint

# #Reading From a SampleCSV File and Writing it Down in @ FinalCSV
# l=[]
# with open("Csv Files\SampleCsv.csv","r") as x:
#     data=csv.reader(x)
#     for i in data:
#         print(i)
#         l.append(i)

# # pprint.pprint(l)

# header=['S.No','Address','Name','Revenue','Profit','Principal Intrest','Simple Intrest','Territory','Bussiness','Percentile']
# with open("FinalCsv.csv","w") as y:
#     data=csv.writer(y)
#     data.writerow(header)
#     data.writerows(l)

# # Splitting down "name" column into two columns such as FirstName and LastName and saving it into a new CSV File
# o=[]
# with open("Csv Files\FinalCsv.csv","r") as a:
#     data=csv.reader(a)
#     for i in data:
#         o.append(i)
# #print(o)
# p=[]
# for j in o[1:]:
#     l=[]
#     try:
#         a=j[2]
#         b=a.split()
#         x=b[0]
#         y=' '.join(b[1:])
#         for k in j:
#             if j[2]==k:
#                 l.append(x)
#                 l.append(y)
#             elif j[3]==k:
#                 q=int(k)*10
#                 l.append(q)
#             else:
#                 l.append(k)
#     except:
#         pass
#     p.append(l)

# h=['S.No','Address','First Name','Last Name','Revenue','Profit','Principal Intrest','Simple Intrest','Territory','Bussiness','Percentile']
# with open("FinalCsv_.csv","w") as y:
#     data=csv.writer(y)
#     data.writerow(h)
#     data.writerows(p)

# pprint.pprint(p)