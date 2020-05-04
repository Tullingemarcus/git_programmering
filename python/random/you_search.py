from youtube_search import YoutubeSearch

results = YoutubeSearch('search terms', max_results=10).to_json()

print(results)