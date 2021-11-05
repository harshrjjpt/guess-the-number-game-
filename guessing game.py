import random 

x = random.randint(1,10)
num = ""

while num != x:
	num=int(input(f"guess a number between 1 and 10 \n"))
	if num > x:
		print("****nope, its a smaller number****")
	elif num < x:
	    print("****nope, its a larger number****")
	elif num == "":
		print("enter a number dumbass")
	else:
	    print("correct, you guessed it right****")    	