class TextBox:
    full_name: str
    email: str
    current_address: str
    permanent_address: str

    def __init__(self, full_name, email, current_address, permanent_address):
        self.full_name = full_name
        self.email = email
        self.current_address = current_address
        self.permanent_address = permanent_address
