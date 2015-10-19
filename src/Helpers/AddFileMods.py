from clint.textui import colored
from Graphiti.ConnectNodes import ConnectNodes
from Graphiti.GetNode import GetNode
from Helpers.GetFileActionAttributes import GetFileActionAttributes
from Bit9.CheckHash import CheckHash

class AddFileMods(object):

	@staticmethod
	def Run(graph, timetable, report):
		print colored.yellow("[*] Adding file actions.")
		for item in report['process']['filemod_complete']:
			if item.split("|")[1][:-4] in timetable:
				attrs = GetFileActionAttributes.Run(int(item.split("|")[0]))
				time = item.split("|")[1][:-4]
				fmod_name = '\\'.join(str(item.split("|")[2]).split('\\')[-4:])
				time_node = GetNode.Run(graph, time, "time",float(1.0))
				fmod_node = GetNode.Run(graph, fmod_name, "file_mod",float(1.0))
				ConnectNodes.Run(graph, time_node, fmod_node, attrs)
		print colored.green("[+] Completed.\n")