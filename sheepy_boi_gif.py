import imageio.v3 as shep

filenames = ['sheep_00.png', 'sheep_01.png', 'sheep_02.png', 'sheep_03.png', 'sheep_04.png', 'sheep_05.png', 'sheep_06.png', 'sheep_07.png', 'sheep_08.png', 'sheep_09.png', 'sheep_10.png', 'sheep_11.png']
images = []

for filename in filenames:
    images.append(shep.imread(filename))

shep.imwrite('sheep_gif2.gif', images, duration = 100, loop = 0)
