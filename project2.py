numArr = []

# read file and add each number to an array
with open('input.txt') as f:
	for line in f:
		numArr.append(int(line))

for i, num in enumerate(numArr):
	for j, num2 in enumerate(numArr):
		for k, num3 in enumerate(numArr):
			if i != j and i != k and j != k:
				total = num + num2 + num3
				if total == 2020:
					product = num * num2 * num3
					print(f"{num} * {num2} * {num3} = {product}")
	