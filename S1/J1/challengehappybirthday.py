from datetime import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def draw_cake(candles_count):
    candles = "i" * candles_count
    cake = f"""
   ___{candles}___
   |:H:a:p:p:y:|
 __|___________|___
|^^^^^^^^^^^^^^^^^|
|:B:i:r:t:h:d:a:y:|
|                 |
~~~~~~~~~~~~~~~~~~~
"""
    print(cake)

def main():
    birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    candles = age % 10

    if is_leap_year(birthdate.year):
        draw_cake(candles)
        draw_cake(candles)
    else:
        draw_cake(candles)

if __name__ == "__main__":
    main()
