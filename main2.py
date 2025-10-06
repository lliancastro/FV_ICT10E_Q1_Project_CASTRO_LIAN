from pyscript import display

owner = "Lian Castro" # name
year_founded = "2025" # integer
popular_item_price1 = "Biko : 70 pesos" # floating-point
popular_item_price2 = "Ube Halaya : 70 pesos" # floating-point
popular_item_price3 = "Sapin-Sapin : 70 pesos" # floating-point
business_hours = "9:30 AM - 10:30 PM" # tuple
has_delivery=(False) # Boolean

# everything from here on out is display
display(owner,  target= "ownerName")
display(year_founded, target= "yearFounded")
display(popular_item_price1, target= "popularitemPrice")
display(popular_item_price2, target= "popularitemPrice")
display(popular_item_price3, target= "popularitemPrice")
display(business_hours, target= "businessHours")
display(has_delivery, target= "hasDelivery")