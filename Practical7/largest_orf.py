import re

# create a string variable seq
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# define start codon and stop codon
start_codon = "AUG"
stop_codons = ["UAA", "UAG", "UGA"]

start_positions = [m.start() for m in re.finditer(start_codon, seq)]

longest_orf_length = 0
longest_orf_sequence = ''

# Scan every position in the sequence for a start codon
for i in start_positions:
    # From this start, scan codon by codon (step 3) until stop or end
    for j in range(i+3, len(seq) - 2, 3):
        codon = seq[j:j+3]
        if codon in stop_codons:
            # ORF from i to j+2 (inclusive)
            orf_length = (j + 3) - i   # = j - i + 3
            orf_sequence = seq[i:j+3]
            if orf_length > longest_orf_length:
                longest_orf_length = orf_length
                longest_orf_sequence = orf_sequence
            break  # Stop further scanning for this start

# Output the result
print(f"Length of the longest ORF: {longest_orf_length} nucleotides")
print(f"Longest ORF sequence: {longest_orf_sequence}")