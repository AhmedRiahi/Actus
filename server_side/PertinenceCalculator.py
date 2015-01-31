import re
from collections import Counter

class PertinenceCalculator:

	separators = [',','.',';','!',"?",':',"'","...","|","(",")","-","_","$","#"]
	stopWordLength = 5

	def rank(self,text):
		text = self.cleanText(text)
		tokens = self.tokenize(text)
		ranks = Counter(tokens)
		return ranks

	def tokenize(self,text):
		tokens = text.split()
		return tokens


	def cleanText(self,text):
		cleanedText = ''
		for e in text:
			if e.isalnum() or e == ' ':
				cleanedText += e
			else:
				cleanedText += ' '

		expression = r'\b\w{0,'+re.escape(str(self.stopWordLength))+r'}\b'
		cleanedText = re.sub(expression,'',cleanedText)
		cleanedText = re.sub('[ ]{2,}',' ',cleanedText)
		return cleanedText


