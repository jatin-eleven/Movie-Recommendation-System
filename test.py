import time

def countdown(t):

	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		# time.sleep(1)
		t -= 1

	print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))


# import signal
# import time
# # def timeout_handler(signal, frame):
# #     raise Exception('Time is up!')
# # signal.signal(signal.SIGALRM, timeout_handler)

# import threading
# seconds_passed = 0


# def timer():
#     while True:
#         seconds_passed += 1
#         time.sleep(1)


# thread1 = threading.Thread(target=timer)
# thread1.start()
