from csv import DictReader
from urllib.request import urlretrieve
from collections import defaultdict,namedtuple,Counter

def get_top_movie_directors(url,top):

	file, response = urlretrieve(url,'./movie_metadata.csv')

	with open(file,mode='r',encoding='utf-8') as f:

		movies_hub = DictReader(f)
		movie = namedtuple('Movie',['movie_title','title_year','imdb_score'])
		best_filterd_movies = defaultdict(list)

		for mo in movies_hub:

			dir_name = mo['director_name']

			try:
				year = int(mo['title_year'])
			except ValueError:
				year = 0

			if dir_name != '' and year > 1960:

				best_filterd_movies[dir_name].append(
					movie(
						movie_title= mo['movie_title'].replace('\xa0',''),
						title_year = mo['title_year'],
						imdb_score = mo['imdb_score'],
					) 
				)
			best_filterd_movies[dir_name].sort(key=lambda x: x.imdb_score,reverse=True)	

		famous = sorted(best_filterd_movies.items(),key=lambda x : len(x[1]),reverse=True)

		if len(famous) > top:
			return dict(famous[:top])

		return dict(famous)	



if __name__ == '__main__':

	url = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'

	form = '[{year}] {title} {space} {score}'

	for name,movies in get_top_movie_directors(url,20).items():
		print('\n')		
		print(name)
		print('--' * 40)
		for movie in movies:
			space = ' ' * (abs(len(movie.movie_title) - 60))
			print(form.format(title=movie.movie_title,year=movie.title_year,score=movie.imdb_score,space=space))
		print('**' * 40)	

