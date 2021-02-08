## Project 1

### Install Requirments:
1. Install Dijkstra from pypi `pip install dijkstra`
2. Install A* from pypi `pip install astar`

### Run program
1. To run the uninformed search: `python uninformed_search.py`
2. Enter two numbers in the terminal ranging from 0 - 99
3. To run the informed search: `python informed_search.py`
4. Enter two numbers in the terminal ranging from 0 - 99

### Analysis on performace:
- We can see that the performance between the two algorithms are very similar, close to negible. Both are extremely fast for the graph we are using. For example, if we use the start as `9` and end as `34` the shortest path is [9, 20, 22, 27, 34]. For the uninformed search it takes on avg 0.0006 seconds, the informed search takes on avg 0.0025 seconds. We can see the informed search is slower which is not what we would expect. This could be cause of the library used, one may be more optimized than the other. It can also be due to the graph we are using. the layers are not that deep compared to graphs that can be thousands or millions of nodes. Since we are only dealing with 100 nodes, the uninformed search may be faster in small graphs. The informed search could still be more effective for large datasets but we are only using 100 nodes, therefore the uninformed search is marginally faster.