def make_sandwich(*toppings):
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich("turkey")
make_sandwich("eggmayo", "bacon")
make_sandwich("steak", "cheese", "onion")
