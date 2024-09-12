class Planet:
    # The three variables below are exaples of class variables
    speed_light = 299792458
    planck_constant = 6.63e-34

    '''
    This is the initialization of a standard method using the __init__ 
    constructor with the attributes ocean, sea, continent and country
    '''
    def __init__(self, name, ocean, sea, continent, country):
        self.name = name
        self.ocean =  ocean
        self.sea = sea
        self.continent = continent
        self.country = country

p4 = Planet('Mars', 0, 0, 100, 0)
p3 = Planet('Earth', 5, 50, 7, 195)

print(f'{p4.name} has {p4.ocean} number of oceans but the speed of light is {p4.speed_light} m/s2')
print(f'{p3.name} has {p3.ocean} number of oceans but the speed of light is {p3.speed_light} m/s2')