from clint.textui import colored
from Graphiti.ConnectNodes import ConnectNodes
from Graphiti.GetNode import GetNode
from Helpers.GetFileActionAttributes import GetFileActionAttributes
from Bit9.CheckHash import CheckHash

class AddModulesLoadedThreatIntel(object):

	@staticmethod
	def Run(graph, timetable, report):
		print colored.yellow("[*] Adding Modules Loaded Threat Intel From Bit9.")
		for item in report['process']['modload_complete']:
			#print item
			if item.split("|")[1]!='':
				hashvalue =	item.split('|')[1]
				intelresult=CheckHash.Run(hashvalue)
				#print intelresult
				#print type(intelresult[0]['threat'])
				if len(intelresult) >= 1 and intelresult[0]['threat']==100:
					print colored.magenta("[+] Bit9 Threat Intel Hit! "+str(hashvalue))
					threatlabel=intelresult[0]['fileName']+str("-Threat=")+str(intelresult[0]['threat'])
					time = item.split("|")[0][:-4]
					modload_name = item.split("|")[2]
					time_node = GetNode.Run(graph, time, "time", float(1.0))
					threat_node = GetNode.Run(graph, threatlabel, "threat",float(5.0))
					modload_node = GetNode.Run(graph, modload_name, "modload",float(1.0))
					ConnectNodes.Run(graph, time_node, modload_node)
					ConnectNodes.Run(graph, modload_node, threat_node)
				else:
					print colored.cyan("[?] Hash not a threat, "+str(hashvalue))
					pass
		print colored.green("[+] Completed.\n")
