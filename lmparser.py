#!/usr/bin/python
import os, re, sys, getopt
lmstat="/path/to/flexlm/lmutil"
opts="lmstat"

def print_usage():
	print "Usage:"
	print os.path.basename(__file__), '-f <feature> -c <lic_server>'

def main(argv):
	lic_server = ''
	feature = ''
	try:
		opts, args = getopt.getopt(argv,"hf:c:",["feature=","lic_server="])
		# Parse options
		for opt, arg in opts:
			if opt == '-h':
				print_usage()
				sys.exit()
			elif opt in ("-f", "--feature"):
				feature = arg
			elif opt in ("-c", "--lic_server"):
				lic_server = arg
		if not feature and not lic_server:
			raise getopt.GetoptError("")
	except getopt.GetoptError:
		print_usage()
		sys.exit(2)

	# Spawn lmutil
	licenses=os.popen("%s %s -a -c %s -f %s" % (lmstat, opts, lic_server, feature))
	# Parse lines
	for line in licenses:
		if re.search("^Users of " + feature + ":.*$", line):
			# Test for line (Total of # licenses issued;  Total of # licenses in use)
			m=re.findall("([0-9]+) license", line)
			if m and len(m) == 2:
				free=int(m[0])-int(m[1])
				# Return free licences
				print free


if __name__ == "__main__":
   main(sys.argv[1:])
