try:

    number = int(input("Enter a four digit number: "))
    result = 0
    var1 = 1000
    sum_of_squares = 0 

    if number<10000 and number>999:

        for i in range(4):
            num2 = number%10
            result = result +(var1*num2)
            sum_of_squares = sum_of_squares + (num2**2)
            number = number//10
            var1//= 10
            
        print("The given number in reverse order is: " , result)
        print("The sum of squares of all digits in the number is: ", sum_of_squares)

    else:
        print("The given number must be of four digits. Enter a four digit number")


except:
    print("Only numbers are accepted in the input. Invalid input")