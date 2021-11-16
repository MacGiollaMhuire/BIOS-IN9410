import sys

with open(sys.argv[1], "r") as fh:
    lines = fh.readlines()


for line in lines:
    # remove new lines
    line = line.strip()
    if line.startswith(">"):
        # record header
        header = line
    else:
        # record length of non-header
        length = len(line)
        print(length, header)
