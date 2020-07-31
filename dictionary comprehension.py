movie_list = {"Intestellar": 9, "Dark Knight": 8,
              "50 Shades": 3, "50 Shades Darker": 2, "50 Shades Darkest": 1}
new_list = []
for movie in movie_list:
    if movie_list[movie] > 6:
        new_list.append(movie)

print(new_list)


new_list = [movie for movie in movie_list if movie_list[movie] > 6]
print(new_list)
