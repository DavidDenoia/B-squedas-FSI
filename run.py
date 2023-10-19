# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
oe = search.GPSProblem('O', 'E', search.romania)
gz = search.GPSProblem('G', 'Z', search.romania)
nd = search.GPSProblem('N', 'D', search.romania)
mf = search.GPSProblem('M', 'F', search.romania)

print("Arad - Bucharest\n")
print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bound_graph_search(ab).path())
print(search.branch_and_bound_subest_graph_search(ab).path())

print("Oradea - Efoire\n")
print(search.breadth_first_graph_search(oe).path())
print(search.depth_first_graph_search(oe).path())
print(search.branch_and_bound_graph_search(oe).path())
print(search.branch_and_bound_subest_graph_search(oe).path())

print("Giurgiu - Zerind\n")
print(search.breadth_first_graph_search(gz).path())
print(search.depth_first_graph_search(gz).path())
print(search.branch_and_bound_graph_search(gz).path())
print(search.branch_and_bound_subest_graph_search(gz).path())

print("Neamt - Dobreta\n")
print(search.breadth_first_graph_search(nd).path())
print(search.depth_first_graph_search(nd).path())
print(search.branch_and_bound_graph_search(nd).path())
print(search.branch_and_bound_subest_graph_search(nd).path())

print("Mehadia - Fagaras\n")
print(search.breadth_first_graph_search(mf).path())
print(search.depth_first_graph_search(mf).path())
print(search.branch_and_bound_graph_search(mf).path())
print(search.branch_and_bound_subest_graph_search(mf).path())


