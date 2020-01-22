import sys

sys.path.extend(['path1','path2'])

import split_farm

split_farm.__path__  
# >>> _NamespacePath(['path1/split_farm', 'path2/split_farm'])

import split_farm.bird
import split_farm.bovine

split_farm.bird.__path__
# >>> ['path2/split_farm/bird']

split_farm.bovine.__path__
# >>> ['path1/split_farm/bovine']
