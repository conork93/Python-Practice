#Conor Kennedy
#9/30/2017
'''
Given a DNA strand, its transcribed RNA strand
is formed by replacing each nucleotide
G->C, C->G, T->A A->U
'''

dna = ['G', 'C', 'T', 'A']


def to_rna(dna):
  rna = []
  for i in dna:
    if i == 'G':
     rna.append('C')
    if i == 'C':
     rna.append('G')
    if i == 'T':
     rna.append('A')
    if i == 'A':
     rna.append('U')
  return rna
      
print(to_rna(dna))
