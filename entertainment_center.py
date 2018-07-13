import media
import fresh_tomatoes


# movie_1, movie_2, movie_3, movie_4, movie_5 and movie_6 corresponds to the
# 	instances of the class 'Movie' defined in the file 'media.py'.
movie_1 = media.Movie(
  "Black Panther",
  "https://goo.gl/bz4wpL",
  "https://www.youtube.com/watch?v=xjDjIWPwcPU"
  )
movie_2 = media.Movie(
  "Wonder Woman",
  "https://goo.gl/K7dHM5",
  "https://www.youtube.com/watch?v=1Q8fG0TtVAY"
  )
movie_3 = media.Movie(
  "Justice League",
  "https://goo.gl/MyJ4UX",
  "https://www.youtube.com/watch?v=r9-DM9uBtVI"
  )
movie_4 = media.Movie(
  "Avengers: Infinity War",
  "https://goo.gl/DmDggs",
  "https://www.youtube.com/watch?v=QwievZ1Tx-8"
  )
movie_5 = media.Movie(
  "Batman VS Superman",
  "https://goo.gl/3bajD9",
  "https://www.youtube.com/watch?v=0WWzgGyAH6Y"
  )
movie_6 = media.Movie(
  "Ant-man and the Wasp",
  "https://goo.gl/Zo9sYF",
  "https://www.youtube.com/watch?v=8_rTIAOohas"
  )

# Variable 'movie_list' creates a 'list' of the instances of class 'Movie'
movie_list = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]

# Below given function open_movies_page creates our required web-page.
fresh_tomatoes.open_movies_page(movie_list)
