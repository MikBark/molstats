from pysmiles import read_smiles

from molstats import methylene_group_count


def test_zero_methylene_group_count():
    molecule = read_smiles('Cc1cc(O)ccc1O')
    assert methylene_group_count(molecule) == 0


def test_one_methylene_group_count():
    molecule = read_smiles('Oc1cccc(Cc2ccccc2)c1')
    assert methylene_group_count(molecule) == 1

def test_two_methylene_group_count():
    molecule = read_smiles('Oc1cccc(CCc2cc(O)cc(O)c2)c1')
    assert methylene_group_count(molecule) == 2
