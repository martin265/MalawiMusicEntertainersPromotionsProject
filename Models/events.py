import flet as ft
import supabase

class Events:
    def __init__(self, ticket_type, ticket_price, event_name, event_type,
                 event_capacity, event_organizers, special_offers, accessibility_information,
                 age_restrictions, event_description, payment_methods, event_category,
                 artists_name):
        super().__init__()
        self.ticket_name = ticket_type
        self.ticket_price = ticket_price
        self.event_name = event_name
        self.event_type = event_type
        self.event_capacity = event_capacity
        self.event_organizers = event_organizers
        self.special_offers = special_offers
        self.accessibility_information = accessibility_information
        self.age_restrictions = age_restrictions
        self.event_description = event_description
        self.payment_methods = payment_methods
        self.event_category = event_category
        self.artists_name = artists_name

    def save_events_details_fun(self):
        try:

        except Exception as ex:
            print(ex)