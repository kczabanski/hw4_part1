# import numbers from day1_input.txt
import numpy

numbers = numpy.loadtxt('day1_input.txt')

# part 1
count = 0

# for each number, check if the one before was smaller. if it was, up the count
for i in range(len(numbers)):
    if i == 0:
        continue
    if numbers[i] > numbers[i-1]:
        count += 1

print(count)

# part 2
count = 0

# for each number, check if the sum of the previous 3 numbers is smaller than the sum of the current 3 numbers
# if it is, up the count
for i in range(len(numbers)):
    if i < 3:
        continue
    
    prev_window = numbers[i-3] + numbers[i-2] + numbers[i-1]
    curr_window = numbers[i-2] + numbers[i-1] + numbers[i]
    
    if curr_window > prev_window:
        count += 1

print(count)
