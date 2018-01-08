import subprocess

def windownew():
	"""Create a new ACME window and return
	the window ID"""
	winid = subprocess.check_output(['9p', 'read', 'acme/new/ctl']).split()[0]
	return int(winid)
	
def writebody(id, s):
	"""Write to the body of a window"""
	echos = subprocess.Popen(['echo', '-n', s], stdout=subprocess.PIPE)
	subprocess.Popen(['9p', 'write', 'acme/'+str(id)+'/body'], stdin=echos.stdout)
	return

def writectl(id, s):
	"""Write to the ctl of a window"""
	echos = subprocess.Popen(['echo', '-n', s], stdout=subprocess.PIPE)
	p = subprocess.Popen(['9p', 'write', 'acme/'+str(id)+'/ctl'], stdin=echos.stdout)
	return
	
def writedata(id, s):
	"""Write to the data of a window"""
	echos = subprocess.Popen(['echo', '-n', s], stdout=subprocess.PIPE)
	p = subprocess.Popen(['9p', 'write', 'acme/'+str(id)+'/data'], stdin=echos.stdout)
	return
	
def writeaddr(id, s):
	"""Write to the addr of a window"""
	echos = subprocess.Popen(['echo', '-n', s], stdout=subprocess.PIPE)
	p = subprocess.Popen(['9p', 'write', 'acme/'+str(id)+'/addr'], stdin=echos.stdout)
	return
	
def readbody(id):
	"""Read from the body of a window"""
	s = subprocess.check_output(['9p', 'read', 'acme/'+str(id)+'/body'])
	return s.decode('utf-8')

def readctl(id):
	"""Read from the ctl of a window"""
	s = subprocess.check_output(['9p', 'read', 'acme/'+str(id)+'/ctl'])
	return s.decode('utf-8')

def readaddr(id):
	"""Read from the addr of a window"""
	s = subprocess.check_output(['9p', 'read', 'acme/'+str(id)+'/addr'])
	return s.decode('utf-8')

def readdata(id):
	"""Read from the data of a window"""
	s = subprocess.check_output(['9p', 'read', 'acme/'+str(id)+'/addr'])
	return s.decode('utf-8')