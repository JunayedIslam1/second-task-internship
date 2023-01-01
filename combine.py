import json
files = ['pos_0.png.json', 'pos_10010.png.json', 'pos_10492.png.json']

with open('merged_file_name.json', "w") as outfile:
    outfile.write('{}'.format('\n'.join([open(f, "r").read() for f in files])))
