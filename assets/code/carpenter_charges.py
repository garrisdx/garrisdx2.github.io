# Dakota Garrison
# 03/27/23
# program that determines a final cost of a desk based on order/design specifications

length = int(input("Enter the length in inches: "))
width = int(input("Enter the width of the desk in inches: "))
wood = input("Enter the type of wood (Oak, Mahogany, Pine) : ")
drawers = int(input("Enter the number of drawers: "))


base_desk = 200

# surface area
area = length * width

# wood_surface represents the value for a charge that is both wood based and surface based.
# value determined in match case and used then in calculation for surface charges

# charges for wood type
match wood:
    case "Mahogany" | "mahogany" if area > 750:
        wood_charge = 150
        wood_surface = 90
    case "Mahogany" | "mahogany" if area <= 750:
        wood_charge = 150
        wood_surface = 0
    case "Oak" | "oak" if area > 500:
        wood_charge = 125
        wood_surface = 45
    case "Oak" | "oak" if area <= 500:
        wood_charge = 125
        wood_surface = 0
    case "Pine" | "pine" if area > 1000:
        wood_charge = 0
        wood_surface = -80
    case "Pine" | "pine" if area <= 1000:
        wood_charge = 0
        wood_surface = 0

# charges for surface area
if area < 350:
    surface_charge = -75.99 + wood_surface
elif area > 750 and area <= 1000:
    surface_charge = 50 + wood_surface
elif area > 1000:
    surface_charge = 250 + wood_surface
else:
    surface_charge = wood_surface


# drawer charges
if drawers < 5:
    drawer_charge = (30 * drawers)
else:
    drawer_charge = 120 + 45 * (drawers - 4)

# total calculation
total = base_desk + wood_charge + surface_charge + drawer_charge

# tax calc
tax = total * 0.07

# final cost
final = total + tax

print("                                  Carpenter Project\n")
print("Wood Type      |      Number of Drawers      |"
      "      Desk Width      |      Desk Length\n")
print(f'{format(wood, "8")}                    {format(drawers, "2")}'
      f'                         {format(width, "3")}'
      f'                     {format(length, "3")}\n\n')
print(f'Base Price:          ${format(base_desk,"3.0f")}\n')
print(f'Surface Area:        {format(area, "3")} in.\n')
print(f'Surface Area Cost:   ${format(surface_charge, "3.2f")}\n')
print(f'Wood Cost:           ${format(wood_charge, "3.2f")}\n')
print(f'Drawer Cost:         ${format(drawer_charge, "3.2f")}\n')
print(f'Tax (7%):            ${format(tax, "2.2f")}\n')
print(f'Total:               ${format(final, "3.2f")}')
