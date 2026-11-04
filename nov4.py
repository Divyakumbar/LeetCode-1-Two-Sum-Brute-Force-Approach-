n=input("Enter a text: ")
d={}
count=1
for i in n.lower():
  if i.isalpha():
    if i not in d:
     d[i]=1

    else:
     d[i]+=1
    
for j in d:
 print(j,":",d[j])