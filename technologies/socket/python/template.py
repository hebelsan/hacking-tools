#!/usr/bin/env python

import socket

HOST = "challenge.ctf.games"
PORT = 32693 

#read one line from the socket
def get_substring(test_str, sub1, sub2):
    # getting index of substrings
	idx1 = test_str.index(sub1)
	idx2 = test_str.index(sub2)
	res = ''
	# getting elements in between
	for idx in range(idx1 + len(sub1) + 1, idx2):
		res = res + test_str[idx]
	return res

def handle_equation(equation_str):
	if '/' in equation_str and '.' not in equation_str:
		equation_str = equation_str.replace("/", "//")
	res = eval(equation_str)
	res = round(res,1)
	return str(res).encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to the server on local computer 
    s.connect((HOST, PORT))
    # Loop to read from the socket until the server requires input
    while True:
        data = s.recv(1024)  # Receive data (adjust buffer size as needed)
        if not data:
            # The server has closed the connection
            break
        print(data)  # Print received data        
        # Check if the server requires input
        if "Do you want to give it a chance? (Y/n): " in data.decode('utf-8'):
            s.send('Y'.encode('utf-8'))
        if "What is" in data.decode('utf-8'):
            equation = get_substring(data.decode('utf-8'), "What is", "? ")
            s.send(handle_equation(equation))
    # close the connection 
    s.close()
