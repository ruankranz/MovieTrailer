import fresh_tomatoes
import media

#create a list to store the movies
movies =[]

#Start creating movies using the Movie class from the media module
#Movie Structure
        #Title
        #Storyline
        #Director
        #Actors
        #Poster Image
        #Youtube trailer URL
the_beach = media.Movie("The Beach",
                        "Twenty-something Richard travels to Thailand and finds himself in possession of a strange map. Rumours state that it leads to a solitary beach paradise, a tropical bliss - excited and intrigued, he sets out to find it.",
                        "Danny Boyle",
                        "Leonardo DiCaprio, Daniel York, Patcharawan Patarakijjanon",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/The_Beach_film.jpg/215px-The_Beach_film.jpg",
                        "https://www.youtube.com/watch?v=lBJ9MAectV0")
movies.append(the_beach)
apocalypse_now = media.Movie("Apocalypse Now",
                        "During the Vietnam War, Captain Willard is sent on a dangerous mission into Cambodia to assassinate a renegade colonel who has set himself up as a god among a local tribe.",
                        "Francis Ford Coppola",
                        "Martin Sheen, Marlon Brando, Robert Duvall",
                        "http://ia.media-imdb.com/images/M/MV5BMTcyMzQ5NDM4OV5BMl5BanBnXkFtZTcwODUwNDg3OA@@._V1_UY268_CR9,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=IkrhkUeDCdQ")
movies.append(apocalypse_now)
the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         "The Wachowski Brothers",
                         "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
                         "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=fY9UhIxitYM")
movies.append(the_matrix)
the_wolf_of_wall_street = media.Movie("The Wolf of Wall Street",
                                     "Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.",
                                     "Martin Scorsese",
                                     "Leonardo DiCaprio, Jonah Hill, Margot Robbie",
                                     "http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                     "https://www.youtube.com/watch?v=BzpIB5TJ7LI")
movies.append(the_wolf_of_wall_street)
django_unchained = media.Movie("Django Unchained",
                               "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.",
                               "Quentin Tarantino",
                               "Jamie Foxx, Christoph Waltz, Leonardo DiCaprio",
                               "http://ia.media-imdb.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow")
movies.append(django_unchained)
the_interview = media.Movie("The Interview",
                            "Dave Skylark and producer Aaron Rapoport run the celebrity tabloid show Skylark Tonight. When they land an interview with a surprise fan, North Korean dictator Kim Jong-un, they are recruited by the CIA to turn their trip to Pyongyang into an assassination mission.",
                            "Evan Goldberg, Seth Rogen",
                            "James Franco, Seth Rogen, Randall Park",
                            "http://ia.media-imdb.com/images/M/MV5BMTQzMTcwMzgyMV5BMl5BanBnXkFtZTgwMzAyMzQ2MzE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=DkJA1rb8Nxo")
movies.append(the_interview)
#End creating movies

#Call function from fresh_tomatoes module to generate html page with list of movies as parameter
fresh_tomatoes.open_movies_page(movies)
