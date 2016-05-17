CarbonGraphiti turns Carbon Black process reports into a format that can be rendered by opengraphiti.com

![Example Process](https://raw.githubusercontent.com/droptables/CarbonGraphiti/master/imgs/CB-Example.png "Example Process")

```
usage: 
./Carbon-Graphiti.py -l https://cb-server-url.com/#analyze/00001b23-0000-1fd4-01d0-d69a136419e0/1 -c servers.config -o output-name.json


Plot process activity by time nodes:
	-Modules Loaded
	-File Modifications
	-Registry Edits
	-Network Connections
	-Threat Intel


Tool is used to help explore the "Molecular Makeup" of malicous process activities.  
View threats in a new way in order to better threat hunting techniques and spot new indicators.
More to come...

## Configuration file format

The configuration file is a simple text file, with one entry per line:

Line 1 contains the URL to the Carbon Black Enterprise Response server
Line 2 contains the API token for the Carbon Black Enterprise Response server


