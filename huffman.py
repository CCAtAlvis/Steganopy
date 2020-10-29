data = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
size = len(data) * 8
print("Initial data size: {} bits\n".format(size))

frequency = []
characters = []
for symbol in data:
    if symbol not in frequency:
        frequency.append(data.count(symbol))
        frequency.append(symbol)
        characters.append(symbol)

nodes = []
while len(frequency) > 0:
    nodes.append(frequency[0:2])
    frequency = frequency[2:]

nodes.sort()
huff = []
huff.append(nodes)

def huffman_tree(nodes):
    pos = 0
    newnode = []
    if len(nodes) > 1:
        nodes.sort()
        nodes[pos].append("0")
        nodes[pos+1].append("1")
        combined_node1 = nodes[pos][0] + nodes[pos+1][0]
        combined_node2 = nodes[pos][1] + nodes[pos+1][1]
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes = []
        newnodes.append(newnode)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        huff.append(nodes)
        huffman_tree(nodes)
    return huff

newnodes = huffman_tree(nodes)

huff.sort(reverse=True)

checklist = []
for level in huff:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)

count = 0
for level in huff:
    print("Level", count, ":", level)
    count += 1