integer_list = []

while True:
    user_input = input("\nEnter an integer (or 'q' to stop):\n ")
    
    if user_input.lower() == 'q':
        break
    
    try:
        num = int(user_input)
        integer_list.append(num)
    except ValueError:
        print("\nInvalid input. Please enter an integer or 'q' to stop.")

print("\n\nEntered list:", integer_list,"\n")
print("Max int of Entered list:", max(integer_list))

#______________________________________________

# integer_list = []

# num_integers = int(input("Enter the number of integers: "))

# for i in range(num_integers):
#     num = int(input(f"Enter integer {i + 1}: "))
#     integer_list.append(num)

# print("Entered list:", integer_list)
# print("max:", max(integer_list))