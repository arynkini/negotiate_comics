import csv
import json

def read_comics_from_csv():
    comics = []
    with open('comics.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        comics = list(reader)
    return comics

def choose_comic(comics):
    print("Available comics:")
    for index, comic in enumerate(comics):
        print(f"{index + 1}. {comic['Title']}")
    choice = int(input("Enter the number of the comic you want to select: ")) - 1
    return comics[choice]

if __name__ == "__main__":
    comics = read_comics_from_csv()
    selected_comic = choose_comic(comics)
    with open('selected_comic_info.json', 'w') as file:
        json.dump(selected_comic, file)
