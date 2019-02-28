import randchain
import scorer
import slide_maker
import get_input
import pickle
from os import path
import sys

def main():
    # print('=== Getting Input ===')
    data = get_input.get_input()

    # print('=== Making Slides ===')
    file_name = 'slides_{}.pickle'.format('default' if len(sys.argv) <= 1 else sys.argv[1])
    if not path.exists(file_name):
        slides = slide_maker.make_slides(data)
        with open(file_name, 'wb') as f:
            pickle.dump(slides, f)
    else:
        with open(file_name, 'rb') as f:
            slides = pickle.load(f)
    
    # print('=== Making Reverse Index ===')
    rev_idx = randchain.make_rev_index(slides)
    # print('=== Making Chain ===')
    slides = randchain.make_chain(slides, rev_idx)
    # print('=== Scoring ===')
    # scorer.score_submission(slides)
    scorer.print_solution(slides)


if __name__ == '__main__':
    main()

