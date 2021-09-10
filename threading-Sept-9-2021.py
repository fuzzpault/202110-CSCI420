'''
Paul Talaga
CSCI 420 - Networking - Fall 2021
Threading demo
Sept 9, 2021

'''

import threading, time

def doStuff(thread_num):
	global counter
	#counter +=1
	print("Starting {}".format(thread_num))
	for i in range(10):
		print(i)
		a = 1
		for i in range(10000):
			a += 1
			counter +=1
		#time.sleep(1)
	print("Ending {}".format(thread_num))

print("stuff here")

# Keep a global variable and have each thread update it.  
# In C, C++, or Java, this will cause the WORST situation 
# possible, as each thread will get paused and restarted
# even in the middle of an update, so the final value 
# will not be correct.  This works in Python because of the
# Global Interpreter Lock (GIL) (https://realpython.com/python-gil/)
counter = 0

thread = [None] * 10
# This will start 10 threads and keep them in an array
for i in range(10):
	thread[i] = threading.Thread(target = doStuff, args=[i])
	thread[i].start()
# The join function will block this current (main) thread
# until the referenced thread is complete.
for i in range(10):
	thread[i].join()
	print("Thread {} joined".format(i))
#for i in range(10):
#		print("Parent: {}".format(i))
#		a = 0
#		for i in range(10000000):
#			a += 1
		#time.sleep(1)
# Because of the joins above, counter should not be updating
# any more.
print("Counter: {}".format(counter))