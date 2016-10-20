import random
from modules.module import TestModule

MODULES = [TestModule]

class MessageParser:

	EMOJI = [0x0001F600, 0x0001F641]

	def RandomEmoji(self, length):
		return ''.join((r'\U%08x' % random.randint(self.EMOJI[0], self.EMOJI[1])) 
			for i in range(length)).decode('unicode-escape')

	def alertModules(self, message):
		response = ""
		thisModule = TestModule()
		if thisModule.shouldRespond(message):
			response += thisModule.getResponse(message) + "\n"

		if len(response) > 0:
			return self.RandomEmoji(3) + "It looks like you referenced something I can help with!" +\
				self.RandomEmoji(3) + "\n" + response.rstrip()

		return ""
