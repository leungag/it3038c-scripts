import time
start_time = time.time()


print("What is your name?") 
myName = input() 
print("Hello, " + myName + ". That is a good name. How old are you?") 
myAge = input() 
programAge = int(time.time() - start_time)

print("%s? That’s funny, I'm only %d seconds old." % (myAge, programAge)) 
print("I wish I was %s years old" % (int(myAge) * 2))

myAge = int(myAge)
if myAge < 13:
	print("Learning young, that's good")
elif myAge ==13:
	print("You're a teenager now... that's cool, I guess")
elif myAge > 13 and myAge < 30:
	print("Still young, still leanring...")
elif myAge >=30 and myAge <65:
	print("Now you're adulting.")
else:
	print("...you've lived a long time?")


time.sleep(3) 

print("I’m tired. I go sleep sleep now.") 