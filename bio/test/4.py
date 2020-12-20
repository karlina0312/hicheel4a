from Bio import pairwise2
from Bio.pairwise2 import format_alignment
X = "ACGTCCTTCATT"
Y = "GTCTCATG"
#A match score = 2, mismatch score = -1, gap opening = -5, gap
extension = -2
alignments = pairwise2.align.globalms(X, Y, 2, -1, -5, -2)
for a in alignments:
    print(format_alignment(*a))


''' ene huu code en alignment deer tulguurlan todrohoi orj irsen string utguudiig onooltiint ovshind matrix deer suurilsan onooltoor ashiglan  -- geh meteer zoruug gargahad ashigldagaa'''    