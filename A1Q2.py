
with open('regex-sum-42.txt', 'r') as file:
    content = file.read()

numbers = [int(num) for num in content.split() if num.isdigit()]
total_sum = sum(numbers)

print(f"The sum of all the numbers in the file is: {total_sum}")



