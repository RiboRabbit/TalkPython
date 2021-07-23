import random

def check(input):

	try:
		input = int(input)
	except ValueError:
		raise Exception('Must be a integer')

	if (input < 1 and input > 20):
		raise Exception('Number must be in range')

	

def loop_with_rand(func):
	rand = random.choice(range(1,21))
	print(rand)
	counter = 0
	while True:
		counter += 1
		func(rand,counter)


def run(random,count):

	value = input("Guess a number between 1 and 20: ")

	try:
		check(value)
	except Exception as e:
		print(e)

	if int(value) == random:
		print(f'You Guessed It Right on {count} try')
		exit()		
	else:
		print("Wrong! Guess again..\n")	 				

def main():
	loop_with_rand(run)


if __name__ == '__main__':
	main()
