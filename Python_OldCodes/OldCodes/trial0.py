import re

sum = 0

file = open('regex_sum_381103.txt')
for line in file:
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        for number in numbers:
            sum += int(number)

print(sum)