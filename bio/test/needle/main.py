# Here's how to make the matrix above from a list of lists
my_matrix = []
# Fill out the 0th row
my_matrix.append([1, 3, 5, 7])
# Fill out the 1st row
my_matrix.append([2, 3, 4, 5])
# Fill out the 2nd row
my_matrix.append([5, 2, 20, 3])

# Here is a helper function to print out matrices
def print_matrix(mat):
    # Loop over all rows
    for i in range(0, len(mat)):
        print("[", end = "")
        # Loop over each column in row i
        for j in range(0, len(mat[i])):
            # Print out the value in row i, column j
            print(mat[i][j], end = "")
            # Only add a tab if we're not in the last column
            if j != len(mat[i]) - 1:
                print("\t", end = "")
        print("]\n")

print_matrix(my_matrix)

# To retrieve the value from the 2nd row, in the 0th column, is relatively simple:
print("The value in the 2nd row and the 0th column is:", my_matrix[2][0])

# The format is always my_matrix[row][column].
# Use these values to calculate scores
gap_penalty = -1
match_award = 1
mismatch_penalty = -1

# Make a score matrix with these two sequences
seq1 = "PRETTY"
seq2 = "PRTTEIN"

# A function for making a matrix of zeroes
def zeros(rows, cols):
    # Define an empty list
    retval = []
    # Set up the rows of the matrix
    for x in range(rows):
        # For each row, add an empty list
        retval.append([])
        # Set up the columns in each row
        for y in range(cols):
            # Add a zero to each column in each row
            retval[-1].append(0)
    # Return the matrix of zeros
    return retval

# A function for determining the score between any two bases in alignment
def match_score(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return mismatch_penalty

# The function that actually fills out a matrix of scores
def needleman_wunsch(seq1, seq2):
    
    # length of two sequences
    n = len(seq1)
    m = len(seq2)  
    
    # Generate matrix of zeros to store scores
    score = zeros(m+1, n+1)
   
    # Calculate score table
    
    # Your code goes here
    
    # Fill out first column
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    
    # Fill out first row
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    
    # Fill out all other values in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the score by checking the top, left, and diagonal cells
            match = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            # Record the maximum score from the three possible scores calculated above
            score[i][j] = max(match, delete, insert)

    return score

print_matrix(needleman_wunsch(seq1, seq2))


def locations(s_and_t):
    results = []

    s, t = s_and_t.split()
    l = len(t)

    for i in range(len(s) - l):
        if s[i:i+l] == t:
            results.append(i + 1)

    return results


if __name__ == "__main__":

    sequences = [ 
        'tagtggtcttttgagtgtagatccgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat', 
        'cgcgactcggcgctcacagttatcgcacgtttagaccaaaacggagttagatccgaaactggagtttaatcggagtcctt', 
        'gttacttgtgagcctggttagatccgaaatataattgttggctgcatagcggagctgacatacgagtaggggaaatgcgt', 
        'aacatcaggctttgattaaacaatttaagcacgtagatccgaattgacctgatgacaatacggaacatgccggctccggg', 
        'accaccggataggctgcttattagatccgaaaggtagtatcgtaataatggctcagccatgtcaatgtgcggcattccac', 
        'tagatccgaatcgatcgtgtttctccctctgtgggttaacgaggggtccgaccttgctcgcatgtgccgaacttgtaccc', 
        'gaaatggttcggtgcgatatcaggccgttctcttaacttggcggtgtagatccgaacgtctctggaggggtcgtgcgcta', 
        'atgtatactagacattctaacgctcgcttattggcggagaccatttgctccactacaagaggctactgtgtagatccgaa', 
        'ttcttacacccttctttagatccgaacctgttggcgccatcttcttttcgagtccttgtacctccatttgctctgatgac', 
        'ctacctatgtaaaacaacatctactaacgtagtccggtctttcctgatctgccctaacctacaggtagatccgaaattcg'
        ]

    results = locations(sequences)

    print (' '.join(map(str, results)))