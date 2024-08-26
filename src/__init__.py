import code
from cpymad.madx import Madx
import config

from .initialize import R3Config
from .survey import R3Survey
from .tl_approx import R3TLApprox
from .matching import R3Matching
from .twiss import R3Twiss

class R3MADX(
    R3Config,
    R3Survey,
    R3TLApprox,
    R3Matching,
    R3Twiss
):
    def __init__(self):
        """
        Initialize the MAD-X instance and set up the configuration.
        """
        self.madx = Madx()
        self.sequence_file = config.SEQUENCE_FILE
        self.beam_config = config.BEAM_CONFIG
        self.n_turns = config.N_TURNS
        self.circumference = 0

    def repl(self):
        """
        Drop into REPL for user custom commands after main macro.
        """
        code.interact(local=locals())
