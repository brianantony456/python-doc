import bz2
import sys

opener = bz2.open
print("Access " + __file__)

# executes when executed as - to create a gzpped file
# python -m reader_doc.compressed.gzipped test.gz data compressed with gzip
if __name__ == '__main__':
    f = bz2.open(sys.argv[1], mode='wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()