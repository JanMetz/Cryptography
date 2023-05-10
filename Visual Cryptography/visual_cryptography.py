import matplotlib.image as mpimg
import numpy as np
import random


class VisualCryptography:
    colour1 = None
    colour2 = None

    def __init__(self, colour1, colour2):
        self.colour1 = np.array(colour1)
        self.colour2 = np.array(colour2)

    @staticmethod
    def read_image(filename):
        img = mpimg.imread(filename)
        return np.array(img)

    def is_colour2_pixel(self, rgb):
        middle = (self.colour1 + self.colour2) // 2
        return np.all(rgb < middle)

    def paint_together(self, row1, row2):
        if VisualCryptography.draw():
            row1.extend((self.colour2, self.colour1))
            row2.extend((self.colour2, self.colour1))
        else:
            row1.extend((self.colour1, self.colour2))
            row2.extend((self.colour1, self.colour2))

    def paint_reverse(self, row1, row2):
        if VisualCryptography.draw():
            row1.extend((self.colour2, self.colour1))
            row2.extend((self.colour1, self.colour2))
        else:
            row1.extend((self.colour1, self.colour2))
            row2.extend((self.colour2, self.colour1))

    @staticmethod
    def draw():
        return random.randint(0, 1)

    def split_image(self, img):
        part1 = []
        part2 = []

        for row in img:
            row1 = []
            row2 = []
            for pix in row:
                if self.is_colour2_pixel(pix):
                    self.paint_together(row1, row2)
                else:
                    self.paint_reverse(row1, row2)

            part1.append(row1)
            part2.append(row2)

        return np.array(part1), np.array(part2)

    def combine_images(self, i1, i2):
        img = []
        for i in range(len(i1)):
            row = []
            for j in range(len(i1[0])):
                if self.is_colour2_pixel(i1[i][j]) or self.is_colour2_pixel(i2[i][j]):
                    row.append(self.colour2)
                else:
                    row.append(self.colour1)

            img.append(row)

        return np.array(img)

    def rescale_and_deinterfere(self, img):
        rescaled = []
        for i in range(len(img)):
            row = []
            for j in range(0, len(img[0]), 2):
                if self.is_colour2_pixel((img[i][j] + img[i][j + 1]) // 2):
                    row.append(self.colour1)
                else:
                    row.append(self.colour2)

            rescaled.append(row)

        return np.array(rescaled)
