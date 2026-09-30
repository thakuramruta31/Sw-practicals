numbers = [10, 20, 30, 40, 50]

# range(len(numbers) + 1) includes an index equal to len(numbers),
# which is outside the valid index range (0 through len(numbers) - 1).
for i in range(len(numbers)):
	print(numbers[i])
