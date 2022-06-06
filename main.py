import requests
import bs4


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

html_text = requests.get(URL).text

soup = bs4.BeautifulSoup(html_text, "html.parser")

title_tags = soup.find_all(name="h3", class_="title")

with open("movie.txt", "w", encoding="utf8") as file:
    for tag in reversed(title_tags):
        file.write(f"{tag.get_text()}\n")

# OR
# title_tags = soup.find_all(name="h3", class_="title")[::-1]
#
#
# with open("movie.txt", "w", encoding="utf8") as file:
#     for tag in title_tags:
#         file.write(f"{tag.get_text()}\n")
