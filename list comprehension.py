names = ['Jennifer', 'Susan', 'Jane', 'Sophie']


list_names = []

for name in names:
    list_names.append(name)

# print(list_names)


list_names = [name for name in names]
print(list_names)


list_names = [name + ' danced with me' for name in names]
print(list_names)


numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []  # create a new list of odd numbers only


odd_numbers = [number for number in numbers if (number % 2) == 1]
print('Odd numbers using for loop', odd_numbers)

square_numbers = []
# square_numbers = [number*number (for number in numbers)]
square_numbers = [number*number for number in numbers]
print("New list of square numbers", square_numbers)


matrix = [(0, 1, 2),
          (3, 4, 5),
          (0, 1, 2),
          (3, 4, 5),
          (0, 1, 2),
          (3, 4, 5),
          (6, 7, 8)]

elemental_matrix = []
# elemental_matrix = [element (for row in matrix) (for element in row)]
elemental_matrix = [element for row in matrix for element in row]
print(elemental_matrix)

movies = [('Star wars', 1941), ('Gandhi', 2001), ('Casablanca', 1923), ('Gone with the wind', 1977),
          ('No Country for Old Men', 2007), ('The Aviator', 2004), ('Citizen kane', 1944)]

G_titles = []  # movies beginning with g

classic_movies = []  # movies older than 2000

G_titles = [movie for movie in movies if movie[0].startswith('G')]
print(G_titles)

classic_movies = [movie for movie in movies if movie[1] < 2000]
print(classic_movies)


# creates a 3x4 "matrix" (row =3, column=4) of 8.

mat3_4 = [[8 for col in range(4)] for row in range(3)]
print('Populating 4 x 3 matrix: ', mat3_4)
print()
