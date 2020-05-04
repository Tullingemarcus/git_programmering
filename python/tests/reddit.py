import praw

reddit = praw.Reddit(client_id='3BqRqrMOaAKI9g',
                     client_secret='qClRMeV9jFOaOUv7AKOLaolpLGE', password='D1sc0rd02',
                     user_agent='discordreddit', username='discordbotonreddit')
x = 0
for submission in reddit.subreddit('FreeGameFindings').top('all', limit=int(5 + x)):
    if submission.link_flair_css_class == 'Expired':
        pass
    else:
        print(submission.title)