import os
from Config.config import supabase


class Artist:
    def __init__(self, first_name, last_name, email, phone_number, gender,
                 age, genre, residence, artist_biography):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.gender = gender
        self.age = age
        self.genre = genre
        self.residence = residence
        self.artist_biography = artist_biography


    def save_artist_records_func(self):
        try:

        except Exception as ex:
            print("something went wrong at {}".format(ex))
