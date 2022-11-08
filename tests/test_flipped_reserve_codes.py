''' 
test usage of the flipped reserve codes with 
petl
'''

import yaml
import petl as etl
from pathlib import Path

def test_flipped_reserve_codes():
    path = './encodings/flipped_reserve_codes.yaml'
    with open(path,'r') as f:
        t = yaml.safe_load(f)['stata']

    cols = [['-9', 'Missing', '-11'], ['Confidential', '-11', 'Refused to answer']]
    source = etl.fromcolumns(cols)
    target = source.convertall(t)

    assert target.tol()==(['f0', 'f1'], ['.d', '.e'], ['.e', '.e'], ['.e', '.b'])


if __name__=='__main__':
    test_flipped_reserve_codes()