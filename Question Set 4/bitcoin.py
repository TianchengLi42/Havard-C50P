import requests
import sys
import json



def main():
    try:
        nb_bitcoin = float(sys.argv[-1])
        priceperbitcoin = get_bitcoin_price()
        price = nb_bitcoin * priceperbitcoin
        price = f"{price:,.2f}"
        print("$", price, sep="")

    except ValueError:
        print("That wasn't a valid number!")
    except requests.RequestException:
        print("Something went wrong!")

def get_bitcoin_price():
    response = requests.get(
        "https://rest.coincap.io/v3/assets?apiKey=YourAPIKey")
    data_ = response.json()
    for coin in data_["data"]:
        if coin["name"] == "Bitcoin":
            return (round(float(coin["priceUsd"]), 2))



main()

#data_ = json.dumps(data_, indent=2)



