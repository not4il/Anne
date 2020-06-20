import os, time

class color():
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	BLUE1 = '\033[94m'
	MAGENTA = '\033[35m'
	PURPLE = '\033[1;35;48m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	BLACK = '\033[1;30;48m'

def clean():
	os.system(['clear', 'cls'][os.name == 'nt'])

def banner():
	print(f'''{color.GREEN}                           ______ _ _      __  __       _             
    /\ {color.BLUE1}github.com/one-eyed{color.GREEN}|  ____(_) |    |  \/  |     | |            
   /  \   _ __  _ __   ___| |__   _| | ___| \  / | __ _| | _____ _ __ 
  / /\ \ | '_ \| '_ \ / _ \  __| | | |/ _ \ |\/| |/ _` | |/ / _ \ '__|
 / ____ \| | | | | | |  __/ |    | | |  __/ |  | | (_| |   <  __/ |   
/_/    \_\_| |_|_| |_|\___|_|    |_|_|\___|_|  |_|\__,_|_|\_\___|_|   \n''')

def getname():
	name = input(f'{color.PURPLE}Enter Your File Name: {color.BLACK}')
	while(name == ''):
		print(f'{color.RED}You Must Enter A Name!')
		name = input(f'{color.PURPLE}Enter Your File Name: {color.BLACK}')
	return name

def getstg():
	sg = input(f'{color.CYAN}Enter Your Data Storage Unit (e.g. KB, MB, GB, TB): {color.BLACK}')
	while(sg == ''):
		print(f'{color.RED}You Must Enter A Correct Unit!')
		sg = input(f'{color.CYAN}Enter Your Data Storage Unit (e.g. KB, MB, GB, TB): {color.BLACK}')
	if(sg == 'KB' or sg == 'MB' or sg == 'GB' or sg == 'TB'):
		return sg
	else:
		print(f'{color.RED}You Must Enter A Correct Unit!')
		return 1

def getsize():
	try:
		much = int(input(f'{color.BLUE}Enter Your Data Size: {color.BLACK}'))
		return much
	except ValueError:
		print(f'{color.RED}Please Enter A Correct Size!')
		time.sleep(1)
		return much

def getpath(name):
	path = input(f'{color.YELLOW}Type Your Path For Creating The File Or Leave It Empty: {color.BLACK}')
	if(path != ''):
		if not os.path.exists(path):
			os.makedirs(path)
			filepath = os.path.join(path, name)
			return filepath
	else:
		return path

def create():
	try:
		clean()
		banner()
		name = getname()
		clean()
		banner()
		strg = getstg()
		while(strg == 1):
			strg = getstg()
		clean()
		banner()
		size = getsize()
		while(size == None):
			size = getsize()
		clean()
		banner()
		pth = getpath(name)
		while(pth == None):
			print(f'{color.RED}Path Is Unavailbe!')
			pth = getpath(name)
		clean()
		banner()
		print(color.WHITE)
		if(pth == ''):
			with open(name, 'wb') as f:
				if(strg == 'KB'):
					print(f'{color.MAGENTA}Your File Is Makeing...!')
					f.seek(size * 1024)
					f.write(b'0')
				elif(strg == 'MB'):
					print(f'{color.MAGENTA}Your File Is Makeing...!')
					f.seek(size * 1048576)
					f.write(b'0')
				elif(strg == 'GB'):
					print(f'{color.MAGENTA}Your File Is Makeing...!')
					f.seek(size * 1073741824)
					f.write(b'0')
				elif(strg == 'TB'):
					print(f'{color.MAGENTA}Your File Is Makeing...!')
					f.seek(size * 1099511627776)
					f.write(b'0')
		else:
			with open(pth, "wb") as f:
				if(strg == 'KB'):
					print(f'{color.MAGENTA}Your File Is Makeing...!')
					f.seek(size * 1024)
					f.write(b'0')
				elif(strg == 'MB'):
					print(f'{color.MAGENTA}Your File Is Makeing...!')
					f.seek(size * 1048576)
					f.write(b'0')
				elif(strg == 'GB'):
					print(f'{color.MAGENTA}Your File Is Makeing...!')
					f.seek(size * 1073741824)
					f.write(b'0')
				elif(strg == 'TB'):
					print(f'{color.MAGENTA}Your File Is Makeing...!')
					f.seek(size * 1099511627776)
					f.write(b'0')
		clean()
		banner()
		print(f'{color.MAGENTA}Your File Is Ready!{color.WHITE}')
	except KeyboardInterrupt:
		print(f'{color.RED}\nExiting...{color.WHITE}')
		time.sleep(2)
		exit()

create()