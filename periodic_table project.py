# Complete Periodic Table with additional properties
periodic_table = {
    1: {'name': 'Hydrogen', 'symbol': 'H', 'atomic_mass': 1.008, 'group': 1, 'period': 1, 'category': 'Non-metal'},
    2: {'name': 'Helium', 'symbol': 'He', 'atomic_mass': 4.0026, 'group': 18, 'period': 1, 'category': 'Noble gas'},
    3: {'name': 'Lithium', 'symbol': 'Li', 'atomic_mass': 6.94, 'group': 1, 'period': 2, 'category': 'Alkali metal'},
    4: {'name': 'Beryllium', 'symbol': 'Be', 'atomic_mass': 9.0122, 'group': 2, 'period': 2, 'category': 'Alkaline earth metal'},
    5: {'name': 'Boron', 'symbol': 'B', 'atomic_mass': 10.81, 'group': 13, 'period': 2, 'category': 'Metalloid'},
    6: {'name': 'Carbon', 'symbol': 'C', 'atomic_mass': 12.011, 'group': 14, 'period': 2, 'category': 'Non-metal'},
    7: {'name': 'Nitrogen', 'symbol': 'N', 'atomic_mass': 14.007, 'group': 15, 'period': 2, 'category': 'Non-metal'},
    8: {'name': 'Oxygen', 'symbol': 'O', 'atomic_mass': 15.999, 'group': 16, 'period': 2, 'category': 'Non-metal'},
    9: {'name': 'Fluorine', 'symbol': 'F', 'atomic_mass': 18.998, 'group': 17, 'period': 2, 'category': 'Non-metal'},
    10: {'name': 'Neon', 'symbol': 'Ne', 'atomic_mass': 20.180, 'group': 18, 'period': 2, 'category': 'Noble gas'},
    11: {'name': 'Sodium', 'symbol': 'Na', 'atomic_mass': 22.990, 'group': 1, 'period': 3, 'category': 'Alkali metal'},
    12: {'name': 'Magnesium', 'symbol': 'Mg', 'atomic_mass': 24.305, 'group': 2, 'period': 3, 'category': 'Alkaline earth metal'},
    13: {'name': 'Aluminum', 'symbol': 'Al', 'atomic_mass': 26.982, 'group': 13, 'period': 3, 'category': 'Post-transition metal'},
    14: {'name': 'Silicon', 'symbol': 'Si', 'atomic_mass': 28.085, 'group': 14, 'period': 3, 'category': 'Metalloid'},
    15: {'name': 'Phosphorus', 'symbol': 'P', 'atomic_mass': 30.974, 'group': 15, 'period': 3, 'category': 'Non-metal'},
    16: {'name': 'Sulfur', 'symbol': 'S', 'atomic_mass': 32.06, 'group': 16, 'period': 3, 'category': 'Non-metal'},
    17: {'name': 'Chlorine', 'symbol': 'Cl', 'atomic_mass': 35.45, 'group': 17, 'period': 3, 'category': 'Non-metal'},
    18: {'name': 'Argon', 'symbol': 'Ar', 'atomic_mass': 39.948, 'group': 18, 'period': 3, 'category': 'Noble gas'},
    19: {'name': 'Potassium', 'symbol': 'K', 'atomic_mass': 39.098, 'group': 1, 'period': 4, 'category': 'Alkali metal'},
    20: {'name': 'Calcium', 'symbol': 'Ca', 'atomic_mass': 40.078, 'group': 2, 'period': 4, 'category': 'Alkaline earth metal'},
    21: {'name': 'Scandium', 'symbol': 'Sc', 'atomic_mass': 44.956, 'group': 3, 'period': 4, 'category': 'Transition metal'},
    22: {'name': 'Titanium', 'symbol': 'Ti', 'atomic_mass': 47.867, 'group': 4, 'period': 4, 'category': 'Transition metal'},
    23: {'name': 'Vanadium', 'symbol': 'V', 'atomic_mass': 50.942, 'group': 5, 'period': 4, 'category': 'Transition metal'},
    24: {'name': 'Chromium', 'symbol': 'Cr', 'atomic_mass': 51.996, 'group': 6, 'period': 4, 'category': 'Transition metal'},
    25: {'name': 'Manganese', 'symbol': 'Mn', 'atomic_mass': 54.938, 'group': 7, 'period': 4, 'category': 'Transition metal'},
    26: {'name': 'Iron', 'symbol': 'Fe', 'atomic_mass': 55.845, 'group': 8, 'period': 4, 'category': 'Transition metal'},
    27: {'name': 'Cobalt', 'symbol': 'Co', 'atomic_mass': 58.933, 'group': 9, 'period': 4, 'category': 'Transition metal'},
    28: {'name': 'Nickel', 'symbol': 'Ni', 'atomic_mass': 58.693, 'group': 10, 'period': 4, 'category': 'Transition metal'},
    29: {'name': 'Copper', 'symbol': 'Cu', 'atomic_mass': 63.546, 'group': 11, 'period': 4, 'category': 'Transition metal'},
    30: {'name': 'Zinc', 'symbol': 'Zn', 'atomic_mass': 65.38, 'group': 12, 'period': 4, 'category': 'Transition metal'},
    31: {'name': 'Gallium', 'symbol': 'Ga', 'atomic_mass': 69.723, 'group': 13, 'period': 4, 'category': 'Post-transition metal'},
    32: {'name': 'Germanium', 'symbol': 'Ge', 'atomic_mass': 72.64, 'group': 14, 'period': 4, 'category': 'Metalloid'},
    33: {'name': 'Arsenic', 'symbol': 'As', 'atomic_mass': 74.922, 'group': 15, 'period': 4, 'category': 'Metalloid'},
    34: {'name': 'Selenium', 'symbol': 'Se', 'atomic_mass': 78.96, 'group': 16, 'period': 4, 'category': 'Non-metal'},
    35: {'name': 'Bromine', 'symbol': 'Br', 'atomic_mass': 79.904, 'group': 17, 'period': 4, 'category': 'Non-metal'},
    36: {'name': 'Krypton', 'symbol': 'Kr', 'atomic_mass': 83.798, 'group': 18, 'period': 4, 'category': 'Noble gas'},
    37: {'name': 'Rubidium', 'symbol': 'Rb', 'atomic_mass': 85.468, 'group': 1, 'period': 5, 'category': 'Alkali metal'},
    38: {'name': 'Strontium', 'symbol': 'Sr', 'atomic_mass': 87.62, 'group': 2, 'period': 5, 'category': 'Alkaline earth metal'},
    39: {'name': 'Yttrium', 'symbol': 'Y', 'atomic_mass': 88.906, 'group': 3, 'period': 5, 'category': 'Transition metal'},
    40: {'name': 'Zirconium', 'symbol': 'Zr', 'atomic_mass': 91.224, 'group': 4, 'period': 5, 'category': 'Transition metal'},
    41: {'name': 'Niobium', 'symbol': 'Nb', 'atomic_mass': 92.906, 'group': 5, 'period': 5, 'category': 'Transition metal'},
    42: {'name': 'Molybdenum', 'symbol': 'Mo', 'atomic_mass': 95.94, 'group': 6, 'period': 5, 'category': 'Transition metal'},
    43: {'name': 'Technetium', 'symbol': 'Tc', 'atomic_mass': 98, 'group': 7, 'period': 5, 'category': 'Transition metal'},
    44: {'name': 'Ruthenium', 'symbol': 'Ru', 'atomic_mass': 101.07, 'group': 8, 'period': 5, 'category': 'Transition metal'},
    45: {'name': 'Rhodium', 'symbol': 'Rh', 'atomic_mass': 102.91, 'group': 9, 'period': 5, 'category': 'Transition metal'},
    46: {'name': 'Palladium', 'symbol': 'Pd', 'atomic_mass': 106.42, 'group': 10, 'period': 5, 'category': 'Transition metal'},
    47: {'name': 'Silver', 'symbol': 'Ag', 'atomic_mass': 107.868, 'group': 11, 'period': 5, 'category': 'Transition metal'},
    48: {'name': 'Cadmium', 'symbol': 'Cd', 'atomic_mass': 112.41, 'group': 12, 'period': 5, 'category': 'Transition metal'},
    49: {'name': 'Indium', 'symbol': 'In', 'atomic_mass': 114.82, 'group': 13, 'period': 5, 'category': 'Post-transition metal'},
    50: {'name': 'Tin', 'symbol': 'Sn', 'atomic_mass': 118.71, 'group': 14, 'period': 5, 'category': 'Post-transition metal'},
    51: {'name': 'Antimony', 'symbol': 'Sb', 'atomic_mass': 121.76, 'group': 15, 'period': 5, 'category': 'Metalloid'},
    52: {'name': 'Tellurium', 'symbol': 'Te', 'atomic_mass': 127.60, 'group': 16, 'period': 5, 'category': 'Metalloid'},
    53: {'name': 'Iodine', 'symbol': 'I', 'atomic_mass': 126.90, 'group': 17, 'period': 5, 'category': 'Non-metal'},
    54: {'name': 'Xenon', 'symbol': 'Xe', 'atomic_mass': 131.29, 'group': 18, 'period': 5, 'category': 'Noble gas'},
    55: {'name': 'Cesium', 'symbol': 'Cs', 'atomic_mass': 132.91, 'group': 1, 'period': 6, 'category': 'Alkali metal'},
    56: {'name': 'Barium', 'symbol': 'Ba', 'atomic_mass': 137.33, 'group': 2, 'period': 6, 'category': 'Alkaline earth metal'},
    57: {'name': 'Lanthanum', 'symbol': 'La', 'atomic_mass': 138.91, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    58: {'name': 'Cerium', 'symbol': 'Ce', 'atomic_mass': 140.12, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    59: {'name': 'Praseodymium', 'symbol': 'Pr', 'atomic_mass': 140.91, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    60: {'name': 'Neodymium', 'symbol': 'Nd', 'atomic_mass': 144.24, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    61: {'name': 'Promethium', 'symbol': 'Pm', 'atomic_mass': 145, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    62: {'name': 'Samarium', 'symbol': 'Sm', 'atomic_mass': 150.36, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    63: {'name': 'Europium', 'symbol': 'Eu', 'atomic_mass': 151.98, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    64: {'name': 'Gadolinium', 'symbol': 'Gd', 'atomic_mass': 157.25, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    65: {'name': 'Terbium', 'symbol': 'Tb', 'atomic_mass': 158.93, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    66: {'name': 'Dysprosium', 'symbol': 'Dy', 'atomic_mass': 162.50, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    67: {'name': 'Holmium', 'symbol': 'Ho', 'atomic_mass': 164.93, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    68: {'name': 'Erbium', 'symbol': 'Er', 'atomic_mass': 167.26, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    69: {'name': 'Thulium', 'symbol': 'Tm', 'atomic_mass': 168.93, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    70: {'name': 'Ytterbium', 'symbol': 'Yb', 'atomic_mass': 173.04, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    71: {'name': 'Lutetium', 'symbol': 'Lu', 'atomic_mass': 175.00, 'group': 3, 'period': 6, 'category': 'Lanthanide'},
    72: {'name': 'Hafnium', 'symbol': 'Hf', 'atomic_mass': 178.49, 'group': 4, 'period': 6, 'category': 'Transition metal'},
    73: {'name': 'Tantalum', 'symbol': 'Ta', 'atomic_mass': 180.95, 'group': 5, 'period': 6, 'category': 'Transition metal'},
    74: {'name': 'Tungsten', 'symbol': 'W', 'atomic_mass': 183.84, 'group': 6, 'period': 6, 'category': 'Transition metal'},
    75: {'name': 'Rhenium', 'symbol': 'Re', 'atomic_mass': 186.21, 'group': 7, 'period': 6, 'category': 'Transition metal'},
    76: {'name': 'Osmium', 'symbol': 'Os', 'atomic_mass': 190.23, 'group': 8, 'period': 6, 'category': 'Transition metal'},
    77: {'name': 'Iridium', 'symbol': 'Ir', 'atomic_mass': 192.22, 'group': 9, 'period': 6, 'category': 'Transition metal'},
    78: {'name': 'Platinum', 'symbol': 'Pt', 'atomic_mass': 195.08, 'group': 10, 'period': 6, 'category': 'Transition metal'},
    79: {'name': 'Gold', 'symbol': 'Au', 'atomic_mass': 196.97, 'group': 11, 'period': 6, 'category': 'Transition metal'},
    80: {'name': 'Mercury', 'symbol': 'Hg', 'atomic_mass': 200.59, 'group': 12, 'period': 6, 'category': 'Transition metal'},
    81: {'name': 'Thallium', 'symbol': 'Tl', 'atomic_mass': 204.38, 'group': 13, 'period': 6, 'category': 'Post-transition metal'},
    82: {'name': 'Lead', 'symbol': 'Pb', 'atomic_mass': 207.2, 'group': 14, 'period': 6, 'category': 'Post-transition metal'},
    83: {'name': 'Bismuth', 'symbol': 'Bi', 'atomic_mass': 208.98, 'group': 15, 'period': 6, 'category': 'Post-transition metal'},
    84: {'name': 'Polonium', 'symbol': 'Po', 'atomic_mass': 209, 'group': 16, 'period': 6, 'category': 'Metalloid'},
    85: {'name': 'Astatine', 'symbol': 'At', 'atomic_mass': 210, 'group': 17, 'period': 6, 'category': 'Non-metal'},
    86: {'name': 'Radon', 'symbol': 'Rn', 'atomic_mass': 222, 'group': 18, 'period': 6, 'category': 'Noble gas'},
    87: {'name': 'Francium', 'symbol': 'Fr', 'atomic_mass': 223, 'group': 1, 'period': 7, 'category': 'Alkali metal'},
    88: {'name': 'Radium', 'symbol': 'Ra', 'atomic_mass': 226, 'group': 2, 'period': 7, 'category': 'Alkaline earth metal'},
    89: {'name': 'Actinium', 'symbol': 'Ac', 'atomic_mass': 227, 'group': 3, 'period': 7, 'category': 'Actinide'},
    90: {'name': 'Thorium', 'symbol': 'Th', 'atomic_mass': 232.04, 'group': 3, 'period': 7, 'category': 'Actinide'},
    91: {'name': 'Protactinium', 'symbol': 'Pa', 'atomic_mass': 231.04, 'group': 3, 'period': 7, 'category': 'Actinide'},
    92: {'name': 'Uranium', 'symbol': 'U', 'atomic_mass': 238.03, 'group': 3, 'period': 7, 'category': 'Actinide'},
    93: {'name': 'Neptunium', 'symbol': 'Np', 'atomic_mass': 237, 'group': 3, 'period': 7, 'category': 'Actinide'},
    94: {'name': 'Plutonium', 'symbol': 'Pu', 'atomic_mass': 244, 'group': 3, 'period': 7, 'category': 'Actinide'},
    95: {'name': 'Americium', 'symbol': 'Am', 'atomic_mass': 243, 'group': 3, 'period': 7, 'category': 'Actinide'},
    96: {'name': 'Curium', 'symbol': 'Cm', 'atomic_mass': 247, 'group': 3, 'period': 7, 'category': 'Actinide'},
    97: {'name': 'Berkelium', 'symbol': 'Bk', 'atomic_mass': 247, 'group': 3, 'period': 7, 'category': 'Actinide'},
    98: {'name': 'Californium', 'symbol': 'Cf', 'atomic_mass': 251, 'group': 3, 'period': 7, 'category': 'Actinide'},
    99: {'name': 'Einsteinium', 'symbol': 'Es', 'atomic_mass': 252, 'group': 3, 'period': 7, 'category': 'Actinide'},
    100: {'name': 'Fermium', 'symbol': 'Fm', 'atomic_mass': 257, 'group': 3, 'period': 7, 'category': 'Actinide'},
    101: {'name': 'Mendelevium', 'symbol': 'Md', 'atomic_mass': 258, 'group': 3, 'period': 7, 'category': 'Actinide'},
    102: {'name': 'Nobelium', 'symbol': 'No', 'atomic_mass': 259, 'group': 3, 'period': 7, 'category': 'Actinide'},
    103: {'name': 'Lawrencium', 'symbol': 'Lr', 'atomic_mass': 262, 'group': 3, 'period': 7, 'category': 'Actinide'},
    104: {'name': 'Rutherfordium', 'symbol': 'Rf', 'atomic_mass': 267, 'group': 4, 'period': 7, 'category': 'Transition metal'},
    105: {'name': 'Dubnium', 'symbol': 'Db', 'atomic_mass': 270, 'group': 5, 'period': 7, 'category': 'Transition metal'},
    106: {'name': 'Seaborgium', 'symbol': 'Sg', 'atomic_mass': 271, 'group': 6, 'period': 7, 'category': 'Transition metal'},
    107: {'name': 'Bohrium', 'symbol': 'Bh', 'atomic_mass': 270, 'group': 7, 'period': 7, 'category': 'Transition metal'},
    108: {'name': 'Hassium', 'symbol': 'Hs', 'atomic_mass': 277, 'group': 8, 'period': 7, 'category': 'Transition metal'},
    109: {'name': 'Meitnerium', 'symbol': 'Mt', 'atomic_mass': 278, 'group': 9, 'period': 7, 'category': 'Transition metal'},
    110: {'name': 'Darmstadtium', 'symbol': 'Ds', 'atomic_mass': 281, 'group': 10, 'period': 7, 'category': 'Transition metal'},
    111: {'name': 'Roentgenium', 'symbol': 'Rg', 'atomic_mass': 280, 'group': 11, 'period': 7, 'category': 'Transition metal'},
    112: {'name': 'Copernicium', 'symbol': 'Cn', 'atomic_mass': 285, 'group': 12, 'period': 7, 'category': 'Transition metal'},
    113: {'name': 'Nihonium', 'symbol': 'Nh', 'atomic_mass': 284, 'group': 13, 'period': 7, 'category': 'Post-transition metal'},
    114: {'name': 'Flerovium', 'symbol': 'Fl', 'atomic_mass': 289, 'group': 14, 'period': 7, 'category': 'Post-transition metal'},
    115: {'name': 'Moscovium', 'symbol': 'Mc', 'atomic_mass': 288, 'group': 15, 'period': 7, 'category': 'Post-transition metal'},
    116: {'name': 'Livermorium', 'symbol': 'Lv', 'atomic_mass': 293, 'group': 16, 'period': 7, 'category': 'Post-transition metal'},
    117: {'name': 'Tennessine', 'symbol': 'Ts', 'atomic_mass': 294, 'group': 17, 'period': 7, 'category': 'Non-metal'},
    118: {'name': 'Oganesson', 'symbol': 'Og', 'atomic_mass': 294, 'group': 18, 'period': 7, 'category': 'Noble gas'}
}
def search_periodic_table(query, search_type='name'):
    """
    Search the periodic table based on different attributes such as name, symbol, atomic number, and atomic mass.
    """
    query = str(query).lower()  # Convert query to lowercase for case-insensitive search

    if search_type == 'name':
        for atomic_number, element_data in periodic_table.items():
            if element_data['name'].lower() == query:
                return atomic_number, element_data

    elif search_type == 'symbol':
        for atomic_number, element_data in periodic_table.items():
            if element_data['symbol'].lower() == query:
                return atomic_number, element_data

    elif search_type == 'atomic_number':
        try:
            atomic_number = int(query)
            if atomic_number in periodic_table:
                return atomic_number, periodic_table[atomic_number]
        except ValueError:
            return None

    elif search_type == 'atomic_mass':
        try:
            atomic_mass = float(query)
            for atomic_number, element_data in periodic_table.items():
                if abs(element_data['atomic_mass'] - atomic_mass) < 0.001:
                    return atomic_number, element_data
        except ValueError:
            return None

    return None


def display_element_info(atomic_number, element_data):
    """
    Display the element information in a clean, organized way with added categories.
    """
    print("\nElement Information:")
    print(f"Name: {element_data['name']}")
    print(f"Symbol: {element_data['symbol']}")
    print(f"Atomic Number: {atomic_number}")
    print(f"Atomic Mass: {element_data['atomic_mass']}")
    print(f"Group: {element_data['group']}")
    print(f"Period: {element_data['period']}")
    print(f"Category: {element_data['category']}")


def run_periodic_table_search():
    """
    Run a loop to allow users to search the periodic table interactively.
    """
    while True:
        print("\nSearch the Periodic Table:")
        print("1. Search by Name")
        print("2. Search by Symbol")
        print("3. Search by Atomic Number")
        print("4. Search by Atomic Mass")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter element name: ")
            result = search_periodic_table(name, 'name')
        elif choice == '2':
            symbol = input("Enter element symbol: ")
            result = search_periodic_table(symbol, 'symbol')
        elif choice == '3':
            number = input("Enter atomic number: ")
            result = search_periodic_table(number, 'atomic_number')
        elif choice == '4':
            mass = input("Enter atomic mass: ")
            result = search_periodic_table(mass, 'atomic_mass')
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if result:
            atomic_number, element_data = result
            display_element_info(atomic_number, element_data)
        else:
            print("Element not found.")


if __name__ == "__main__":
    run_periodic_table_search()