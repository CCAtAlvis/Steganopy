from PIL import Image
import numpy as np

from huffman import huffman
from huffman import huff_decode

def image_load(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int32")
    return data

def image_save(npdata, outfilename) :
    img = Image.fromarray(np.asarray(np.clip(npdata,0,255), dtype="uint8"), "RGB")
    img.save(outfilename)

def make_binary(img_a):
    img_bin = []
    for i in range(len(img_a)):
        img_bin.append([])
        for j in range(len(img_a[i])):
            t = [np.binary_repr(k, width=8) for k in img_a[i][j]]
            img_bin[i].append(t)
    return img_bin

def image_create(img):
    img_new = []
    for i in range(len(img)):
        img_new.append([])
        for j in range(len(img[i])):
            t = [int(k, 2) for k in img[i][j]]
            img_new[i].append(t)
    return img_new

def encode(img, data):
    img_new = []
    # data_c = 0
    k = 0

    for i in range(len(img)):
        img_new.append([])
        for j in range(len(img[i])):
            t = img[i][j]
            if k < len(data):
                # print(t)
                # print(data[data_c], int(data[data_c], 2), chr(int(data[data_c], 2)))
                t[0] = t[0][:-3] + data[k+0:k+3]
                t[1] = t[1][:-3] + data[k+3:k+6]
                t[2] = t[2][:-3] + data[k+6:k+9]
                # print(data[data_c][0:3], data[data_c][3:6], data[data_c][6:8])
                # print(t)
                # print('-'*50)
                # data_c += 1
                k += 9
            elif k == len(data):
                t[0] = t[0][0:-4] + '1111'
                t[1] = t[1][0:-4] + '1111'
                t[2] = t[2][0:-4] + '1111'
                k += 1

            img_new[i].append(t)
    return img_new

def decode(img):
    data = ''
    for i in range(len(img)):
        for j in range(len(img[i])):
            t = img[i][j]
            t = [np.binary_repr(k, width=8) for k in img[i][j]]
            last = t[0][-4:] + t[1][-4:] + t[2][-4:]
            if last == '111111111111':
                return data
            d = t[0][-3:] + t[1][-3:] + t[2][-3:]
            data += d
            # e = int(d, 2)
            # f = chr(e)
            # data += f
            # print(t)
            # print(t[0][-3:], t[1][-3:], t[2][-2:])
            # print(d, e, f)
            # print('*'*50)
    return data


original = image_load('./images/interpreter-symbol-small.jpg')
img_bin = make_binary(original)

data = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type
and scrambled it to make a type specimen book. It has survived not only five centuries, but also the
leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s
with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop
publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
# data = "lets make some dummy data"

# data_binary = [np.binary_repr(ord(i), width=8) for i in data]
data_binary, char_binary = huffman(data)
padding = 9 - (len(data_binary) % 9)
for i in range(padding):
    data_binary += '0'
# print(len(data_binary))

# img_encoded = image_create(encode(img_bin, data_binary))
img_encoded = encode(img_bin, data_binary)
img_crt = image_create(img_encoded)
# saving image as png image is recommended option as its lossless
# saving as jpeg is lossy thus saving and reading from jepg file may result
# in incorrect decoding and excess loop execution
image_save(img_crt, './images/output.png')
img_ip = image_load('./images/output.png')

# i=0
# j=0

# print(original[i][j])
# print([np.binary_repr(i, width=8) for i in original[i][j]])
# print(img_encoded[i][j])
# print(np.asarray(img_crt[i][j]))
# print(img_ip[i][j])

# data_decoded = decode(image_load('./images/output-new.jpg'))
data_decoded = decode(img_ip)
data_decoded = data_decoded[:-padding]
uncompressed_data = huff_decode(data_decoded, char_binary)
print("Decoded data:", uncompressed_data)
print("\nDecoded data size: {} Kb".format((len(uncompressed_data) * 8) / 1000))