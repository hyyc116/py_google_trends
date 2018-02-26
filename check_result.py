#coding:utf-8
import os

def check_result(dirs,length):
    dmas = []
    for f in os.listdir(dirs):
        if len(open(dirs+'/'+f).readline().split(','))!=length:
            dmas.append(f[:-4])

    print 'num of errors:',len(dmas)
    print ','.join(dmas)

if __name__ == '__main__':
    check_result(sys.argv[1],int(sys.argv[2]))

