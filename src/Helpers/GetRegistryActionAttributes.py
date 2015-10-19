class GetRegistryActionAttributes(object):

	@staticmethod
	def Run(regaction):
		attrs={}
		if regaction==1:
			attrs={'label': 'action', 'type': 'created'}

		if regaction==2:
			attrs={'label': 'action', 'type': 'first-wrote'}

		if regaction==4:
			attrs={'label': 'action', 'type': 'deleted-key'}

		if regaction==8:
			attrs={'label': 'action', 'type': 'deleted-value'}

		return attrs