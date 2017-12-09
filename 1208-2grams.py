from urllib.request import urlopen
import re

url = "http://pythonscraping.com/files/inaugurationSpeech.txt"
text = urlopen(url).read().decode("utf8").lower()
text = re.sub("[^a-z0-9]", " ", text)
text = re.sub(" +", " ", text)
text = text.split()
bad = ["a", "about", "all", "also", "an", "and", "as", "as", "at", "be", "because", "been", "but", "by", "can", "come", "could", "day", "do", "find", "first", "for", "from", "get", "give", "go", "has", "have", "he", "her", "here", "him", "his", "how", "i", "if", "in", "into", "is", "it", "its", "just", "know", "like", "look", "make", "man", "many", "me", "more", "more", "my", "new", "no", "not", "now", "of", "on", "one", "or", "other", "our", "out", "people", "say", "see", "she", "so", "some", "take", "than", "that", "that", "the", "their", "them", "then", "there", "these", "they", "thing", "think", "this", "time", "to", "two", "up", "use", "want", "way", "we", "well", "what", "when", "which", "who", "will", "with", "would", "year", "you", "your"]

dic = {}
for i in range(len(text)-1):
	w = text[i]+" "+text[i+1]
	if text[i] in bad or text[i+1] in bad:
		continue
	if not w in dic:
		dic[w] = 0
	dic[w] += 1
dic = sorted(dic.items(), key=lambda v:v[1])
for v in dic:
	print(v[0], v[1])
