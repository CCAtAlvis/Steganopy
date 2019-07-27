from PIL import Image
import numpy as np

def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int32")
    return data

def save_image(npdata, outfilename) :
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

def create_image(img):
    img_new = []
    for i in range(len(img)):
        img_new.append([])
        for j in range(len(img[i])):
            t = [int(k, 2) for k in img[i][j]]
            img_new[i].append(t)
    return img_new

def encode(img, data):
    img_new = []
    data_c = 0

    for i in range(len(img)):
        img_new.append([])
        for j in range(len(img[i])):
            t = img[i][j]
            # print(t)
            if data_c < len(data):
                print(data[data_c], int(data[data_c], 2), chr(int(data[data_c], 2)))
                t[0] = t[0][0:-3] + data[data_c][0:3]
                t[1] = t[1][0:-3] + data[data_c][3:6]
                t[2] = t[2][0:-2] + data[data_c][6:8]
                data_c += 1
                # print(t)
            elif data_c == len(data):
                t[0] = t[0][0:-3] + '111'
                t[1] = t[1][0:-3] + '111'
                t[2] = t[2][0:-2] + '11'

            img_new[i].append(t)
    return img_new

def decode(img):
    data = ''
    for i in range(len(img)):
        for j in range(len(img[i])):
            t = [np.binary_repr(k, width=8) for k in img[i][j]]
            d = t[0][-3:] + t[1][-3:] + t[2][-2:]
            e = int(d, 2)
            f = chr(e)
            data += f
            print(d, e, f)
    return data


original = load_image("./images/interpreter-symbol-small.jpg")
i = make_binary(original)

# data = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
data = "lets make some dummy data"
data_binary = [np.binary_repr(ord(i), width=8) for i in data]

img_encoded = create_image(encode(i, data_binary))

save_image(img_encoded, 'new.jpg')

data_decoded = decode(load_image("new.jpg"))
print(data_decoded)
