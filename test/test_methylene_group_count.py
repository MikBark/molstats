from pysmiles import read_smiles

from smilestats import graph_methylene_group_count, methylene_group_count


def test_zero_methylene_group_count():
    molecule = 'Cc1cc(O)ccc1O'
    assert methylene_group_count(molecule) == 0
    assert graph_methylene_group_count(read_smiles(molecule)) == 0


def test_one_methylene_group_count():
    molecule = 'Oc1cccc(Cc2ccccc2)c1'
    assert methylene_group_count(molecule) == 1
    assert graph_methylene_group_count(read_smiles(molecule)) == 1


def test_two_methylene_group_count():
    molecule = 'Oc1cccc(CCc2cc(O)cc(O)c2)c1'
    assert methylene_group_count(molecule) == 2
    assert graph_methylene_group_count(read_smiles(molecule)) == 2
