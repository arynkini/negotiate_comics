import json

def read_selected_comic_info():
    with open('selected_comic_info.json', 'r') as file:
        selected_comic = json.load(file)
    return selected_comic

def get_user_best_offer():
    best_offer = float(input("Enter your best offer price: "))
    return best_offer

def save_offer_details(comic_info, best_offer):
    comic_info['Best Offer'] = best_offer
    with open('offer_details.json', 'w') as file:
        json.dump(comic_info, file)

if __name__ == "__main__":
    selected_comic = read_selected_comic_info()
    best_offer = get_user_best_offer()
    save_offer_details(selected_comic, best_offer)
