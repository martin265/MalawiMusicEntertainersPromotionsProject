import flet as ft
from Pages.events import InputControls


class ValidateInputs(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ======== getting the inputs here ========= //
        self.inputControls = InputControls(page=page)

    def validate_input_fields(self, e):
        """the function will be used to validate the input fields"""
        if not self.inputControls.event_title.value:
            self.inputControls.event_title.error_text = "please fill in the blank".title()
            self.update()

