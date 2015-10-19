from clint.textui import colored
from Graphiti.ConnectNodes import ConnectNodes
from Graphiti.GetNode import GetNode


class AddNetConns(object):

	@staticmethod
	def Run(graph, timetable, report):
		print colored.yellow("[*] Adding Network Connection activity.")

		try:
			for item in report['process']['netconn_complete']:
				print item
				if item.split("|")[0][:-4] in timetable:
					time = item.split("|")[0][:-4]
					time_node = GetNode.Run(graph,time, "time",float(1.0))
					netconn_name = item.split("|")[4]
					netconn_node = GetNode.Run(graph,netconn_name, "netconn",float(1.0))
					ConnectNodes.Run(graph, time_node, netconn_node, attrs={})
			print colored.green("[+] Completed.\n")
		except:
			print colored.red("No Network Connections.")
			pass