import subprocess

def write(s, id, loc):
	"""
	Write string s, into window id's loc file
	
	runs
		echo -n s | 9p write acme/id/loc
	"""
	out = subprocess.Popen(['echo', '-n', s], stdout=subprocess.PIPE)
	wrt = subprocess.Popen(['9p', 'write', 'acme/'+str(id)+'/'+loc], stdin=out.stdout)
	return
	
def read(id, loc):
	"""
	Read from window id's loc file
	
	runs
		9p read acme/id/loc
	returns
		utf-8 encoded string with contents of acme/id/loc
	"""
	s = subprocess.check_output(['9p', 'read', 'acme/'+str(id)+'/'+loc])
	return s.decode('utf-8')

def windownew():
	"""Create a new ACME window and return
	the window ID"""
	winid = subprocess.check_output(['9p', 'read', 'acme/new/ctl']).split()[0]
	return int(winid)
