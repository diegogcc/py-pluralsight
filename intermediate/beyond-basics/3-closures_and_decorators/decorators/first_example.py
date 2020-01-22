def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap


def northen_city():
    return 'Tromsø'

@escape_unicode
def northen_city_unicode():
    return 'Tromsø'

if __name__ == '__main__':
    print(northen_city())  # Tromsø
    print(northen_city_unicode())  #'Troms\xf8'