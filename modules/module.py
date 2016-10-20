import abc

class Module(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def shouldRespond(self, text):
		pass
	@abc.abstractmethod
	def responseMessage(self, text):
		pass