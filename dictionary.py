""" {
    "key 1" : value1,
    "key 2" : value2,
} """

""" vac = {
    "name" : "Dyson V15 Cordless Vaccum",
    "price" : 699.99,
    "department" : "Appliances",
    "descrption" : "High-powered cordless vaccum with laser dust detection"
}

best_buy_items = [
    {
        "name": "Samsung 55\" 4K UHD TV",
        "price": 429.99,
        "department": "Televisions",
        "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
    },
    {
        "name": "Sony Noise Cancelling Headphones",
        "price": 299.99,
        "department": "Audio",
        "description": "Wireless over-ear headphones with industry-leading noise cancellation."
    },
    {
        "name": "Apple iPhone 15",
        "price": 999.99,
        "department": "Mobile Phones",
        "description": "Latest Apple smartphone with A17 chip and advanced camera system."
    }
]
 """
""" print(best_buy_items[0]["name"])
print(best_buy_items[0]["price"])
 """

Illit_merch = [
    {
        "name" : "Illit 1st Mini Album SUPER REAL ME(SUPER ME edition)",
        "price" : 29.99,
        "department" : "Music Albums",
        "description" : "Hit K-Pop group Illit's first mini album, comes with photocards, stickers, a CD, and posters."
    },
    {
        "name" : "Illit 2nd Mini Album I'LL LIKE YOU(WITH YOU edition)",
        "price" : 28.99,
        "department" : "Music Albums",
        "description" : "Hit K-Pop group Illit's second mini album, comes with photocards, stickers, a CD, and posters."
    },
    {
        "name" : "Illit 3rd Mini Album bomb(MAGIC BOMB edition)",
        "price" : 29.99,
        "department" : "Music Albums",
        "descrption" : "Hit K-Pop group Illit's third mini album, comes with photocards, stickers, a CD, and posters."
    },
    {
        "name" : "Illit 1st Single Album NOT CUTE ANYMORE(Not Cute edition)",
        "price" : 34.99,
        "department" : "Music Album",
        "description" : "Hit K-Pop group Illit's first single album, comes with photocards, stickers, a CD, and posters."
    },
    {
        "name" : "Illit 4th Mini Album MAMIHLAPINATAPAI(It's Me edition)",
        "price" : 26.98,
        "department" : "Music Album",
        "descrption" : "Hit K-Pop group Illit's fourth mini album, comes with photocards, stickers, a CD, and posters."
    }
]

print(Illit_merch[0]["name"])
print(Illit_merch[0]["price"])

def show_items(itmes):
    for index, item in enumerate(Illit_merch):
        print(index, ":", item["name"])

def choose_items():
    show_items(Illit_merch)
    x = int(input("What do you want to get?"))
    for i in range(6):
        x = input("Would you like to get anything else? If not, type no.")
        if x == "no":
            break
        if x == "yes":
            print(Illit_merch)
        print(Illit_merch[x])
choose_items()

