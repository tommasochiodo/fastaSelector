import pyfasta
from pyfasta import Fasta

def fastaSubset(fastaPath, seqName, fragStart, fragEnd):
    f=Fasta(fastaPath)
    seq=f[seqName][fragStart:fragEnd]
    fasta_string = '>'+seqName+'_'+str(fragStart)+'-'+str(fragEnd)+'\n'+seq+'\n'
    return fasta_string
    
fasta=str(input('Fasta File: '))
name=str(input('Fasta Sequence: '))
start=int(input('Fragment Range Start: '))
end=int(input('Fragment Range End: '))

#fastaSubset(fasta, name, start, end)

with open('Ccap_X3_Fragments.fasta', 'a') as file:
    file.write(fastaSubset(fasta, name, start, end))
print('Done.')
