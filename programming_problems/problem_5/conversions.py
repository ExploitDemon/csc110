def kg_to_lbs():
    kilos = input("How many Kilos?: :")
    if kilos != "":
        kilos_to_lbs_conversion = round((float(kilos) * 2.205), 2)
        return kilos_to_lbs_conversion
    else:
        print("Invalid int, rerun program!!")
        breakpoint()


def liters_to_gallons():
    liters = input("How many liters?: ")
    if liters is not None:
        liters_to_gallons_conversion = round((float(liters) / 3.785), 2)
        return liters_to_gallons_conversion
    else:
        print("Invalid int, rerun program!!")
        breakpoint()
