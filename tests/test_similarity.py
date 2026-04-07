import pytest

from spectral_fingerprints import tanimoto_similarity
from spectral_fingerprints.similarity import match_fingerprints
from spectral_fingerprints.fingerprint import SpectralFingerprint
from scipy.constants import electron_volt


def test_match_fingerprints():
    
    fp1 = SpectralFingerprint()
    fp2 = SpectralFingerprint()
    fp1.bins = fp1._compress_binary_fingerprint_string('00000000111111110000000011111111')
    fp2.bins = fp1._compress_binary_fingerprint_string('1111111100000000')
    grid_id = 'nonuniform:1:1:1:1:1:1:1:1:8'
    fp1.grid_id = grid_id
    fp2.grid_id = grid_id
    fp1.indices = [0,3]
    fp2.indices = [1,2]
    print(fp1.n_state_bins, fp2.n_state_bins)

    bits1, bits2 = match_fingerprints(fp1, fp2)

    assert len(bits1) == len(bits2) == 16, "Fingerprints do not match"

def test_tanimoto_v2():
    # generate fp-type data and check if this can be realized with binary-strings only
    fp1 = SpectralFingerprint()
    fp2 = SpectralFingerprint()
    fp1.bins = fp1._compress_binary_fingerprint_string('00000000111111110000000011111111')
    fp2.bins = fp1._compress_binary_fingerprint_string('1111111100000000')
    grid_id = 'nonuniform:1:1:1:1:1:1:1:1:8'
    fp1.grid_id = grid_id
    fp2.grid_id = grid_id
    fp1.indices = [0,3]
    fp2.indices = [1,2]
    print(fp1.get_bitarray())
    print(fp2.get_bitarray())
    assert tanimoto_similarity(fp1, fp2) == 1, "Non-identical cut fingerprints"
    assert tanimoto_similarity(fp1, fp1) == 1, "Non-identity for Fingerprint v2 NR 1"
    assert tanimoto_similarity(fp2, fp2) == 1, "Non-identity for Fingerprint v2 NR 1"

@pytest.mark.skip()
def test_matching_of_spectra():
    test_data = dict()
    data = test_data["17661:2634879"]
    cut_energies = []
    cut_dos = []
    cut_energies = [e for e,d in zip(data['dos_energies'], data['dos_values'][0]) if (e / electron_volt > -7.3 and e / electron_volt < 2)]
    cut_dos = [d for e,d in zip(data['dos_energies'], data['dos_values'][0]) if (e / electron_volt > -7.3 and e / electron_volt < 2)]
    fp = SpectralFingerprint().calculate(data['dos_energies'], data['dos_values'], convert_data="enc")
    cut_fp = SpectralFingerprint().calculate(cut_energies, [cut_dos], convert_data="enc")
    assert tanimoto_similarity(cut_fp, fp) == tanimoto_similarity(fp, cut_fp)
    assert 1 - tanimoto_similarity(fp, cut_fp) < 1e-2  