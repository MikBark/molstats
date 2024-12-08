from pysmiles import read_smiles

from smilestats import graph_hydroxy_group_count, hydroxy_group_count


def test_one_hydroxy_group():
    molecule = 'Cc1cc(-c2cccc(Cl)c2)ccc1O'
    assert hydroxy_group_count(molecule) == 1
    assert graph_hydroxy_group_count(read_smiles(molecule)) == 1


def test_two_hydroxy_group():
    molecule = 'Cc1cc(O)ccc1O'
    assert hydroxy_group_count(molecule) == 2
    assert graph_hydroxy_group_count(read_smiles(molecule)) == 2
