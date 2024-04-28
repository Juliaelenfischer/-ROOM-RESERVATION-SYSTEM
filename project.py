import datetime

# Example data of room availability
room_availability = {
    "101": {"available": True, "price": 199.99},
    "102": {"available": True, "price": 120},
    "103": {"available": False, "price": 150}           
}

# Data sample for reservations
reservations = {}

def main():
    print("Welcome to the Board of Room Reservation System!")
    while True:
        print("\n1. Check room availability")
        print("2. Make reservation")
        print("3. Manage reservations")
        print("4. Cancel reservation")
        print("5. Generate invoice")
        print("6. Exit")

        option = input("Select an option: ")

        if option == "1":
            check_room_availability()
        elif option == "2":
            make_reservation()
        elif option == "3":
            manage_reservations()
        elif option == "4":
            cancel_reservation()
        elif option == "5":
            generate_invoice()
        elif option == "6":
            print("See you again. Thanks for using our system. Goodbye!")
            break
        else:
            print("The input is not a valid option. Please insert a valid option")

def check_room_availability():
    print("\nRoom Availability:")
    for room, info in room_availability.items():
        status = "Available" if info["available"] else "Not available"
        print(f"Room {room}: Status: {status}, Price: ${info['price']} per night")

def make_reservation():
    room = input("Enter room number: ")
    if room not in room_availability:
        print("Invalid room number.")
        return
    
    if room_availability[room]["available"]:
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
        
        try: 
            check_in = datetime.datetime.strptime(check_in_date, "%Y-%m-%d").date()
            check_out = datetime.datetime.strptime(check_out_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format.")
            return
        
        if check_in >= check_out:
            print("Check-out date must be after check-in date.")
            return
        
        # Add reservation to the dictionary
        reservations[room] = {"check_in": check_in, "check_out": check_out}
        room_availability[room]["available"] = False
        print("Reservation successful!")
    else:
        print("Room is not available for the selected dates.")

def manage_reservations():
    print("\nManage Reservations:")
    for room, reservation in reservations.items():
        print(f"Room {room}: Check-in: {reservation['check_in']}, Check-out: {reservation['check_out']}")

def cancel_reservation():
    room = input("Enter room number to cancel reservation: ")
    if room in reservations:
        del reservations[room]
        room_availability[room]["available"] = True
        print("Reservation canceled successfully.")
    else:
        print("No reservation found for the room number provided.")

def generate_invoice():
    room = input("Enter room number to generate invoice: ")
    if room in reservations:
        reservation = reservations[room]
        total_nights = (reservation["check_out"] - reservation["check_in"]).days
        total_price = total_nights * room_availability[room]["price"]
        print(f"Invoice for Room {room}:")
        print(f"Check-in: {reservation['check_in']}, Check-out: {reservation['check_out']}")
        print(f"Total nights: {total_nights}, Total price: ${total_price}")
    else:
        print("No reservation found for the room number provided.")

if __name__ == "__main__":
    main()