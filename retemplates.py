#!/usr/bin/env python
import fileinput,re
field_pat = re.compile(r'\[(.+?)\]')
scope = {}
def replacement(match):
	code = match.group(1)
	print "code :",code
	try:
		gg = str(eval(code,scope))
		#gg = str(eval(code))
		print "result :",gg
		#print "scope :" ,scope
		return gg
	except SyntaxError:
		print 'hello'
		exec code in scope
		return ''
	
lines = []
for line in fileinput.input():
	lines.append(line)
text = ''.join(lines)
print field_pat.sub(replacement,text)
