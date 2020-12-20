#!/usr/bin/python

from rosalind_utils import parse_fasta

def semiglobal_align(s, t):
    # Initialize the distance and traceback matrices with zeros.
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    traceback = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

    # Fill in the matrices.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            scores = [d[i-1][j] - 1,
                      d[i][j-1] - 1,
                      d[i-1][j-1] + [-1, 1][s[i-1] == t[j-1]]]
            d[i][j] = max(scores)
            traceback[i][j] = scores.index(d[i][j])

    # The max score can be found either along the last column or last row.
    last_row = d[-1]
    last_col = [d[i][-1] for i in range(len(d))]

    if max(last_row) >= max(last_col):
        i = len(s)
        j = last_row.index(max(last_row))
    else:
        i = last_col.index(max(last_col))
        j = len(t)
        
    max_score = d[i][j]
    
    # Initialize the aligned strings as the input strings.
    s_align, t_align = s, t

    # Append insertions/deletions as necessary.
    for dash in range(len(s) - i):
        t_align += '-'
    for dash in range(len(t) - j):
        s_align += '-'
    
    # Traceback to the matrix edge starting at the index of the max score.
    while i>0 and j>0:
        if traceback[i][j] == 0:
            i -= 1
            t_align = t_align[:j] + '-' + t_align[j:]
        elif traceback[i][j] == 1:
            j -= 1
            s_align = s_align[:i] + '-' + s_align[i:]
        else:
            i -= 1
            j -= 1

    # Prepend insertions/deletions as necessary.
    for dash in range(i):
        t_align = t_align[:0] + '-' + t_align[0:]
    for dash in range(j):
        s_align = s_align[:0] + '-' + s_align[0:]

    return str(max_score), s_align, t_align

   
def main():
    s, t = parse_fasta('./rosalind_smgb.txt')
    alignment = semiglobal_align(s, t)

    with open('./rosalind_smgb_out.txt', 'w') as outfile:
        outfile.write('\n'.join(alignment))

    print('Maximum alignment score =', alignment[0])
        
   
if __name__ == '__main__':
    main()
