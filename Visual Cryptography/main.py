from visual_cryptography import *
import matplotlib.pyplot as plt


def plot(img, title):
    plt.imshow(img)
    plt.title(title)
    plt.show()


def main():
    vc = VisualCryptography([255, 255, 255], [0, 0, 0])

    original = VisualCryptography.read_image('xyz.jpg')
    part1, part2 = vc.split_image(original)
    combined = vc.combine_images(part1, part2)
    rescaled = vc.rescale_to_original(combined)

    plot(original, 'Original')
    plot(part1, 'Part 1')
    plot(part2, 'Part 2')
    plot(combined, 'Combined')
    plot(rescaled, 'Rescaled')


if __name__ == '__main__':
    main()
