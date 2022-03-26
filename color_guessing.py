colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Light Blue", "Light Green", "Black", "White", "Grey", "Brown", "Gold", "Silver"]

a=0
while a==0:
    a=int(input("Do you want to play the Color Guessing Game? Press 0 for yes, 1 for no: "))
    if a==1:
        print("Bye! Hope you can play again sometime!")
        break
    print("Red \nOrange \nYellow \nGreen \nBlue \nPurple \nPink \nLight Blue \nLight Green \nBlack \nWhite \nGrey \nBrown \nGold \nSilver")
    print("\nPick any one color and I will guess your color")
    print("\nRed \nPurple \nLight Blue \nWhite \nGrey \nBrown \nSilver" )
    r=int(0)
    x=int(input("If your color is in this list, press 1, otherwise press 0:"))
    if x==1:
        r=r+1
    print("\nOrange\nBlack\nWhite\nGrey\nGold\nSilver")
    x=int(input("If your color is in this list, press 1, otherwise press 0:"))
    if x==1:
        r=r+2
    print("\nYellow\nPink\nLight Blue\nBlack\nWhite\nBrown\nGold\nSilver")
    x=int(input("If your color is in this list, press 1, otherwise press 0:"))
    if x==1:
        r=r+3
    print("\nGreen\nPink\nLight Blue\nLight Green\nGrey\nBrown\nGold\nSilver")
    x=int(input("If your color is in this list, press 1, otherwise press 0:"))
    if x==1:
        r=r+4
    print("\nBlue\nPurple\nLight Green\nBlack\nWhite\nGrey\nBrown\nGold\nSilver")
    x=int(input("If your color is in this list, press 1, otherwise press 0:"))
    if x==1:
        r=r+5
    print("Your color is", colors[r-1])
    