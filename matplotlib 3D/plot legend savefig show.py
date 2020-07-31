import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()
    for row in csv_reader:
        language_counter.update((row)['LanguagesWorkedWith'].split(';'))


'''
    # row = next(csv_reader)
    # print(row['LanguagesWorkedWith'].split(';'))

from collections import Counter
c=Counter(['Python', 'JavaScript'])
print(c)
c.update(['C++', 'Python'])
print(c)
c.update(['C++', 'Python'])
print(c)
'''


# print(language_counter.most_common(15))

languages = []
popularity = []

for item in language_counter.most_common(15):  # we could use zip to
    languages.append(item[0])
    popularity.append(item[1])


# print(languages)
# print(popularity)

plt.barh(languages, popularity)
plt.title("Most Popular Languages")
plt.xlabel("Number of People Who use")

plt.tight_layout()
plt.show()
