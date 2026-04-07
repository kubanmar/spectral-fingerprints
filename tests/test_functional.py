from spectral_fingerprints import SpectralFingerprint
import os
import json
import numpy as np
import pytest

@pytest.mark.skip()
def test_materials_similarity():

    with open(os.path.join(os.path.dirname(__file__), 'fingerprint_generation_test_data.json'), 'r') as test_data_file:
        test_data = json.load(test_data_file)


    fingerprints = test_data['fingerprints']
    similarity_matrix = test_data['simat']
    mids = [x[1] for x in fingerprints]
    raw_data = [test_data[mid] for mid in mids]
    new_fingerprints = [SpectralFingerprint().calculate(entry['dos_energies'], entry['dos_values'], convert_data="ENC") for entry in raw_data]
    matrix = []
    for fp in new_fingerprints:
        matrix.append(fp.get_similarities(new_fingerprints))
    assert np.allclose(similarity_matrix, matrix, atol = 1e-2)
