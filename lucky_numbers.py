num1 = int(input("Enter a number"))
i = num1
num = num1
sum_output = 0
output_2 = 0



while i > 0:
    
    i = num1%10
    sum_output = sum_output +  i
    
    num1 = int(num1/10)    

print("")


print("The sum of all numbers is %s " %   sum_output)

print("")

if sum_output<10:
    print(num," is a lucky number"  )
    
else:
    not_lucky_num = sum_output
    while sum_output>10:
        
        while sum_output > 0:
            
            output_2 = not_lucky_num%10
            output_2 = output_2 +  sum_output
            
            sum_output = int(sum_output/10)    
        
print("The lucky number so formed is %s" % output_2)