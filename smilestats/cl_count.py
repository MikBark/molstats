import networkx as nx
from pysmiles import read_smiles


def cl_count(molecule: str | nx.Graph) -> int:
    """
    Parameters
    ----------
    molecule : str | networkx.Graph
        The string with smiles is encoded by a molecule or a  networkx.Graph created
        using pysmiles from a molecule containing (or not containing) an Cl element.

    Returns
    -------
    cl_count : int
        The number of Cl elements in the molecule.
    """
    if isinstance(molecule, str):
        return graph_cl_count(read_smiles(molecule))

    return graph_cl_count(molecule)


def graph_cl_count(molecule: nx.Graph) -> int:
    """
    Parameters
    ----------
    molecule : networkx.Graph
        The networkx.Graph created using pysmiles from a molecule containing (or
        not containing) an Cl element.

    Returns
    -------
    cl_count : int
        The number of Cl elements in the molecule.
    """
    return sum(
        element == 'Cl' for _, element in molecule.nodes(data='element')
    )