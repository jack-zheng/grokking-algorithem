def get_width(length, width):
    if length % width == 0:
        return width
    return get_width(width, length%width)

if __name__ == '__main__':
    print('168*64, max width = %s' % get_width(168, 64))