First_Number = int(input('First Number: '))
Second_Number = int(input('Second Number: '))
Third_Number = int(input('Third Number: '))
Fourth_Number = int(input('Fourth Number: '))
Fifth_Number = int(input('Fifth Number: '))

if First_Number - Second_Number >= 0:
    if First_Number - Third_Number >= 0:
        if First_Number - Fourth_Number >= 0:
            if First_Number - Fifth_Number >= 0:
                print('The Largest is the First Number', First_Number)
if Second_Number - First_Number >= 0:
    if Second_Number - Third_Number >= 0:
        if Second_Number - Fourth_Number >= 0:
            if Second_Number - Fifth_Number >= 0:
                print('The Largest is the Second Number', Second_Number)
if Third_Number - First_Number >= 0:
    if Third_Number - Second_Number >= 0:
        if Third_Number - Fourth_Number >= 0:
            if Third_Number - Fifth_Number >= 0:
                print('The Largest is the Third Number', Third_Number)
if Fourth_Number - First_Number >= 0:
    if Fourth_Number - Second_Number >= 0:
        if Fourth_Number - Third_Number >= 0:
            if Fourth_Number - Fifth_Number >= 0:
                print('The Largest is the Fourth Number', Fourth_Number)
if Fifth_Number - First_Number >= 0:
    if Fifth_Number - Second_Number >= 0:
        if Fifth_Number - Third_Number >= 0:
            if Fifth_Number - Fourth_Number >= 0:
                print('The Largest is the Fifth Number', Fifth_Number)
