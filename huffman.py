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
print()

def encode(characters, checklist, data):
    char_bin = []
    if len(characters) == 1:
        char_code = [characters[0], "0"]
        char_bin.append(char_code * len(data))
    else:
        for char in characters:
            charcode = ""
            for node in checklist:
                if len(node) > 2 and char in node[1]:
                    charcode += node[2]
            char_code = [char, charcode]
            char_bin.append(char_code)

    bitstring = ""
    for char in data:
        for item in char_bin:
            if char in item:
                bitstring += item[1]
    return bitstring, char_bin

encoded_data, character_binary = encode(characters, checklist, data)

for item in character_binary:
    print(item[0], item[1])

print("\nEncoded Data: {}\n".format(encoded_data))
print("Compressed data size: {} bits\n".format(len(encoded_data)))

def decode(enc_data, character_binary):
    uncompressed_data = ""
    code = ""
    for bit in enc_data:
        code += bit
        pos = 0
        for item in character_binary:
            if code == item[1]:
                uncompressed_data += character_binary[pos][0]
                code = ""
            pos += 1
    return uncompressed_data

decoded_data = decode(encoded_data, character_binary)

print("Original data:", decoded_data)
print("Original data size: {} bits".format(len(decoded_data) * 8))