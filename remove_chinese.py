import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input', type=str, help='input file name')
parser.add_argument('--cardinal', type=int, help="add from this")
parser.add_argument('--mul', type=int, help='if exact division, then remove')
args = parser.parse_args()

file = open(args.input)
new_name = args.input[:-4] + "_removed" + args.input[-4:]
fout = open(new_name, "w")
index = 0
while 1:
    line = file.readline()
    index += 1
    if not line:
        break
    if (index - args.cardinal) >= 0 and (index - args.cardinal) % args.mul == 0:
        pass
    else:
        fout.writelines(line)

file.close()
fout.close()



