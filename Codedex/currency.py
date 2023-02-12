# Sumar todo el dinero que me ha sobrado de un viaje y pasarlo a USD


chinese_yuan = int(input("What do you have left in yuan? "))
japanese_yen = int(input("What do you have left in yen? "))
south_korean_won = int(input("What do you have left in south korean won? "))


chinese_yuan_USD = chinese_yuan*(0.15/1)
japanese_yen_USD = japanese_yen*(0.0076/1)
south_korean_won_USD = south_korean_won*(0.00079)


total_USD = chinese_yuan_USD + japanese_yen_USD + south_korean_won_USD

print("Te han quedado " + str(total_USD) + " dolares")