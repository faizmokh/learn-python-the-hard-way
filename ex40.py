class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

birthday_list = ["Happy birthday to you", "I don't want to get sude", "So I'll stop right there"]
bulls_list = ["They rally around tha family", "With pockets full of shells"]

happy_bday = Song(birthday_list)
bulls_on_parade = Song(bulls_list)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()