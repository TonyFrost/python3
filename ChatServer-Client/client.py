import socket, threading, time
setserver=str(input("input ip: \n >"))
key = 8194

shutdown = False
join = False

inputport=int(input("Input port number: \n >"))
def receving (name, sock):
	while not shutdown:
		try:
			while True:
				#переменная аддр в сервере
				data, addr = sock.recvfrom(1024)
				decrypt = ""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)

				time.sleep(0.2)
		except:
			pass
host = socket.gethostbyname(socket.gethostname())
port = 0

server = (setserver,inputport)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

user = input("Input your name: \n >")

rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()

while shutdown == False:
	if join == False:
		s.sendto(("["+user + "] => join chat ").encode("utf-8"),server)
		join = True
	else:
		try:
			message = input()

			crypt = ""
			for i in message:
				crypt += chr(ord(i)^key)
			message = crypt

			if message != "":
				s.sendto(("["+user + "]: "+message).encode("utf-8"),server)
			
			time.sleep(0.2)
		except:
			s.sendto(("["+user + "] <= left chat ").encode("utf-8"),server)
			shutdown = True

rT.join()
s.close()