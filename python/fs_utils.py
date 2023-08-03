import os
import sys

# UE5 tool: prints all uassets from the 'ifolder' into 'ofile'.
def print_dir(ifolder, ofile='assets.txt'):
	sys.original_stdout = sys.stdout
	with open(ofile, 'w') as f:
		sys.stdout = f
		dirs = []
		dirs.append(ifolder)
		while len(dirs):
			elements = os.scandir(dirs.pop(len(dirs)-1))
			for element in elements:
				if element.is_dir():
					dirs.append(element.path)
				elif element.name.endswith('.uasset'):
					print(element.path)
		sys.stdout = sys.original_stdout

# Prints all common strings from if1 and if2 files into 'ofile'.
def file_intersection(if1, if2, ofile = 'files.intersection'):
	if1_lines = open(if1, 'r').readlines()
	if2_lines = open(if2, 'r').readlines()
	sys.original_stdout = sys.stdout
	with open(ofile, 'w') as f:
		sys.stdout = f
		for line in [value for value in if1_lines if value in if2_lines]:
			print(line)
		sys.stdout = sys.original_stdout