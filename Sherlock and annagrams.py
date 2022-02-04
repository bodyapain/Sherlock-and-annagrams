n=int(input())
sarray=''
array=[]
helparray1=''
helparray3=''
size=1
count = 0
# for i in range(n):
#     sarray=input()
#     for j in range(len(sarray)):
#         size=1
#         while size+j<len(sarray):
#             for m in range(size):  
#                 if(m+j>=len(sarray)):
#                         continue              
#                 helparray1+=sarray[m+j]
#             str1=list(helparray1)
#             str1.sort()
#             helparray1=''            
#             for k in range(j+1,len(sarray)):                
#                 for c in range(size):
#                     if(c+k>=len(sarray)):
#                         continue
#                     helparray3+=sarray[k+c]
#                 str2=list(helparray3)
#                 str2.sort()
#                 if str1==str2:
#                     count+=1
#                 helparray3=''            
#             size+=1
#     print(count)
#     count=0

for i in range(n):
    sarray=input()
    array=[]
    for j in range(len(sarray)):              
        for m in range(len(sarray)):  
            if(m+j>=len(sarray)):
                break              
            helparray1 += sarray[m+j]
            str1=list(helparray1)
            str1.sort()
            str1=''.join(str1)            
            for k in range(len(array)):
                if array[k]==str1:
                    count+=1
            array.append(str1)
        helparray1=''            
    print(count)   
    count=0         
    
    
    