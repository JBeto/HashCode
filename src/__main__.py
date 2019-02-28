import chain
import scorer
import slide_maker
import get_input


def main():
    data = get_input.get_input()
    slides = slide_maker.make_slides(data)
    rev_idx = chain.make_rev_index(slides)
    slides = chain.make_chain(slides, rev_idx)
    #scorer.score_submission(slides)
    scorer.print_solution(slides)


if __name__ == '__main__':
    main()

