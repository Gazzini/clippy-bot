from fox_issue_tracker import FoxIssueTracker
import requests

class JiraTracker(FoxIssueTracker):
	def shouldRespond(self, text):
		jiraIssue = self.getJiraIssueFromText(text)
		if not jiraIssue:
			return False
		request = requests.get('https://bugs.rev.com/browse/'+jiraIssue)
		if "Issue does not exist" in request.text:
			return False
		else:
			return True
	def responseMessage(self, text):
		pass
a = JiraTracker()
print(a.shouldRespond("FOX-19315 aa "))