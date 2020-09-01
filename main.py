# lst = [23, 42, 86, 92, 93, 94]

# has_value_over_90 = False
# for val in lst:
#     if val > 90:
#         has_value_over_90 = True
#         break

# print(has_value_over_90)


"""Write an integer sum accumulator that uses a boolean flag to exit once the sum of num_list exceeds 500. Your accumulator variable should be called num_sum and your boolean flag should be called exceeded_500."""

# Leave this line alone
num_list = [96, 74, 90, 3, 26, 12, 4, 27, 19, 11, 89, 78, 33, 48, 22, 100, 44, 6, 28, 5, 52, 49, 49, 3, 44]

# Write your code here
num_sum = 0
exceeded_500 = False

for num in num_list:
  num_sum+= num
  if num_sum>500:
    exceeded_500 = True
    break

"""IN the following attempt to solve the same problem using the while loop"""

# num_sum = 0
# exceeded_500 = False

# while not exceeded_500:
#   if num_sum >500:
#     exceeded_500 = True
