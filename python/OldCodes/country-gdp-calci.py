# Python gdp calculator
import time
print("==========================================================")
print("Welcome to GDP Calculator built with python 3.17 on OCT22")
print("==========================================================")

country = input("Enter name of the country - ")
initial = int(input("Enter current gdp of the country (in billion $s) - "))
inyear = int(input("Which year is it right now ? - "))
year = int(input("Upto which year you want to check ? - "))
rate = float(input("GDP Growth Rate ?? (%) - "))

print("==========================================================")
print(f"The country 🏳️{country} with initial gdp of 💵{initial}B$ on 📅{inyear} with growth rate of 📈{rate}% will be")
count = 1
gdp = initial
growth = 0
while inyear <= year:
    gdp = round(gdp, ndigits=4)
    growth = round(growth, ndigits=4)
    print(f"{count}. Year {inyear} || GDP = {gdp}B$ || Growth = {growth}B$ ")
    growth = rate/100*gdp
    gdp = gdp + growth
    inyear += 1
    count += 1
    time.sleep(0.1)

gdp = gdp - growth
print("==========================================================")
print(f"The country {country} will have estimated gdp of {gdp}B$ at year {year}")
