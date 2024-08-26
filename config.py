# Simulation settings
N_TURNS = 1

# Ring configuration
SEQUENCE_FILE = 'src/sequence.madx'
AMU = 931.49410242  # MeV
BEAM_ENERGY = 200.0  # MeV/u

# Beam configuration
BEAM_CONFIG = {
    "mass": 124 * AMU / 1000,  # in GeV
    "charge": 54.0,
    "energy": 124 * (AMU + BEAM_ENERGY) / 1000,  # in GeV
    "sigt": 4.4616,  # bunch length
    "sige": 0.001,  # relative energy spread
    "kbunch": 20,  # number of bunches
    "radiate": True,  # synchrotron radiation
    "bunched": True
}
