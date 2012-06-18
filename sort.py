"""
Ver 1.0
author: Halostar
licensed under GPL
"""

#! /usr/bin/env python
from os import *
from shutil import *
import re

def main():
    #re.compile()
    #pa = '/Users/hs454/Downloads/'
    pa = getcwd()+'/'
    files = listdir(pa)
    acc=[]
    for f in files:
        appendix = f.split('.')[-1]
        if not path.isdir(pa+f):
            acc.append(appendix)
    
    acc = list(set(acc))
    acc.append('Directories')
    acc.append('No_extension')
    d = dict((e,[]) for e in acc)
  
    for f in files:
        if not f == '.DS_Store':
            splt =  f.split('.')
            appendix = splt[-1]
            if not path.isdir(pa+f) and len(splt) > 1:
                d[appendix].append(f)
            elif path.isdir(pa+f) and not re.match('^[a-zA-Z0-9]{1,4}$', f):
                d['Directories'].append(f)
            elif not path.isdir(pa+f) and len(splt) < 2:
                d['No_extension'].append(f)
                
    for appd in acc:
      if not path.exists(pa+appd) and appd != 'DS_Store':
          makedirs(pa+appd)

      fs = d[appd]
      for f in fs:
          #if not path.isdir(pa+f):
            try :
                move(pa+f , pa+appd)
            except BaseException as e:
              print 'Warnings: '  
              print e

if __name__ == '__main__':
  main()
