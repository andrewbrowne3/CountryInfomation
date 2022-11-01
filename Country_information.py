#pip install countryinfo
from countryinfo import CountryInfo
count=input("Enter your country: ")
country = CountryInfo(count)
print("Capital is: ", country.capital())
print("Currency are: ", country.currencies())
print("Lanuguage is: ", country.languages())
print("Borders are: ", country.borders())
print("Other names: ", country.alt_spellings())
