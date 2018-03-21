
# coding: utf-8


#put imports here
import codecs
import networkx as nx
import unicodecsv
import cPickle


#load the necessary data
fin = open('family_trees.dat','rb')
full_tree,bib_tree = cPickle.load(fin)
fin.close()

#function to calculate distance
def distance(source,sink,bibles_only = True):
    #select graph
    if bibles_only:
        tree = bib_tree
    else:
        tree = full_tree

    #get tree depth for normalization - depth of the nearest common ancestor
    sod = nx.shortest_path(tree,'ROOT',source) #path to source
    sid = nx.shortest_path(tree,'ROOT',sink) #path to sink
    depth = min(len(sod),len(sid)) #max depth
    norm = 0.0
    for i in range(depth):
        if sod[i] != sid[i]:
            break
        norm += 1

    #get normalized tree distance
    dist = len(nx.shortest_path(tree,source,sink))/norm
    return dist


#function to calculate nearest neighbor
def nearest(source,bibles_only = True):
    #select graph
    if bibles_only:
        tree = bib_tree
    else:
        tree = full_tree

    #get a directed tree to find the leaves (the other viable ISO codes)
    dG = nx.dfs_tree(tree,'ROOT')
    leaves = [node for node in dG.nodes() if dG.in_degree(node)!=0 and dG.out_degree(node)==0]
    leaves.remove(source)

    #find the distance to all other nodes from the rouce
    spaths = nx.single_source_shortest_path(tree,source)

    #check which of the leaves is the best
    bestd = len(spaths[leaves[0]])
    best = leaves[0]
    for l in leaves:
        ld = len(spaths[l])
        if ld < bestd:
            bestd = ld
            best = l

    return best



#example usage
if __name__ == '__main__':
    print 'DISTANCES:'
    print 'Spanish and Portuguese:', distance('spa','por')
    print 'Spanish and Javanese:', distance('spa','jav')
    print
    print 'NEAREST NEIGHBORS:'
    print 'Spanish:', nearest('spa')
    print 'Javanese:',nearest('jav')











