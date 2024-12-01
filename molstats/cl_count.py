import networkx as nx


def cl_count(molecule: nx.Graph) -> int:
    """
    Parameters
    ----------
    molecule : networkx.Graph
        The networkx object.Graph created using pysmiles from a molecule containing (or
        not containing) an Cl element.

    Returns
    -------
    cl_count : int
        The number of Cl elements in the molecule.
    """
    return sum(
        element == 'Cl' for _, element in molecule.nodes(data='element')
    )
