# Use the subprocess module to execute a command like  netstate  and the  re  (regular expression) module 
# to search/extract information from its output.   This is to find out if a port has more than 7 connections, and 
# if so, clean up the connections for the port.


import subprocess
import re

def netstat_conns():
		''' http://docs.python.org/3/library/subprocess.html#  '''
		## call netstate and parse it's output
		lines = subprocess.check_output(["netstate","-pNnt4"],universal_newlines=True)
		# netstate flags
		# p		process
		# t 		tcp
		# 4		ipv4
		# N		numerical hosts
		# n		numerical ports
		
		for line in lines, splitlines()[2]:
				yield line

if _name_ == '_main_':
		count = dict()		# used to store total connections for (host, port) tuple
		proc_map = dict()		# used to map (host, port) to process pid
		
		for conn in netstate_conns():
				''' regular expression to match host:port (anything) ESTABLISHED  pid/process_name  '''
				R = 
re.search(r '(?P<local_host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?P<local_port>\d{1,5}).*ESTABLISHED(?P<pid>\d{2,6})/(?P<process>\w+)', conn)
				## regular expression to extract established connections
				## see: https://docs.python.org/2//library/re.html 
				if R:
						host_port = (R.group('local_host'), R.group('local_port'))		# tuple (host, port)
						prev = count.get(host_port, 0)
						if host_port not in proc_map:
								proc_map[host_port] = R.group('pid')
								
				print(count)
				print(proc_map)
				
				for hp, cnt in count.item():
						if cnt >= 7:
								pid = proc_map[hp]
										## kill pid 
										
										


	
