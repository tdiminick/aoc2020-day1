numArr = []

# read file and add each number to an array
with open('input.txt') as f:
	for line in f:
		numArr.append(int(line))

for i, num in enumerate(numArr):
	for j, num2 in enumerate(numArr):
		if i != j:
			total = num + num2
			if total == 2020:
				product = num * num2
				print(f"{num} * {num2} = {product}")
	