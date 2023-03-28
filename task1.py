#Assign a value to variables
num1 = 9
num2 = 5
num3 = 3

#find the largest value among num1 and num2
#initialize largestVal
largestVal = 0
#use if-else statement to check largest of num1 and num2
if(num1 > num2):
    largestVal = num1
else:
    largestVal = num2
#print the value
print("The largest value is: ", largestVal)    

#find odd or even of num1
print()
#check whether it gives remainder or not
if(num1 % 2 == 0):
    print("num1", num1, "is an even value")
else:
    print("num1", num1, "is an odd value")

#sort given values in descending order
print()
#conditional statement to check which one is greater among the three and store it in the variables #l1, l2, and l3
if(num1 > num2 and num1 > num3): #find if num1 is largest
    if(num2 > num3):
        l1 = num1
        l2 = num2
        l3 = num3
    else:
        l1 = num1
        l2 = num3
        l3 = num2
elif(num2 > num1 and num2 > num3): #check if the num2 is larger value
    if(num1 > num3):
        l1 = num2
        l2 = num1
        l3 = num3
    else:
        l1 = num2
        l2 = num3
        l3 = num1
else:
    if(num1 > num2): #else num3 is largest and find next largest
        l1 = num3
        l2 = num1
        l3 = num2
    else:
        l1 = num3
        l2 = num2
        l3 = num1

#print the sorted num
print("Sorted values from largest to smallest: ",l1, l2, l3) 