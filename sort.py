import re
import praw
from operator import itemgetter

def set_sorting_values(submissions):
    """Set's sorting values and discard non-challenge posts"""
    result = []
    difficulty = {'easy' : 1, 'intermediate': 2,
                  'hard': 3, 'difficult': 3}
    for sub in submissions:
        for key, value in difficulty.iteritems():
            if key in sub.title.lower():
                sub.difficulty = value
                break
        else:
            continue
        sub.number = int(re.findall('#(\d+)', sub.title)[0])
        result.append(sub)
    return result

r = praw.Reddit('Intermediate 117 challange on r/dailyprogrammer by u/_daimon_'
                ' ver 0.1')
subreddit = r.get_subreddit('dailyprogrammer')
posts = set_sorting_values(subreddit.get_hot(limit=None))
list1 = sorted(posts, key=lambda post: (post.number, post.difficulty))
for sub in list1:
    print "<a href=\"%s\">%s</a>" % (sub.short_link.encode('utf-8'), sub.title.encode('utf-8'))
    print sub.selftext.encode('utf-8')
    print "\n"
