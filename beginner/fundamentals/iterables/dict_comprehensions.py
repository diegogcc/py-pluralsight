from pprint import pprint as pp

country_to_capital = {'UK':'London',
                      'Brazil':'Brazilia',
                      'Colombia':'Bogota'}      # {'Brazil': 'Brazilia', 'Colombia': 'Bogota', 'UK': 'London'}

capital_to_country = {capital:country for country, capital in country_to_capital.items()}  # {'Bogota': 'Colombia', 'Brazilia': 'Brazil', 'London': 'UK'}