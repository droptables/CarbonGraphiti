from clint.textui import colored

class CreateTimeTable(object):
	
	@staticmethod
	def Run(report):
		print colored.yellow("[*] Creating time table.")
		timelist=[]
		timetable={}

		for item in report['process'].get('filemod_complete', []):
			timelist.append(item.split("|")[1][:-4])

		try:	
			for item in report['process'].get('regmod_complete', []):
				timelist.append(item.split("|")[1][:-4])
		except:
			print colored.red("[-] No registry modifications made.")
			pass

		try:
			for item in report['process'].get('netconn_complete', []):
				timelist.append(item.split("|")[0][:-4])
		except:
			print colored.red("[-] No network connections found in process report.")
			pass

		for item in report['process'].get('modload_complete', []):
			timelist.append(item.split("|")[0][:-4])

		timelist=sorted(set(timelist))
		for time in timelist:
			#print datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
			timetable[time]=[]
		print colored.green("[+] Completed.\n")
		return timetable,timelist
