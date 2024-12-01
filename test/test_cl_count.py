from pysmiles import read_smiles

from smilestats import cl_count


def test_cl_count():
    molecule = read_smiles('Cc1cc(-c2cccc(Cl)c2)ccc1O')
    assert cl_count(molecule) == 1
