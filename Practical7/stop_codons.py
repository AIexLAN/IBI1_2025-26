import sys

def parse_fasta(filename):
    """
    Read a FASTA file and return a list of (header, sequence) tuples.
    The sequence is merged into a single uppercase string.
    """
    records = []
    with open(filename, 'r') as f:
        current_header = None
        current_seq = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                # Save the previous record
                if current_header is not None:
                    records.append((current_header, ''.join(current_seq)))
                current_header = line[1:]   # Remove the '>' symbol
                current_seq = []
            else:
                current_seq.append(line.upper())
        # Save the last record
        if current_header is not None:
            records.append((current_header, ''.join(current_seq)))
    return records

def get_gene_name(header):
    """
    Extract the gene name from the FASTA header line.
    Usually the first word before any space is the gene name (e.g., "YAL001C").
    """
    parts = header.split()
    return parts[0] if parts else header

def find_inframe_stop_codons(seq):
    """
    Find all types of in-frame stop codons in the sequence.
    Scan every ATG start position, then step forward by 3 codons,
    collect any TAA/TAG/TGA encountered (unique).
    Returns a set, e.g., {'TAA', 'TAG'}.
    """
    stop_codons = set()
    n = len(seq)
    # Look for every possible ATG start
    for i in range(n - 2):
        if seq[i:i+3] == 'ATG':
            # From i+3, walk in steps of 3 until the end
            for j in range(i + 3, n - 2, 3):
                codon = seq[j:j+3]
                if codon in ('TAA', 'TAG', 'TGA'):
                    stop_codons.add(codon)
                # Continue scanning because a single ORF may contain multiple stop codons
                # (even though translation stops at the first one, the task asks for all)
    return stop_codons

def main():
    # Input file name (make sure it exists in the current directory or provide full path)
    input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_file = 'stop_genes.fa'
    
    # Read the FASTA file
    try:
        records = parse_fasta(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found. Please check the file name and path.")
        sys.exit(1)
    
    # Process each record
    out_lines = []
    for header, seq in records:
        gene_name = get_gene_name(header)
        stop_set = find_inframe_stop_codons(seq)
        if stop_set:   # At least one in-frame stop codon found
            # Build new header: >gene_name stop_codon_types (comma-separated)
            stop_list = ','.join(sorted(stop_set))   # Sort for consistent output
            new_header = f">{gene_name} {stop_list}"
            out_lines.append(new_header)
            out_lines.append(seq)   # Sequence as a single line
    
    # Write output file
    with open(output_file, 'w') as f:
        f.write('\n'.join(out_lines))
    
    print(f"Processing complete. Found {len(out_lines)//2} genes containing in-frame stop codons.")
    print(f"Results saved to {output_file}")

if __name__ == '__main__':
    main()
    