
def search_number(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count

numbers_list = list(range(1,11))+list(range(1,11,2))

target_number = int(input("Enter the number to search for: "))
result = search_number(numbers_list, target_number)
print(type(numbers_list))
print(numbers_list)
print(f"Number of occurrences of {target_number}: {result}")


#--------------------------------------------------------


# def count_number(nums):
#     count = 0
#     for num in nums:
#         if num == 4:
#             count += 1
#     return count

# numbers_list = [1, 5, 3, 9, 2, 4, 5, 44, 0, 4, 8]
# result = count_number(numbers_list)
# print("Number of '4' : ", result)
