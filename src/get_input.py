def get_input():
    num_photos = int(input())
    pics = []
    for n in range(num_photos):
        el = input().split(' ')
        pics.append((el[0], set(el[2:])))
    return pics


if __name__ == '__main__':
    get_input()
