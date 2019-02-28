from typing import Dict, Tuple, Set
from random import randrange

def make_rev_index (slides: Dict[Tuple[int, int], Set[int]]):
    index = {}
    for p in slides.items():
        for t in p[1]:
            if t in index:
                index[t].add(p[0])
            else:
                index[t] = set([p[0]])
    return index


def make_chain (slides, index):
    last = next(iter(slides))
    # print('Starting with {}'.format(last))
    chain = []

    chain.append((last, slides[last]))
    to_del = last
    last = slides[last]
    del slides[to_del]

    while len(slides) > 0:
        # print('Iteration, with sz left: {}'.format(len(slides)))
        candidates = set()

        for term in last:
            candidates |= index[term]
            # for candidate in index[term]:
                # print('candidate: {}'.format(candidate))
                # candidates.add(candidate)

        best = None
        bestDiff = 0
        for cand in candidates:
            if best is not None:
                break
            if cand not in slides:
                continue
            # might be able to be optimized
            inter = len(slides[cand] & last)
            ratio = inter / len(slides[cand])
            diff = abs(ratio - 0.5)
            if best is None or diff < bestDiff:
                best = cand
                bestDiff = diff
        
        if best == None:
            r = next(iter(slides))
            # print('R: ', r)
            best = slides[r]
            # print('b', best)
            chain.append((r, slides[r]))
            del slides[r]
            # print('RIPPPPPP')
        else:
            chain.append((best, slides[best]))
            last = slides[best]
            del slides[best]

    return chain

if __name__ == '__main__':
    sample = {
        (0,): {'cat', 'beach', 'sun'},
        (1, 2): {'selfie', 'smile', 'garden'},
        (3,): {'garden', 'cat'},
        (4,): {},
    }

    print(sample)
    idx = make_rev_index(sample)
    print('Index: {}'.format(idx))

    chain = make_chain (sample, idx)
    print('Chain: {}'.format(chain))
