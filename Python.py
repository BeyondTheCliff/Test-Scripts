import sys,time,random

typing_speed = 50 #wpm
def slow_type(t):
	for l in t:
		sys.stdout.write(l)
		sys.stdout.flush()
		time.sleep(random.random()*10.0/typing_speed)
	print ''

slow_type("Hello World!")
time.sleep(0.1)
slow_type("How are you?")
inputs=raw_input(">")
if inputs=="Good":
	slow_type("What is so good?")
elif inputs=="Bad":
	slow_type("That is sad. Why?")
else:
	slow_type("Okay!")
