from util import parseFasta, flines, motif_pos
import re
import urllib.request

N_glycosylation = r'N[^P][ST][^P]'

def dl_protein_fasta(url):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')

def print_motif_pos(protein, data, motif):
    res = motif_pos(data, motif)
    if res != []:
        print(protein)
        print(' '.join(map(str, res)))


lines = flines('mprt.in')

for protein in lines:
    url = 'http://www.uniprot.org/uniprot/' + protein + '.fasta'
    data = parseFasta(dl_protein_fasta(url))[0].seq

    print_motif_pos(protein, data, N_glycosylation)
