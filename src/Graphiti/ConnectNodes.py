

class ConnectNodes(object):
	
	@staticmethod
	def Run(graph, src, dst, attrs={}):
	    if src != None and dst != None:
	        graph.add_edge(src, dst, attrs)