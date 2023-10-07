#!/usr/bin/env python

import pysam
import sys
from array import array


def markreads(bamfn, fasta_ref, outfn, tag):
    bam = pysam.AlignmentFile(bamfn, reference_filename=fasta_ref)
    out = pysam.AlignmentFile(outfn, 'wb', template=bam)

    for read in bam.fetch(until_eof=True):
        tags = read.tags
        tags.append(('BS',1))
        read.tags = tags
        read.set_tag('BS',tag,'Z')
        out.write(read)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        markreads(*sys.argv[1:])

    else:
        sys.exit('usage: %s <input BAM> <output BAM>' % sys.argv[0])
            
