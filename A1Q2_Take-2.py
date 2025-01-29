import re

with open("regex-sum-42.txt", 'r') as file:
    content = file.read()
    numbers = re.findall('\d+', content)

    total_sum = sum(int(i) for i in numbers)

print(f'The sum of all numbers in the file is: {total_sum}')


