def score_submission(slides):
    score = 0
    for i in range(len(slides) - 1):
        slide_0 = slides[i][1]
        slide_1 = slides[i+1][1]
        score += min(len(slide_0 & slide_1), len(slide_1 - slide_0), len(slide_0 - slide_1))
    print(score)


if __name__ == '__main__':
    score_submission([
        (1, {'cat', 'dog', 'garden'}),
        (1, {'tower', 'moon', 'garden'}),
        (1, {'tower', 'wow', 'garden'})
    ])
