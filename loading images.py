import matplotlib.image as mpimg

def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = mpimg.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images
image=load_images("D:\course\PETA dataset\CAVIAR4REID\archive")
print(image)
