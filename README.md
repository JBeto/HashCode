# Google Hash Code 2019

#### Team: Jerry Jiang, Edward Zabrensky, William Shiao, Joshua Beto

## Abridged Problem Statement
* You can view the full problem statement [here](https://github.com/JBeto/HashCode/blob/master/photo_slideshow.pdf). (I recommend it!)

"Given a list of photos and tags associated with each photo, arrange the photos into a slideshow that is as interesting as possible."

Interest factor is defined as the minimum between adjacent slides' shared tags and exclusive tags. Your goal is to maximize the total interest factor in the entire slideshow.

## Our Approach

We went with a basic greedy approach to both construct the slides and pair each slide with each other. In our approach, we **build the slideshow greedily from left -> right, one slide at a time.**

Our approach is broken into 3 steps:
1. Construct each slide from the list of photos.
    * A horizontal photo is a slide of itself.
    * Vertical photos are matched greedily. Randomly pick a vertical photo, then match it with the next photo that maximizes the **number of tags** in the slide.
2. Randomly select a slide to be the first slide.
3. Greedily select the next slide such that the interest factor is maximized from the *last slide picked*. 

## Analysis

Surprisingly, our very naive greedy approach was effective. From our results post-contest, we were able to score 800,000+ points.

Our reasoning for constructing the slides greedily in Step 1) was that the more tags a slide had, the bigger the interest factor would be when matching slides later. This is because the interest factor is defined as the *minimum* between the intersection, S1 exclusive, and S2 exclusive. Thus, the more tags there were, the higher chance that there would be a higher interest factor since that would *maximize* the *minimum*.

## Problems Encountered

One main issue we encountered was that our implementation was extrememly slow. We were adding and removing to/from lists respectively, causing a bottleneck in performance when it came down to the larger data sets. 

Because of this, we weren't able to submit our greedy solution for the big data set during the contest in time, and instead substituted Step 3 last minute for a random based approach (Yes, literally randomly pairing two slides together).

## Improvement

One obvious room for improvement is the implementation. Had we thought our data structures more thouroughly during the contest or were faster coding, we could have siginificantly increased performance.

Another point of improvement was our greedy approach. Later in the competition, we realized a tree-based approach where instead of building the slideshow one slide at a time from left -> right, we could pair two slides together and set them aside as a **single slide**, not necessarily attaching it to the final slideshow just yet. 

The key realization of this tree-based approach is that each slide can be considered as two components, the **left** and the **right** side. When you pair two slides together, the left side of the left slide is the **left**, and the right side of the right slide is the **right** (I'll let that sink in for a bit).

When you consider a single slide by itself, the **left** and **right** side are just mirrors of each other. They hold the same set of tags, which is just the set of tags of the actual slide.

You can then do something similar to a [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) where each slide is considered a node, and you continuously pair the best 2 nodes that give the highest interest rating with each other until you end up with a tree structure. 