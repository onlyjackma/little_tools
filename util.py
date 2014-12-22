#!/usr/bin/env python
def lines(files):
	for line in files:
		yield line
	yield "\n"

def blocks(files):
	block = []
	for line in lines(files):
		if line.strip():
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block = []
