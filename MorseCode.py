morse_dict ={
        ".-" : "A",
        "-..." : "B",
        "-.-." : "C",
        "-.." : "D",
        "." : "E",
        "..-." : "F",
        "--." : "G",
        "...." : "H",
        ".." : "I",
        ".---" : "J",
        "-.-" : "K",
        ".-.." : "L",
        "--" : "M",
        "-." : "N",
        "---" : "O",
        ".--." : "P",
        "--.-" : "Q",
        ".-." : "R",
        "..." : "S",
        "-" : "T",
        "..-" : "U",
        "...-" : "V",
        ".--" : "W",
        "-..-" : "X",
        "-.--" : "Y",
        "--.." : "Z",
        }

def validWords(morse_string, morse_dict):
	words = []
	letter = ''
	characters = list(morse_string)
	start = 0
	for i in range(len(characters)):
			letter += characters[i]
			if letter == morse_string:
				print 'hi'
				break
			word = getWord(characters, start, letter)
			if word:
				words.append(word)
	print words

def getWord(characters, start, letter):
	word = []
	for i in range(len(letter),len(characters), 1):
		letter = ''.join(characters[start:i])
		if morse_dict.get(letter, None):
			word.append(morse_dict.get(letter, None))
			start = i
			if start == len(characters) - 1:
				return ''.join(word)
	return







validWords('.-...-.', morse_dict)
