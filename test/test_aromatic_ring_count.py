from molstats import aromatic_ring_count

from pysmiles import read_smiles


def test_one_aromatic_ring():
    molecule = read_smiles('Cc1cc(O)ccc1O')
    assert aromatic_ring_count(molecule) == 1


def test_two_aromatic_ring():
    molecule = read_smiles('Cc1cc(-c2cccc(Cl)c2)ccc1O')
    assert aromatic_ring_count(molecule) == 2
