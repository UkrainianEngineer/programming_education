first_string_of_nums = "12345"
second_string_of_nums = "611091234512"

first_list = list(first_string_of_nums)
count = sum(int(i) for i in first_list)

second_list = list(second_string_of_nums)
count2 = sum(int(n) for n in second_list)

print(count)
print(count2)