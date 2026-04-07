Fingerprinting of materials based on their electronic structure.

Python package to compute binary valued fingerprints of spectral quantities and evaluate their similarity.

This package implements the electronic density-of-states fingerprints and the similarity metrics introduced in Refs. [1,2]. 

As a similarity measure we use the Tanimoto coefficient [3].

This package is the continuation of https://github.com/kubanmar/dos-fingerprints.

# Usage

Fingerprints of, e.g., the electronic density-of-states (DOS), are instances of the `SpectralFingerprint()` class and can be calculated by providing, e.g., the energy in [eV] and the DOS in [states/unit cell/eV] to the `calculate()` method. Furthermore, the energy axis can be discretized over a non-uniform grid. For this, specific parameters must be provided. By default, the grid is specialized on the energy range between -10 and 5 eV, thereby emphasizing the upper valence region.

```Python
from spectral_fingerprints import SpectralFingerprint
dos_fingerprint = SpectralFingerprint().calculate(<dos_energies>,<dos_values>)
```

To evaluate the similarity, the function `tanimoto_similarity()` can be used:

```Python
from spectral_fingerprints import tanimoto_similarity
tc = tanimoto_similarity(dos_fingerprint_1, dos_fingerprint_2)
```

Additionally, the `SpectralFingerprint()` functions `get_similarty` and `get_similarities` can be used:

```Python
similarity = dos_fingerprint_1.get_similarity(dos_fingerprint_2)
similarities = dos_fingerprint_1.get_similarity([dos_fingerprint_1, dos_fingerprint_2])
```


# Citation

If you use this package in a publication, please cite it in the following way:

Martin Kuban, Santiago Rigamonti, Markus Scheidgen, and Claudia Draxl:
_Density-of-states similarity descriptor for unsupervised learning from materials data_
Sci Data *9*, 646 (2022). https://doi.org/10.1038/s41597-022-01754-z

# References

[1] Martin Kuban, Santiago Rigamonti, Markus Scheidgen, and Claudia Draxl:
_Density-of-states similarity descriptor for unsupervised learning from materials data_.
_Sci Data_ *9*, 646 (2022). https://doi.org/10.1038/s41597-022-01754-z

[2] Martin Kuban, Šimon Gabaj, Wahib Aggoune, Cecilia Vona, Santiago Rigamonti, Claudia Draxl:
_Similarity of materials and data-quality assessment by fingerprinting_.
_MRS Bulletin_ *47*, 991–999 (2022). https://doi.org/10.1557/s43577-022-00339-w

[3] P. Willet _et al._, _J. Chem. Inf. Comput._ *38* , 983 996 (1998) (https://doi.org/10.1021/ci9800211)