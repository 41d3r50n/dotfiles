import sys

# returns one of -2, -1, 1, 2 depending on whether string[index] should be replaced with '\[', '\(', '\)' or '\]'
def dollar_pos(index, string):
	single_dollar_inds = []
	double_dollar_inds = []

	for i in range(len(string) - 1):
		if string[i] == '$' and (string[i+1] != '$' and string[i-1] != '$'):
			single_dollar_inds.append(i)
		elif string[i] == string[i+1] == '$':
			l = list()
			l.append(i)
			l.append(i+1)
			double_dollar_inds.append(l)


	print(single_dollar_inds, double_dollar_inds)
	
	for i in range(len(single_dollar_inds)):
		if index == single_dollar_inds[i]:
			if i%2 == 0:
				return -1
			else:
				return 1

	for i in range(len(double_dollar_inds)):
		if index in double_dollar_inds[i]:
			if i%2==0:
				return -2
			else:
				return 2

def math_mode(code):
	if code == -2:
		return '\['
	elif code == 2:
		return '\]'
	elif code == -1:
		return '\('
	elif code == 1:
		return '\)'

def cleaner(s):
	s_cleaned = ""

	for i in range(len(s)):
		if s[i] != '$':
			s_cleaned += s[i]
		elif s[i] == s[i-1] == '$':
			continue
		else:
			s_cleaned += math_mode(dollar_pos(i,s))

	return s_cleaned

def main():
	s = str(input("Enter LaTeX:\n"))
	print(cleaner(s))

if __name__ == "__main__":
	main()
