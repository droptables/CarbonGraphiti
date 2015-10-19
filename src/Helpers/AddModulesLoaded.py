from clint.textui import colored
from Graphiti.ConnectNodes import ConnectNodes
from Graphiti.GetNode import GetNode
from Bit9.CheckHash import CheckHash

class AddModulesLoaded(object):

	@staticmethod
	def Run(graph, timetable, report):
		print colored.yellow("[*] Adding Modules Loaded actions.")
		for item in report['process']['modload_complete']:
			 if item.split("|")[0][:-4] in timetable:
				time = item.split("|")[0][:-4]
				time_node = GetNode.Run(graph, time, "time", float(1.0))
				modload_name = item.split("|")[2]
				modload_node = GetNode.Run(graph, modload_name, "modload",float(1.0))
				ConnectNodes.Run(graph, time_node, modload_node)
		print colored.green("[+] Completed.\n")