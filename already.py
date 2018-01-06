#coding:utf-8

for line in open(sys.argv[1]):
    line = line.strip()
    fid = line.split(":")[-1].split('.')[0].strip()
    print sys.argv[2]+"_"+fid