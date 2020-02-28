'''
    -To INSTALL packages:
        '$ pip3 install package'
    The package will be installed alongside its DEPENDENCIES

    -To REMOVE packages:
        '$ pip3 uninstall package'
    ONLY the package will be removed, NOT its dependencies.

    -To see all the dependencies installed:
        '$ pip3 list'
    
    -To see more detail about a package:
        '$ pip3 show package'

    -Other way of calling pip:
        '$ python3.7 -m pip3 install package'

    Note: install packages on virtual environments
'''

import requests

if __name__ == "__main__":
    '''
    If this code is run without installing 'requests'
    it'll cause an 
        ModuleNotFoundError
    '''
    response = requests.get(
        "https://api.exchangeratesapi.io/latest?symbols=USD"
    )
    print(response.text)
    