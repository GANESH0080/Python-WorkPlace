def Sampleminimal():
    total = 100
    country = "US"
    #country = "AU"
    if country == "AU":
        print("Country is :",country)
        if total <= 50:
            print("Shipping Cost is  $50")
    elif total <= 100:
        print("Shipping Cost is $25")
    elif total <= 150:
        print("Shipping Costs $5")
    else:
        print("FREE")
    if country == "AU":
        if total <= 50:
           print("Shipping Cost is  $100")
    else:
        print("FREE")

Sampleminimal()