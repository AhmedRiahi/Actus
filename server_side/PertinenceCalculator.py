import re
from collections import Counter

class PertinenceCalculator:

	separators = [',','.',';','!',"?",':',"'","...","|","(",")"]
	stopWordLength = 4

	def rank(self,text):
		text = self.cleanText(text)
		tokens = self.tokenize(text)
		ranks = Counter(tokens)
		return ranks

	def tokenize(self,text):
		tokens = text.split()
		return tokens


	def cleanText(self,text):
		text = re.sub('('+str(self.separators)+')',' ',text)
		expression = r'\b\w{1,'+re.escape(str(self.stopWordLength))+r'}\b'
		text = re.sub(expression,'',text)
		text = re.sub('[ ]{2,}',' ',text)
		return text


