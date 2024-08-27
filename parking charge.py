def calculate_parking_charge(vehicle_type, hours):
    """
    Calculates the parking charge for a given vehicle type and number of hours.

    Args:
        vehicle_type (str): Type of vehicle (c for car, b for bus, t for truck, cy for cycle/bike)
        hours (int): Number of hours the vehicle is parked

    Returns:
        int: Parking charge
    """
    charges = {
        'c': 10,  # Car
        'b': 20,  # Bus
        't': 20,  # Truck
        'cy': 5   # Cycle/Bike
    }

    if vehicle_type in charges:
        return charges[vehicle_type] * hours
    else:
        print("Invalid vehicle type")
        return None

def main():
    print("Parking Charge Calculator")
    print("-------------------------")

    vehicle_type = input("Enter the type of vehicle (c for car, b for bus, t for truck, cy for cycle/bike): ")
    hours = int(input("Enter the number of hours: "))

    charge = calculate_parking_charge(vehicle_type, hours)

    if charge is not None:
        print(f"Parking charge: Rs. {charge}")

if __name__ == "__main__":
    main()
