input_file = open("day5_input.txt", "r")

lines = input_file.readlines()

ordering_rules = []

line_num = 0
while lines[line_num] != "\n":
    rule = lines[line_num][:-1].split("|")
    ordering_rules.append((rule[0], rule[1]))
    line_num += 1
line_num += 1

def in_order(page_index):
    for page1, page2 in ordering_rules:
        if page_index.get(page1, -1) > page_index.get(page2, 100):
            return False
    return True

sum_middles = 0

while line_num < len(lines):
    update = lines[line_num][:-1].split(",")
    page_index = {}
    for i, page in enumerate(update):
        page_index[page] = i
    if in_order(page_index):
        sum_middles += int(update[len(update) // 2])
    line_num += 1

print("Part 1 answer:", sum_middles)

# PART 2

# Idea #0: Write a sort comparator using ordering rules directly
# Abandoned as it won't work if not all relations are given directly (ex: given 1 < 2 and 2 < 3 *implies* that 1 < 3)

'''
# Idea #1: Remembered/rediscovered "proper" way from competitive programming days.
# We can represent the ordering rules as a directed acyclic graph (acyclic meaning cycles like 1 -> 2 and 2 -> 1 are not allowed).
# Edit: wrong assumption ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Now look at the in-degree of each node (# of incoming edges).
# Node(s) with 0 indegree must, by definition, come first since no nodes point *to* them.
# -- Side note: if there are multiple, their relative order is ambiguous (ex: for A -> C and B -> C, ABC and BAC are both valid)

# Process these node(s) one by one, removing them from the graph (and their outgoing edges)
# You now have a smaller version of the same exact problem, as you created more nodes with 0 indegree.
# Simply reapply the same idea until you have processed all nodes.

graph = {}
in_degree = {}

line_num = 0
while lines[line_num] != "\n":
    rule = lines[line_num][:-1].split("|")
    if rule[0] not in graph:
        graph[rule[0]] = []
    if rule[1] not in graph:
        graph[rule[1]] = []
    graph[rule[0]].append(rule[1])
    in_degree[rule[0]] = in_degree.get(rule[0], 0)
    in_degree[rule[1]] = in_degree.get(rule[1], 0) + 1
    line_num += 1
line_num += 1

queue = []
print(graph)

def add_0_indeg_nodes():
    for node, indeg in in_degree.items():
        if indeg == 0:
            queue.append(node)

def remove_node(fromNode):
    for toNode in graph[fromNode]:
        in_degree[toNode] -= 1
    del graph[fromNode]
    del in_degree[fromNode]

add_0_indeg_nodes()

final_ordering = []

while queue:
    current = queue.pop(0)
    final_ordering.append(current)
    remove_node(current)
    add_0_indeg_nodes()

print(final_ordering)
'''

# Idea #2: For each list, go through the ordering rules until you find an inconsistency and swap the two numbers.
# Repeat until the entire list converges on correctness. Convergence is hard to prove though...

ordering_rules = []

line_num = 0
while lines[line_num] != "\n":
    rule = lines[line_num][:-1].split("|")
    ordering_rules.append((rule[0], rule[1]))
    line_num += 1
line_num += 1

def in_order(page_index):
    for page1, page2 in ordering_rules:
        if page_index.get(page1, -1) > page_index.get(page2, 100):
            page_index[page1], page_index[page2] = page_index[page2], page_index[page1]
            return False
    return True

sum_fixed_middles = 0

while line_num < len(lines):
    update = lines[line_num][:-1].split(",")
    page_index = {}
    for i, page in enumerate(update):
        page_index[page] = i
    if in_order(page_index):
        line_num += 1
        continue
    while not in_order(page_index):
        pass

    for page, index in page_index.items():
        if index == len(update) // 2:
            sum_fixed_middles += int(page)

    line_num += 1

print("Part 2 answer:", sum_fixed_middles)
