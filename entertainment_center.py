"""Create a list of my favorite movies"""
#!/usr/bin/python

import media
import fresh_tomatoes
"""
movie_title = media.Movie(
    "Movie Title",
    "Movie Storyline",
    "Poster Image Url",
    "Youtube Trailer Url")
"""
pacific_rim = media.Movie(
    "Pacific Rim",
    "As a war between humankind and monstrous sea creatures wages on, a former pilot and a trainee are paired up to drive a seemingly obsolete special weapon in a desperate effort to save the world from the apocalypse.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3MTI5NjQ4Nl5BMl5BanBnXkFtZTcwOTU1OTU0OQ@@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=BeEkAnCesxw")

true_lies = media.Movie(
    "True Lies",
    "A fearless, globe-trotting, terrorist-battling secret agent has his life turned upside down when he discovers his wife might be having an affair with a used car salesman.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BYzg5YmUyNGMtMThiNS00MjA2LTgwZDctNDlhM2RkZDNmZmRkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=kWVFgUo5Btg")

the_dark_knight = media.Movie(
    "The Dark Knight",
    "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=qY3UkAHufLY")

snatch = media.Movie(
    "Snatch",
    "Unscrupulous boxing promoters, violent bookmakers, a Russian gangster, incompetent amateur robbers, and supposedly Jewish jewelers fight to track down a priceless stolen diamond.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA2NDYxOGYtYjU1Mi00Y2QzLTgxMTQtMWI1MGI0ZGQ5MmU4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_SX684_AL_.jpg",
    "https://www.youtube.com/watch?v=laNboH3hjiM")

forrest_gump = media.Movie(
    "Forrest Gump",
    "While not intelligent, Forrest Gump has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=EtYNngO7eq4")

interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=Df7IEKqimOY")

#List of movie
movies = [pacific_rim, true_lies, the_dark_knight, snatch, forrest_gump, interstellar] 
#Generate fresh_tomatoes.html
fresh_tomatoes.open_movies_page(movies)
