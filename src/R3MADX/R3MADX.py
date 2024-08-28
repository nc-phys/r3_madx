from ._alt_madx import alt_madx_cls
from .R3Mutate import R3Mutate
from .R3Review import R3Review
from .R3Run import R3Run

@alt_madx_cls
class R3MADX(
    R3Mutate,
    R3Review,
    R3Run,
):
    """
    Child umbrella class that uses multiple inheritance to combine all parent classes.
    """
    def __init__(self, madx=None):
        """
        Initialize the MAD-X instance.
        """
        self.madx = madx
        if self.madx is not None:
            self._config()
        else:
            print("No Madx() instance provided to R3MADX(); bypassing config.")

    def _config(self):
        """
        Configure MAD-X Instance.
        """
        from src.config import config

        # Set number of turns and load sequence
        self.madx.input(f'n_turns = {config.N_TURNS}')
        self.madx.call(file=f"{config.SEQUENCE_FILE}")

        # Configure the beam using the provided configuration
        self.madx.command.beam(**config.BEAM_CONFIG)

        # Select the sequence
        self.madx.use(sequence='full_ring')

        # Perform a geometric survey the configuration
        self.survey()
