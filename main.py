import imageio

image1 = input("Enter the first image: ")
image2 = input("Enter the second image: ")

filenames = [image1, image2]
images = []

for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('team.gif', images, duration=0.5, loop=0)

