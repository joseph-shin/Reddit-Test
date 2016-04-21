import praw
import requests

# random word generator
# http://stackoverflow.com/questions/18834636/random-word-generator-python

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()

# connect to reddit and identify script

user_agent = "reddit test 0.1 by /u/JshinPython"
r = praw.Reddit(user_agent=user_agent)
r.login()	# prompts user for input if no args passed

# make a text submission to dummy subreddit
# random title with three words and random body with five words

from random import randint
sub = r.get_subreddit("JShinPython")
rand_title = ""
rand_body = ""
for x in range(0, 3):
	rand_title = rand_title + ( WORDS[randint(0,24000)] + " " )
for x in range(0, 6):
	rand_body = rand_body + ( WORDS[randint(0,24000)] + " " )
print(rand_title + rand_body)
r.submit(sub, rand_title, rand_body )

# check to see user's past 10 posts
username = "JshinPython"
user = r.get_redditor(username)
post_limit = 10
gen = user.get_submitted(limit=post_limit)
