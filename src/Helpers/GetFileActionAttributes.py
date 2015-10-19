class GetFileActionAttributes(object):

	@staticmethod
	def Run(fileaction):
		attrs={}
		if fileaction==1:
			attrs={'label': 'action', 'type': 'created'}

		if fileaction==2:
			attrs={'label': 'action', 'type': 'first-wrote'}

		if fileaction==4:
			attrs={'label': 'action', 'type': 'deleted'}

		if fileaction==8:
			attrs={'label': 'action', 'type': 'last-wrote'}

		return attrs