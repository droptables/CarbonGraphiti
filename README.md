CarbonGraphiti turns Carbon Black process reports into a format that can be rendered by opengraphiti.com

![Example Process](https://raw.githubusercontent.com/droptables/community-1/master/cb/CarbonGraphiti/imgs/CB-Example.png "Example Process")

```
usage: ./Carbon-Graphiti -l https://cb-server-url.com/#analyze/00001b23-0000-1fd4-01d0-d69a136419e0/1 -c cb-server.config -o output-name.json


Plot process activity by time nodes:
	-Modules Loaded
	-File Modifications
	-Registry Edits
	-Network Connections
	-Threat Intel


Tool is used to help explore the "Molecular Makeup" of malicous process activities.  View threats in a new way in order to better threat hunting techniques and spot new indicators.