weather = input("what is the weather like today ? (sunny/rain/cold)").lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rain":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")