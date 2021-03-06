import random
from modules.jira_tracker import JiraTracker

MODULES = []

class MessageParser:

	EMOJI = [0x0001F600, 0x0001F64F]

	def __init__(self, slackEmoji):
		self.slackEmoji = slackEmoji

	def RandomEmoji(self, length):
		return ''.join((r'\U%08x' % random.randint(self.EMOJI[0], self.EMOJI[1])) 
			for i in range(length)).decode('unicode-escape')

	def RandomSlackEmoji(self, length):
		return ''.join(':' + random.choice(self.slackEmoji) + ':'
			for i in range(length))

	def alertModules(self, message):
		response = ""
		thisModule = JiraTracker()
		if thisModule.shouldRespond(message):
			response += thisModule.getResponse(message) + "\n"

		if len(response) > 0:
			return self.RandomEmoji(3) + "It looks like you referenced something I can help with!" +\
				self.RandomEmoji(3) + "\n" + response.rstrip() + "\n" + self.RandomSlackEmoji(22)

		return ""
