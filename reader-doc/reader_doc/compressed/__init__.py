from reader_doc.compressed.bzipped import opener as bz2_opener
from reader_doc.compressed.gzipped import opener as gzip_opener
# Controlling imports with __all__
# this way the actual module names are not exposed
__all__ = ['bz2_opener']