#!/usr/bin/python

import sys
from os import system, remove
from tempfile import mkstemp
import random

from pyPdf import PdfFileWriter, PdfFileReader

# read input pdf and instantiate output pdf
output = PdfFileWriter()
input1 = PdfFileReader(file(sys.argv[1],"rb"))

# construct and shuffle page number list
pages = list(range(input1.getNumPages()))
random.shuffle(pages)

# display new sequence
print 'Reordering pages according to sequence:'
print pages

# add the new sequence of pages to output pdf
if len(pages) > 0:
    output.addPage(input1.getPage(pages[0]))

# write the output pdf to file

[fh, tmpfile] = mkstemp(suffix='.pdf')
print tmpfile

outputStream = file(tmpfile, 'wb')
output.write(outputStream)
outputStream.close()

system('/usr/bin/open -a Preview ' + tmpfile)
#remove(tmpfile)
#system('open ' + tmpfile)
