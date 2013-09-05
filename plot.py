"""Plot gene data or dump it as JSON

Usage:
  plot.py extension file1 [file2 ...]

  If extension is json, dump the given files as JSON documents.
  Otherwise save plots of the files with the given extension, which
  must be understood by pylab.savefig.
"""

import json
import numpy as np
import pylab
import sys


def read(f):
    d = np.loadtxt(f, skiprows=1, usecols=(1, 2), unpack=True)
    return d


def plot(d, f=None, ext=None):
    pylab.figure()
    pylab.plot(d[0], d[1], '.', markersize=1)
    if f and ext:
        pylab.savefig('.'.join([f, ext]))
    else:
        pylab.show()


def dump_json(d, filename, length=1500, offset=0):
    d = d.T
    d = d[d[:, 0].argsort()]
    with open(filename+'.json', 'w') as f:
        json.dump(d[offset:offset+length].tolist(), f)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write(__doc__)
        sys.exit(1)
    ext = sys.argv[1]
    for f in sys.argv[2:]:
        d = read(f)
        if ext == 'json':
            dump_json(d, f+'.json.full', length=-1)
        else:
            plot(d, f, ext)
