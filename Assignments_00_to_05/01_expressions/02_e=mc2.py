# Constant for the speed of light
C: int = 299_792_458  # in meters per second

def main():
    while True:
        try:
            # Get mass input from user
            mass_in_kg: float = float(input("Enter kilos of mass: "))

            # Calculate energy using Einstein's formula
            energy_in_joules: float = mass_in_kg * (C ** 2)

            # Display results
            print("\ne = m * C^2...")
            print(f"m = {mass_in_kg} kg")
            print(f"C = {C} m/s")
            print(f"{energy_in_joules} joules of energy!\n")
        except ValueError:
            print("Please enter a valid number.\n")

# Required to run the program
if __name__ == '__main__':
    main()
