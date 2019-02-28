from typing import Set, Tuple, List

# Takes in input in the form of a list of tuples representing
# a photo, where the first element is the orientation
# and the second element is a set of tags


def make_slides(photos: List[Tuple[str, Set[str]]]):
    cnt = 0
    verticaldict = dict()
    resultdict = dict()
    seendict = dict()

    for photo in photos:
        if photo[0] == "H":
            print("h")
            resultdict[(cnt,)] = photo[1]
        elif photo[0] == "V":
            print("v")
            verticaldict[cnt] = (cnt, photo[1])

        cnt += 1

    for key, verticalphoto in verticaldict.items():
        if key in seendict:
            continue

        bestmatch = ()
        bestdiff = 0

        for potentialkey, potentialmatch in verticaldict.items():
            if potentialkey in seendict:
                continue

            if bestmatch is ():
                bestmatch = potentialmatch
                bestdiff = len(bestmatch[1].difference(verticalphoto[1]))
            else:
                temp = len(potentialmatch[1].difference(verticalphoto[1]))

                if temp > bestdiff:
                    bestmatch = potentialmatch
                    bestdiff = temp

        if bestmatch is not ():
            seendict[bestmatch[0]] = True
            seendict[verticalphoto[0]] = True
            resultdict[(bestmatch[0], verticalphoto[0])] = bestmatch[1].union(verticalphoto[1])

    return resultdict


# basic test
# print(make_slides([("V", {"a", "b", "c"}), ("H", {"b", "c", "d"}), ("V", {"a", "b", "c"}), ("V", {"e", "d"}), ("V", {"f", "g"})]))
