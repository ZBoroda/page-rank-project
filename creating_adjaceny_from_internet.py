import numpy as np


"""
Function to make an adjacency matrix from two dictionaries: the adjancency list and a dictionary which maps each site in the adjacency list (our internet) to a distinct integer

    First, we create a square zero matrix the size of our adjacency matrix.
    For each possible site in our internet, we will check if it links to any other sites based on our adjacency list. 
    Then, we locate all of the links between sites and write a one in the associated cell in the adjacency matrix.
    Return the finished adjacency matrix.
"""


def makeAdjacencyMatrix(a_list, disct_columns):
    adjacency = np.zeros((len(disct_columns), len(disct_columns)))
    for key, indexColumn in disct_columns.items():
        if (key in a_list):
            for value in a_list[key]:
                adjacency[disct_columns[value], indexColumn] = 1
    return adjacency


"""
Function to to make the dictionary that associates each site with an integer, taking the adjacency list (dictionary) as an input

    First, we will initialize a counter which will give us unique values and initialize a dictionary of sites.
    Now, we will iterate of the items in our adjacency list, and if it isn't in our dictionary of site, we give it the value and increment the counter.
    Return the dictionary of sites.
    
This function is maninly used to be able to find out which site is which in the adjancy matrix and page ranked list
"""


def makeColumnsDict(dictionary):
    columns = {}
    cnt = 0
    for key, elements in dictionary.items():
        if key not in columns.keys():
            columns.setdefault(key, cnt)
            cnt += 1
        for element in elements:
            if element not in columns.keys():
                columns.setdefault(element, cnt)
                cnt += 1
    return columns


"""
Function to make the adjacency list from a data frame, in which each row is a pair of a site (source domain) and one it links to (target domain)

    We will make a dictionary where the index points to the pairs.
    Now, we will initialize an empty dictionary.
    For each pair, if the source domain is not in the dictionary, we initialize a new list it will be linking to through the dictionary.
    Then, we will add the target domain to the dictionary with the key value being the source domain.
    Return the finished adjacency list (internetDict)
    
    
"""


def makeAdjacencyList(pandasDataFrame):
    internetDictList = pandasDataFrame.to_dict('records')
    internetDict = {}
    for i in range(len(internetDictList)):
        internetDict.setdefault(internetDictList[i]['SOURCE DOMAIN'], [])
        internetDict[internetDictList[i]['SOURCE DOMAIN']].append(internetDictList[i]['TARGET DOMAIN'])
    return internetDict


