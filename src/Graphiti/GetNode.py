class GetNode(object):

	@staticmethod
	def Run(graph,nodelabel, nodetype, size):
	    node = graph.get_nodes_by_attr("label", nodelabel, nosingleton=True)
	    if not node:
	        return graph.add_node({"label": nodelabel, "type": nodetype, "og:space:size":size})

	    return node["id"]