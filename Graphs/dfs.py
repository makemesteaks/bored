# DICTIONARY WITH ALL THE DOTS AND CONNECTIONS

d = {'A' : ['D','B','F'],
     'B' : ['A'],
     'F' : ['D', 'A'],
     'D' : ['B'] }
     
def dfs(graph, start, path=[]):

# THE INITIAL VARIABLE IS THE ELEMENT INSIDE THE LIST TO BE TESTED
    initial = [start]

	# LOOP UNTIL WE RUN OUT OF INITIAL POSSIBILITES
    while initial:

	# THIS IS THE VARIABLE WILL BE CHECKED AGAINST THE PATH
        check = initial.pop()
        if check not in path:

	# IF IT DOESN'T EXIST, ADD TO THE PATH
            path.append(check)

	# INITIAL JUMPS TO THE NEXT CHARACTER TO BE TESTED AND RESPECTIVE NODES
            initial = graph[check]

	# RETURNS FINAL PATH
    return path
    
dfs(d, 'B')
