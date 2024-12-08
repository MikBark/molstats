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
