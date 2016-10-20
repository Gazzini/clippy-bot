import abc
from module import Module
import re
import requests

class FoxIssueTracker(Module):
	def getJiraIssueFromText(self, text):
		issue = re.search('(?:^|\s)(FOX|TUT)-(\+?\d+)(?:\s|$)', text)
		if not issue:
			return issue
		return issue.group().strip()

	def shouldRespond(self, text):
		pass
	def responseMessage(self, text):
		pass