from Bio.Align import PairwiseAligner

def pairwise_alignment(seq1, seq2):
    aligner = PairwiseAligner()
    alignments = aligner.align(seq1, seq2)
    best_alignment = alignments[0]
    alignment_score = best_alignment.score
    aligned_seq1 = best_alignment.aligned[0]
    aligned_seq2 = best_alignment.aligned[1]
    return aligned_seq1, aligned_seq2, alignment_score


def star_alignment(sequences):
    """
    Perform Multiple Sequence Alignment using Star Alignment.
    """
    # Initialize the alignment with the first sequence
    alignment = sequences[0]
    # Iterate through the remaining sequences
    for seq in sequences[1:]:
        best_score = float('-inf')
        best_alignment = None
        # Find the best position to insert the sequence
        for i in range(len(alignment) + 1):
            temp_alignment = alignment[:i] + seq + alignment[i:]
            score_sum = 0
            # Compute the alignment score with each sequence in the alignment
            for aligned_seq in alignment:
                _, _, score = pairwise_alignment(temp_alignment, aligned_seq)
                score_sum += score
            # Update the best alignment if the current score is higher
            if score_sum > best_score:
                best_score = score_sum
                best_alignment = temp_alignment
        # Update the final alignment with the best alignment found
        alignment = best_alignment
    return alignment, best_score


sequences = [
    "ATTGCCATT",
    "ATGGCCATT",
    "ATCCAATTTT",
    "ATCTTCTT",
    "ACTGACC"
]


final_alignment, final_score = star_alignment(sequences)

# Print 
print("Secuencia Final:")
for seq in final_alignment:
    print(seq)
print("Score:", final_score)
