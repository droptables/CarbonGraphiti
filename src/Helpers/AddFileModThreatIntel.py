from clint.textui import colored
from Graphiti.ConnectNodes import ConnectNodes
from Graphiti.GetNode import GetNode
from Helpers.GetFileActionAttributes import GetFileActionAttributes
from Bit9.CheckHash import CheckHash

class AddFileModThreatIntel(object):

	@staticmethod
	def Run(graph, timetable, report):
		print colored.yellow("[*] Adding File Modifications Threat Intel From Bit9.")
		for item in report['process']['filemod_complete']:
			if item.split("|")[3]!='':
				hashvalue =	item.split('|')[3]
				intelresult=CheckHash.Run(hashvalue)
				if intelresult[0]['threat']==0:
					print colored.cyan("[?] Hash not a threat, "+str(hashvalue))
					pass
				else:
					print colored.magenta("[+] Bit9 Thrat Intel Hit! "+str(hashvalue))
					threatlabel=intelresult[0]['fileName']+str("-Threat=")+str(intelresult[0]['threat'])
					fmod_name = '\\'.join(str(item.split("|")[2]).split('\\')[-4:])
					threat_node = GetNode.Run(graph, threatlabel, "threat",float(5.0))
					fmod_node = GetNode.Run(graph, fmod_name, "file_mod",float(1.0))
					ConnectNodes.Run(graph, fmod_node, threat_node)
		print colored.green("[+] Completed.\n")