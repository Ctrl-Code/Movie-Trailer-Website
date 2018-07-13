import webbrowser


class Movie():
    """This is the movie class template to store the movie title, movie image
        url and movie trailer from youtube"""

    def __init__(self, movie_title, url_image, url_trailer):
        """The 'title' attribute is used to set up the movie name in
        web-page"""
        self.title = movie_title

        """This attribute 'poster_image_url' will set the image of the movie
        on the web-page from this attribute"""

        self.poster_image_url = url_image
        """The'trailer_youtube_url' attribute will set up the link that will be
        opened when we click our movie on web-page"""
        self.trailer_youtube_url = url_trailer

    # To display the movie trailer in a scaled window.
    def show_trailer(self):
        webbrowser.open(self.trailer)
