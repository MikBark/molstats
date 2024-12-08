from pysmiles import read_smiles

from smilestats import aromatic_ring_count, graph_aromatic_ring_count


def test_one_aromatic_ring():
    molecule = 'Cc1cc(O)ccc1O'
    assert aromatic_ring_count(molecule) == 1
    assert graph_aromatic_ring_count(read_smiles(molecule)) == 1


def test_two_aromatic_ring():
    molecule = 'Cc1cc(-c2cccc(Cl)c2)ccc1O'
    assert aromatic_ring_count(molecule) == 2
    assert graph_aromatic_ring_count(read_smiles(molecule)) == 2
