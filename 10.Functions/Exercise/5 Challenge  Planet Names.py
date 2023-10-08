# 5 Challenge  Planet Names
# Find the planet name if the id of the planet is given
# 1-mercury, 2-venus, 3-earth, 4-mars, 5-jupiter, 6-saturn, 7-uranus, 8-neptune, 9-pluto

def planet_name():
    planets = {1: 'Mercury',
               2: 'Venus',
               3: 'Earth',
               4: 'Mars',
               5: 'Jupiter',
               6: 'Saturn',
               7: 'Uranus',
               8: 'Neptune',
               9: 'Pluto'}

    idval = int(input('Enter Id value: '))
    if 0 < idval < 10:
        planet = planets[idval]
        print(planet)
    else:
        print('Enter number between 1 and 9')


planet_name()	
