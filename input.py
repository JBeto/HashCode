def getInput():
	numPhotos = int(input())
	pics = []

	for n in range(numPhotos):
		el = input().split(' ')
		pics.append((el[0], set(el[2:])))
	return pics


if __name__ == '__main__':
	getInput()