from copy import deepcopy

import networkx as nx
from pysmiles.smiles_helper import add_explicit_hydrogens, mark_aromatic_atoms


def add_hydrogens(molecule: nx.Graph) -> nx.Graph:
    molecule = deepcopy(molecule)
    add_explicit_hydrogens(molecule)
    return molecule


def add_aromatic_atoms(molecule: nx.Graph) -> nx.Graph:
    molecule = deepcopy(molecule)
    mark_aromatic_atoms(molecule)
    return molecule


def hydrogen_neighbor_count(molecule: nx.Graph, node_id: int) -> int:
    h_count = 0
    for neighbor_id in molecule.neighbors(node_id):
        if molecule.nodes[neighbor_id].get('element') == 'H':
            h_count += 1

    return h_count
