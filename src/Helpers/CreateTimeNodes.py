from clint.textui import colored
from Graphiti.ConnectNodes import ConnectNodes
from Graphiti.GetNode import GetNode

class CreateTimeNodes(object):

	@staticmethod
	def Run(graph, timelist):
		print colored.yellow("[*] Creating time nodes.")
		ConnectNodes.Run(graph, GetNode.Run(graph,timelist[0], 'time',float(3.0)), GetNode.Run(graph,timelist[1],'time',float(1.0)),{'label': 'time', 'type': 'timestamp', 'og:space:activity':float(1.0)})
		ConnectNodes.Run(graph, GetNode.Run(graph,timelist[-1], 'time',float(3.0)), GetNode.Run(graph,timelist[-2],'time',float(1.0)),{'label': 'time', 'type': 'timestamp', 'og:space:activity':float(1.0)})

		for x in range(1,len(timelist)-2):
			ConnectNodes.Run(graph, GetNode.Run(graph,timelist[x], 'time',float(1.0)), GetNode.Run(graph,timelist[x+1],'time',float(1.0)),{'label': 'time', 'type': 'timestamp', 'og:space:activity':float(1.0)})

		print colored.green("[+] Completed.\n")