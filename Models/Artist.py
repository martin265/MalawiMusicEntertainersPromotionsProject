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

    #  ============= // the function will save the records to the database
    def save_artist_records_func(self):
        """ the function to save the records to the database here"""
        try:
            data, count = supabase.table("Artists").insert(
                {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "email": self.email,
                    "phone_number": self.phone_number,
                    "gender": self.gender,
                    "age": self.age,
                    "genre": self.genre,
                    "residence": self.residence,
                    "artist_biography": self.artist_biography
                }
            ).execute()

        except Exception as ex:
            print("something went wrong at {}".format(ex))

    #  ================= // the function will be used to update the records
    def update_artist_record(self, current_update_id):
        """the function will update the records"""
        try:
            data, count = supabase.table("Artists").update(
                {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "email": self.email,
                    "phone_number": self.phone_number,
                    "gender": self.gender,
                    "age": self.age,
                    "genre": self.genre,
                    "residence": self.residence,
                    "artist_biography": self.artist_biography
                }
            ).eq("id", current_update_id).execute()
            # =========== running the database query here =========== //
        except Exception as ex:
            print(ex)
