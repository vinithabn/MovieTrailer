import media

import fresh_tomatoes

usual_suspects = media.Movie("The Usual Suspects",
                             "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which begin when five criminals meet at a seemingly random police lineup.",
                             "http://ia.media-imdb.com/images/M/MV5BMzI1MjI5MDQyOV5BMl5BanBnXkFtZTcwNzE4Mjg3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=oiXdPolca5w")
                                
finding_nemo = media.Movie("Finding Nemo",
                           "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.",
                           "http://ia.media-imdb.com/images/M/MV5BMTY1MTg1NDAxOV5BMl5BanBnXkFtZTcwMjg1MDI5Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

jurassic_park = media.Movie("Jurassic Park",
                            "During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok. ",
                            "http://ia.media-imdb.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=lc0UehYemQA")

good_bad_ugly = media.Movie("The Good, the Bad and the Ugly",
                            "Hunting for a fortune of gold in an old cemetery",
                            "http://ia.media-imdb.com/images/M/MV5BOTQ5NDI3MTI4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=WCN5JJY_wiA")

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him. ",
                           "http://ia.media-imdb.com/images/M/MV5BMTI1Nzk1MzQwMV5BMl5BanBnXkFtZTYwODkxOTA5._V1_UY268_CR2,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

lion_king = media.Movie("The Lion King",
                       "Adventures of a young lion who takes back his father's kingdom",
                       "http://ia.media-imdb.com/images/M/MV5BMjEyMzgwNTUzMl5BMl5BanBnXkFtZTcwNTMxMzM3Ng@@._V1_UY268_CR12,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=4sj1MT05lAA")

# Define a list and add all the created instances of Movie to it
movies = [usual_suspects, finding_nemo, jurassic_park, good_bad_ugly, forrest_gump, lion_king]

# Pass the list of movies to the function to open the movies page 
fresh_tomatoes.open_movies_page(movies)
