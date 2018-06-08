'''
OPTIONAL WEB SCRAPING HOMEWORK

First, define a function that accepts an IMDb ID and returns a dictionary of
movie information: title, star_rating, description, content_rating, duration.
The function should gather this information by scraping the IMDb website, not
by calling the OMDb API. (This is really just a wrapper of the web scraping
code we wrote above.)

For example, get_movie_info('tt0111161') should return:

{'content_rating': 'R',
 'description': u'Two imprisoned men bond over a number of years...',
 'duration': 142,
 'star_rating': 9.3,
 'title': u'The Shawshank Redemption'}

Then, open the file imdb_ids.txt using Python, and write a for loop that builds
a list in which each element is a dictionary of movie information.

Finally, convert that list into a DataFrame.
'''
import requests
import pandas
from bs4 import BeautifulSoup

# define a function that accepts an IMDb ID and returns a dictionary of movie information
columns = ['content_rating', 'description', 'duration', 'star_rating', 'title']
def get_movie_info (movie_id):
    info = []
    url = 'https://www.imdb.com/title/{}/'.format(movie_id)
    response = requests.post(url)
    b = BeautifulSoup(response.text)
    info.append(b.find(name='meta', attrs={'itemprop':'contentRating'})['content'])
    info.append(b.find(name='div', attrs={'class':'summary_text'}).text.replace('\n','')[20:-12])
    info.append(int(b.find_all(name='time')[1].text[:-4]))
    info.append(float(b.find(name='span', attrs={'itemprop':'ratingValue'}).text))
    info.append(b.find(name='h1', attrs={'itemprop':'name'}).text[:-8])
    return dict(zip(columns, info))

# test the function
get_movie_info ('tt0317705')

# open the file of IDs (one ID per row), and store the IDs in a list
f = open('imdb_ids.txt', 'r')
id_str = f.read()
id_list = id_str.split('\n')[:-1]

# get the information for each movie, and store the results in a list
movie_list = []
for i in id_list:
    movie_list.append(get_movie_info(i))

# check that the list of IDs and list of movies are the same length
len(id_list)
len(movie_list)

# convert the list of movies into a DataFrame
data = pandas.DataFrame(movie_list)

'''
Another IMDb example: Getting the genres
'''

# read the Shawshank Redemption page again
url = 'https://www.imdb.com/title/tt0111161/'
response = requests.post(url)
b = BeautifulSoup(response.text)

# only gets the first genre
b.find(name='span', attrs={'class':'itemprop', 'itemprop':'genre'}).text

# gets all of the genres
genres = b.find_all(name='span', attrs={'class':'itemprop', 'itemprop':'genre'})
for genre in genres:
    print(genre.text)

# stores the genres in a list
genre_list = []
genres = b.find_all(name='span', attrs={'class':'itemprop', 'itemprop':'genre'})
for genre in genres:
    genre_list.append(genre.text)

'''
Another IMDb example: Getting the writers
'''

# attempt to get the list of writers (too many results)
b.find_all(name='span', attrs={'class':'itemprop', 'itemprop':'name'})

# limit search to a smaller section to only get the writers
writers = b.find_all(name='div', attrs={'class':'credit_summary_item'})[1].find_all(name='span', attrs={'class':'itemprop', 'itemprop':'name'})
for writer in writers:
    print(writer.text)
'''
Another IMDb example: Getting the URLs of cast images
'''

# find the images by size
cast = b.find_all(name='img', attrs={'height':'44', 'width':'32'})

# check that the number of results matches the number of cast images on the page
len(b.find_all(name='img', attrs={'height':'44', 'width':'32'}))

# iterate over the results to get all URLs
actor_img = []
for actor in cast:
    actor_img.append(actor['src'])

'''
Useful to know: Alternative Beautiful Soup syntax
'''

