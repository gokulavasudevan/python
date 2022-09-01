# Finding Prime numbers between given number
# Date of modification = 09/01/2022

Name =input("Please Enter your name?")

print ("Hi", Name, "Welcome")

lower = int(input("Enter Starting number of the Prime Number?")) 
upper = int(input("Enter Ending number of the Prime Number?")) 

print ("Prime numbers between", lower, "and", upper, "are Selected")

if upper < lower:
                print ("Starting number higher than ending number? Please try again")
                

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
        #print (num, "Is not a Prime Number because it is divided by", i)
                    break
        else:
                print(num)
                
                

