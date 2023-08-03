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
				elif element.name.endswith(".uasset"):
					print(element.path)
		sys.stdout = sys.original_stdout

