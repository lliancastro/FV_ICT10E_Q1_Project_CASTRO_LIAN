from pyscript import display, document




    customer_name = document.getElementById("customerName").value
    customer_address = document.getElementById("customerAddress").value
    customer_number = document.getElementById("customerNumber").value
    checkboxes = document.querySelectorAll("input[name='item']")
    selected_items = []
    total = 0

    for checkbox in checkboxes:
        if checkbox.checked:
            selected_items.append(checkbox.value)
            total += items_prices[checkbox.value]

    if selected_items:
        items_str = ", ".join(selected_items)
    else:
        items_str = "(no items selected)"

    message = f"""
<strong>Order Summary:</strong><br>
    ---------------------------- <br> 
Customer Name: {customer_name} <br> 
Delivery Address: {customer_address} <br> 
Contact Number: {customer_number} <br>
Items Ordered: {items_str} <br>
<strong>Total:</strong> ₱{total:.2f} <br>
    """
    document.getElementById("result").innerHTML = message
items_prices = {
        "Matcharap Cookie": 170
        "Halaya Cookie": 170
        "Cookie-Bomb": 170
        "Biscoff Crush Cookie": 170
        "Birthday Confetti": 170
}