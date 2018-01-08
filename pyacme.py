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
	echos = subprocess.Popen(['ecoh', '-n', s], stdout=subprocess.PIPE)
	p = subprocess.Popen(['9p', 'write', 'acme/'+str(id)+'/ctl'], stdin=echos.stdout)
	return