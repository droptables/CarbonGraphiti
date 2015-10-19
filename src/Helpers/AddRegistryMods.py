from clint.textui import colored
from Graphiti.ConnectNodes import ConnectNodes
from Graphiti.GetNode import GetNode
from Helpers.GetRegistryActionAttributes import GetRegistryActionAttributes


class AddRegistryMods(object):

	@staticmethod
	def Run(graph, timetable, report):
		print colored.yellow("[*] Adding registry actions.")
		try:
			for item in report['process']['regmod_complete']:
				 if item.split("|")[1][:-4] in timetable:
					attrs = GetRegistryActionAttributes.Run(int(item.split("|")[0]))
					time = item.split("|")[1][:-4]
					time_node = GetNode.Run(graph,time, "time",float(1.0))
					rmod_name = '\\'.join(str(item.split("|")[2]).split('\\')[-4:])
					rmod_node = GetNode.Run(graph,rmod_name, "reg_mod",float(1.0))
					ConnectNodes.Run(graph, time_node, rmod_node, attrs)
			print colored.green("[+] Completed.\n")
		except:
			print colored.red("[-] No Registry Activity")