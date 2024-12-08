from pysmiles import read_smiles

from smilestats import cl_count, graph_cl_count


def test_cl_count():
    molecule = 'Cc1cc(-c2cccc(Cl)c2)ccc1O'
    assert cl_count(molecule) == 1
    assert graph_cl_count(read_smiles(molecule)) == 1
