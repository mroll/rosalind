from util import transcribe, DNACodonTable, parseFasta, fread
import re

def splc(S, introns):
    return transcribe(re.sub(r"|".join(introns), "", S), DNACodonTable)

fastas = parseFasta(fread("splc.in"))
S = fastas[0].seq
introns = map(lambda f: f.seq, fastas[1:])

print splc(S, introns)
