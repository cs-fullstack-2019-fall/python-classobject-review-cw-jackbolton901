# !! : MORE COMMNETS!!!!!
# Problem 1

class Movie:
    def __init__(self, movieName, rating, yearRelease):
        self.movieName = movieName
        self.rating = rating
        self.yearRelease = yearRelease
    def __str__(self):
         theStr = f'Properties for the class Movies\n' \
              f'movieName = {self.movieName}\n' \
              f'rating = {self.rating}\n' \
              f'yearRelease = {self.yearRelease}'
         return theStr


thriller = Movie("The Mummy", "pg-13", "1999")
action = Movie("Crank", "R", "2005")
print(thriller)

# Problem 2

class Product:
    def __init__(self, price, quantity, name):
        self.price = price
        self.quantity = quantity
        self.name = name
    def __str__(self):
        myStr = f'Properties from the class Product\n' \
               f'Price = {self.price}\n' \
               f'Quantity = {self.quantity}\n' \
               f'Name = {self.name}'
        return myStr

prod = Product("$4.99","1", "oldspice")
prod2 = Product("$10", "2", "Tshirts")
print(prod)