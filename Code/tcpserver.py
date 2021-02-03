#import database module
import sqlite3

# import socket programming library 
import socket 

# import thread module 
from _thread import *
import threading 

from DBUtil import Database

def addUser(data):
	try:
		conn = sqlite3.connect('Auth.sqlite3')
		c = conn.cursor()
		sql ='''INSERT INTO AUTHENTICATION(Username,Password) VALUES(?,?)'''
		c.execute(sql,data)
		conn.commit()
		conn.close()
		return True
	except error as e:
		print(e)
		return False

def existUser(data):
	try:
		conn = sqlite3.connect('Auth.sqlite3')
		c = conn.cursor()
		sql ='''SELECT * FROM AUTHENTICATION WHERE Username=?'''
		c.execute(sql,(data,))
		rows = c.fetchall()
		if(len(rows)>0):
			conn.close()
			return True
		conn.close()
		return False
	except error as e:
		print(e)
		return False

def isValidUser(data):
	print(data)
	try:
		conn = sqlite3.connect('Auth.sqlite3')
		c = conn.cursor()
		sql ='''SELECT * FROM AUTHENTICATION WHERE Username=? AND Password=?'''
		c.execute(sql,data)
		rows = c.fetchall()
		if(len(rows)>0):
			conn.close()
			return True
		conn.close()
		return False
	except error as e:
		print(e)
		return False





def processMessage(data):
	print("data arived ... before encoding printing")
	print(data)
	
	data = data.decode("utf-8")
	print("after decoding printing ... ")
	print(data)
	alldata = str.split(data)
	print(alldata)
	if alldata[0] == "login":
		if isValidUser((alldata[1], alldata[2])):
			return "OK"
		return "NO"
	else:
		if alldata[0] == "register":
			print(alldata[1])
			if existUser(alldata[1]):
				return "NO"
			if addUser((alldata[1],alldata[2])):
				return "OK"
			else:
				return "NO"

	

# thread fuction 
def threaded(c): 
	while True: 

		# data received from client 
		data = c.recv(10000) 
		if not data:
			break

		print(data)
		reply=processMessage(data)
		print("\nreceived\n")
		c.send(bytearray(reply,'utf-8')) 

	# connection closed 
	c.close() 






def Main(): 
	host = '127.0.0.1'

	# reverse a port on your computer 
	# in our case it is 12345 but it 
	# can be anything 
	port = 5555
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to post", port) 

	# put the socket into listening mode 
	s.listen(5) 
	print("socket is listening") 

	# a forever loop until client wants to exit 
	while True: 

		# establish connection with client 
		c, addr = s.accept() 

		# lock acquired by client 
		
		print('Connected to :', addr[0], ':', addr[1]) 

		# Start a new thread and return its identifier 
		start_new_thread(threaded, (c,)) 
	s.close() 


if __name__ == '__main__': 
	Main() 


