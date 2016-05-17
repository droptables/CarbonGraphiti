#!/usr/bin/env python
import sys
from clint.textui import colored
import semanticnet as sn
from Launch.Launch import Launch
from Carbonblack.GetProcessReport import GetProcessReport
from Helpers.CreateTimeTable import CreateTimeTable
from Helpers.CreateTimeNodes import CreateTimeNodes
from Helpers.AddFileMods import AddFileMods
from Helpers.AddRegistryMods import AddRegistryMods
from Helpers.AddNetConns import AddNetConns
from Helpers.AddFileModThreatIntel import AddFileModThreatIntel
from Helpers.AddModulesLoaded import AddModulesLoaded
from Helpers.AddModulesLoadedThreatIntel import AddModulesLoadedThreatIntel

if __name__ == '__main__':
	graph=sn.Graph()
	graph.cache_nodes_by("label")
	launch=Launch()
	if len(sys.argv) == 1:
		launch.show_options()
		sys.exit()
	launch.show_logo()
	args=launch.get_args()
	#load CB API
	cb=launch.load_config_file(args.configfile)
	#Get process report for CB link

	report=GetProcessReport.Run(cb,args.link)
	#Create a timetable
	timetable,timelist=CreateTimeTable.Run(report)
	#Create time nodes to plot process activity on
	CreateTimeNodes.Run(graph, timelist)
	#Add modules loaded to time nodes
	#AddModulesLoaded.Run(graph, timetable, report)
	#Add file modifications
	AddFileMods.Run(graph, timetable, report)
	#Add Netcons
	AddNetConns.Run(graph, timetable, report)
	#Add registry mods
	AddRegistryMods.Run(graph, timetable, report)

	if args.cbprotection:
		#Add Threat Intel from Cb Protection on file modifications
		AddFileModThreatIntel.Run(graph, timetable, report)
		#Add Threat Intel from Cb Protection on modules loaded
		AddModulesLoadedThreatIntel.Run(graph, timetable, report)


	#Save output JSON file for OpenGraphiti
	print colored.yellow("[*] Saving output file.")
	graph.save_json(args.outputfile)
	print colored.cyan("[+] Completed, output saved to "+str(args.outputfile))
