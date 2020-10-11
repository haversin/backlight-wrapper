def lin2curved(percent):
	x = percent
	return x+x*(x-100)*(x+100)/(10100)

def generateSteps(n):
	for i in range(0,n+1):
		yield round(8.52*lin2curved(0.0 + (100.0/n)*i))

def main():
	steps = [x for x in generateSteps(20)]
	print(steps)
	# [0,1,2,4,8,15,25,39,57,81,110,145,187,237,295,362,439,525,623,731,852]

if __name__ == "__main__":
    main()