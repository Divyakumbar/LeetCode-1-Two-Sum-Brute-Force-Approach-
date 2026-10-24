nums=eval(input("Enter a list collection:- "))
key=eval(input("Enter a element you want to search:- "))
for i in range(len(nums)):
     if nums[i]==key:
        print("YES,Element found at ",i)
        break

        