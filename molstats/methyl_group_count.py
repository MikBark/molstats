import networkx as nx

from molstats.helper import add_hydrogens, hydrogen_neighbor_count


def methyl_group_count(molecule: nx.Graph, safety: bool = True) -> int:
    """
    Parameters
    ----------
    molecule : networkx.Graph
        The networkx.Graph created using pysmiles from a molecule containing (or
        not containing) a methylene group (CH3).
    safety : bool (default=True)
        If the checkbox is set to True, the calculations do not affect the transferred
        object - molecule. If the check box is set to False, it is assumed that the
        transmitted graph contains hydrogen atoms supported by pysmiles. Disabling
        safety mode can increase the speed of operation, but lead to errors if the data
        is not properly prepared.

    Returns
    -------
    ch3_count : int
        The number of methyl group (CH3) in the molecule.
    """
    if safety:
        molecule = add_hydrogens(molecule)

    ch3_count = 0
    for node_id, element in molecule.nodes(data='element'):
        if element == 'C' and hydrogen_neighbor_count(molecule, node_id) == 3:
            ch3_count += 1

    return ch3_count
