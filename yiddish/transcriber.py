import re
import alefbeys as a

def normalize(word):
"""Since not all texts in Yiddish are normalized and
   the inbuilt normalize function from unicodedata does not work
   for Yiddish this normalizes combined characters."""
	for i in range(len(word)):
		word = re.sub("אַ", "אַ", word)
		word = re.sub("ײַ", "ײַ", word)
		word = re.sub("אָ", "אָ", word)
		word = re.sub("בּ", "בּ", word)
		word = re.sub("וּ", "וּ", word)
		word = re.sub("כּ", "כּ", word)
		word = re.sub("פּ", "פּ", word)
		word = re.sub("תּ", "תּ", word)
		word = re.sub("בֿ", "בֿ", word)
		word = re.sub("פֿ", "פֿ", word)
		word = re.sub("יִ", "יִ", word)
		word = re.sub("שׂ", "שׂ", word)
		word = re.sub("יי", "ײ", word)
		word = re.sub("וו", "װ", word)
	return word

def transliterate(word):
	"""Transliterates a yiddish word according to the YIVO norm."""
	l_word = list(word)
	res = ""
	for i, letter in enumerate(l_word):
		if i == 0 and letter == "י":
			res += "y"	
		elif i < len(word) - 1 and l_word[i:i + 2] == ["ז", "ש"]:
			res += "zh"
			del l_word[i:i + 2]
		elif not letter in a.ALEFBEYS:
			res += letter
		else:
			res += a.ALEFBEYS[letter]
	return res		

file_name = input("Enter the name of the .txt file with text to transliterate: ")
in_list = list(map(lambda x: normalize(x), open(file_name).read().split()))
output = open("%s_transliterated.txt" %re.sub('.txt', '', file_name), "w")

for i, token in enumerate(in_list):
	if len(token) == 1 and not token in a.ALEFBEYS:
		output.write(token)
	else:
		output.write(transliterate(token))
		output.write(" ")
output.close()

