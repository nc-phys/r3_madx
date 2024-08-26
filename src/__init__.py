import config
from .survey import R3Survey
from .tlapprox import R3TLApprox
from .match import R3Match
from .twiss import R3Twiss

class R3MADX(
    R3Survey,
    R3TLApprox,
    R3Match,
    R3Twiss
):
    """
    Child umbrella class that uses multiple inheritance to combine all parent classes.
    """
    def __init__(self, madx):
        """
        Initialize the MAD-X instance.
        """
        self.madx = madx
        self._config()

    def _config(self):
        """
        Configure MAD-X Instance.
        """
        self.sequence_file = config.SEQUENCE_FILE
        self.beam_config = config.BEAM_CONFIG
        self.n_turns = config.N_TURNS
        self.circumference = 0

        # Set number of turns and load sequence
        self.madx.input(f'n_turns = {self.n_turns}')
        self.madx.call(file=self.sequence_file)

        # Configure the beam using the provided configuration
        self.madx.command.beam(**self.beam_config)

        # Select the sequence
        self.madx.use(sequence='full_ring')
