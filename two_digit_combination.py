#Write a program to print all the unique combinations of 2 digits from 1 to 4. Repetion not allowed



print_value = []

#Creating two lists with the values 1-4
list1 = list2 = [1,2,3,4]

#First loop iterates the first list whose numbers will be filled on the tens place
for i in list1:
    #Second loop iterates the second list which numbers will be on the ones place
    for j in list2:
        print_value.append(i)
        #Value of i will be added to the list
        if i == j:
            #If we do not want a same number repeated again, we can use pass
            #Pass moves the program out of the if statement
            pass

        if i != j:
            #Adds values of j in the second place
            print_value.append(j)

            print(print_value)

        #Clears the list so that the next value can be inserted
        print_value = [] 

