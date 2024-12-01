from pysmiles import read_smiles

from smilestats import methyl_group_count


def test_zero_methyl_group_count():
    molecule = read_smiles('Oc1ccc(Cl)cc1Cl')
    assert methyl_group_count(molecule) == 0


def test_one_methyl_group_count():
    molecule = read_smiles('Cc1cc(O)ccc1O')
    assert methyl_group_count(molecule) == 1


def test_two_methyl_group_count():
    molecule = read_smiles('Cc1ccc(O)c(C)c1')
    assert methyl_group_count(molecule) == 2
