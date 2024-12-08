# smilestats

This is a small library that provides functions to calculate certain molecule features using the [SMILES](http://opensmiles.org/) encoding. The library uses the pysmiles package to read molecules encoded in SMILES as graphs.

# Installation

Requirements are Python 3.8 or higher version. To install the package from PyPI, run this command:

```bash
pip install smilestats
```

# Example

```python
from smilestats import aromatic_ring_count

print(aromatic_ring_count('Cc1cc(O)ccc1O'))
# 1 
```

See more in the `examples`.

# Functions 

### aromatic_ring_count ([src](https://github.com/MikBark/smilestats/blob/master/smilestats/aromatic_ring_count.py))

```
    Parameters
    ----------
    molecule : str | networkx.Graph
        The string with smiles is encoded by a molecule or a networkx.Graph created using
        pysmiles from a molecule that contains (or not contains) an aromatic ring.

    safety : bool (default=True)
        This parameter affects only if the molecule is not an instance of a string.
        If the parametr is set to True, the calculations do not affect the transferred
        object - molecule. If the check box is set to False, it is assumed that the
        transmitted graph contains marked aromatic atoms supported by pysmiles. Disabling
        safety mode can increase the speed of operation, but lead to errors if the data
        is not properly prepared.

    Returns
    -------
    aromatic_ring_count : int
        The number of aromatic rings in the molecule.
```

### hydroxy_group_count ([src](https://github.com/MikBark/smilestats/blob/master/smilestats/hydroxy_group_count.py))

```
    Parameters
    ----------
    molecule : str | networkx.Graph
        The string with smiles is encoded by a molecule or a networkx.Graph created using
        pysmiles from a molecule containing (or not containing) a hydroxy group (OH).

    safety : bool (default=True)
        This parameter affects only if the molecule is not an instance of a string.
        If the checkbox is set to True, the calculations do not affect the transferred
        object - molecule. If the check box is set to False, it is assumed that the
        transmitted graph contains hydrogen atoms supported by pysmiles. Disabling
        safety mode can increase the speed of operation, but lead to errors if the data
        is not properly prepared.

    Returns
    -------
    oh_count : int
        The number of hydroxy group (OH) in the molecule.
```


### methylene_group_count ([src](https://github.com/MikBark/smilestats/blob/master/smilestats/methylene_group_count.py))

```
    Parameters
    ----------
    molecule : str | networkx.Graph
        The string with smiles is encoded by a molecule or a networkx.Graph created using
        pysmiles from a molecule containing (or not containing) a methylene group (CH2).

    safety : bool (default=True)
        This parameter affects only if the molecule is not an instance of a string.
        If the checkbox is set to True, the calculations do not affect the transferred
        object - molecule. If the check box is set to False, it is assumed that the
        transmitted graph contains hydrogen atoms supported by pysmiles. Disabling
        safety mode can increase the speed of operation, but lead to errors if the data
        is not properly prepared.

    Returns
    -------
    ch2_count : int
        The number of methylene group (CH2) in the molecule.
```

### methyl_group_count ([src](https://github.com/MikBark/smilestats/blob/master/smilestats/methyl_group_count.py))

```
    Parameters
    ----------
    molecule : str | networkx.Graph
        The string with smiles is encoded by a molecule or a networkx.Graph created using
        pysmiles from a molecule containing (or not containing) a methylene group (CH3).

    safety : bool (default=True)
        This parameter affects only if the molecule is not an instance of a string.
        If the checkbox is set to True, the calculations do not affect the transferred
        object - molecule. If the check box is set to False, it is assumed that the
        transmitted graph contains hydrogen atoms supported by pysmiles. Disabling
        safety mode can increase the speed of operation, but lead to errors if the data
        is not properly prepared.

    Returns
    -------
    ch3_count : int
        The number of methyl group (CH3) in the molecule.
```

### cl_count ([src](https://github.com/MikBark/smilestats/blob/master/smilestats/cl_count.py))

```
    Parameters
    ----------
    molecule : str | networkx.Graph
        The string with smiles is encoded by a molecule or a  networkx.Graph created
        using pysmiles from a molecule containing (or not containing) an Cl element.

    Returns
    -------
    cl_count : int
        The number of Cl elements in the molecule.
```
