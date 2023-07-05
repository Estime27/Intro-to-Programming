#This function returns the wind chill in Farenheit
def windchill(T,V):
    wind_chill = 35.74 + float(0.6215*T) - float(35.75*(V**0.16)) + float(0.4275*(T)*(V**0.16))
    return wind_chill

#This converts celcius to farenheit, while returning the farenheit value
def temperature_conversion(celcius_temperature):
    fahrenheit = (float(celcius_temperature * (9/5)) + 32)
    return fahrenheit

temperature_value = input('What is the temperature? ')
temperature_type = input('Fahrenheit or Celsius (F/C)? ')

temperature_value_new = int(temperature_value)
temperature_type_upper = temperature_type.upper()

if temperature_type_upper == 'C':
    T = temperature_conversion(temperature_value_new)

    for V in range(5, 65, 5):
        print(f'At temperature {T}F, and wind speed {V} mph, the windchill is: {windchill(T,V):.2f}F')

elif temperature_type_upper == 'F':
   T = temperature_value_new

   for V in range(5, 65, 5):
        print(f'At temperature {T}F, and wind speed {V} mph, the windchill is: {windchill(T,V):.2f}F')


