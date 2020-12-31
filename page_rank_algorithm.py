
"""
Function to make weighted adjaceny matrix with a matrix as the input.

    Cast the matrix as floating point values.
    For each column, we are counting the total links (n).
    If there are no links, we make this column link to every other, so the value of n is the dimension of the matrix.
    Then, divide each value in each column by the n value for that column.
    Return the weighted matrix.
"""


def makeWeightedAdjacency(a):
    a = a.astype(float)
    for i in range(a.shape[1]):
        total_links = 0
        for j in range(a.shape[0]):
            if a[j, i] != 0:
                total_links += 1
        if total_links == 0:
            a[:, i] = a[:, i] + 1/a.shape[0]
        else:
            a[:, i] = a[:, i]/total_links
    return a


"""
The Page Rank function takes inputs: an adjacency matrix A of a graph, the number of iterations for the power method of finding eigenvectors, the probability value, and the initial guess vector, v.

    First, we call the previous function to turn our adjacency matrix into the weighted adjacency matrix.
    Then, we create the Google matrix G based off of the paper (http://www.ams.org/publicoutreach/feature-column/fcarc-pagerank).
    Next, we use the power method to find eigenvector using our initial guess, v.
"""


def pagerank(a, v, num_iterations = 100, alpha = 0.85):
    m = makeWeightedAdjacency(a)
    # print(np.linalg.eig(A)[1][:,0] / np.linalg.norm(np.linalg.eig(A)[1][:,0],1))
    g = (alpha * m + (1 - alpha) / m.shape[1])
    for i in range(num_iterations):
        v = g @ v
    return v
