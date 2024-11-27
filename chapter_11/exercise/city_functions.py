def city(city_name, country_name, population=0):
    ret = ''
    ret += city_name.title()
    ret += ', '
    ret += country_name.title()
    if population != 0:
        ret += ' - '
        ret += str(population)
    return ret

