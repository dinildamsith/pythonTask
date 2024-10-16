
destination = input("Enter the destination you want to travel to: ")


if destination == "Paris":
    message = "Bonjour! Enjoy your flight to the romantic city of Paris!"
elif destination == "Tokyo":
    message = "Konnichiwa! Have a great time exploring the vibrant city of Tokyo!"
elif destination == "New York":
    message = "Welcome to the Big Apple! Enjoy your stay in New York City!"
elif destination == "Sydney":
    message = "G'day mate! Have a fantastic trip to the beautiful city of Sydney!"
else:
    message = "Safe travels to your chosen destination!"


print(message)
