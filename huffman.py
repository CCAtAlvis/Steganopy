import heapq
from collections import defaultdict

def encode(freq):
    heap = [[weight, [symbol, '']] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

data = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
frequency = defaultdict(int)

for symbol in data:
    frequency[symbol] += 1

huff = encode(frequency)
enc_data = []

for symbol in data:
    for i in range(len(huff)):
        if huff[i][0] == symbol:
            enc_data.append(huff[i][1])
print(enc_data)