class library:
    def __init__(self, title, author ,available=True):
        self.title = title
        self.author = author
        self.available = available
    
    def checkout(self):
        if self.available:
            self.available = False
            return f"You have checked out '{self.title}' by {self.author}."
        else:
            return f"Sorry, '{self.title}' is currently unavailable."
    
    def return_book(self):
        self.available = True
        return f"You have returned '{self.title}'. Thank you!"
    
    def display_info(self):
        availability = "Available" if self.available else "Checked Out"
        return f"Title: {self.title}, Author: {self.author}, Status: {availability}"

book1 = library("2025", "Python1", "Sarthak")
print(book1.checkout())
print(book1.return_book())
print(book1.display_info())


   