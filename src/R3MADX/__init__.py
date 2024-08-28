import functools
from .survey import R3Survey
from .tlapprox import R3TLApprox
from .match import R3Match
from .twiss import R3Twiss

def alt_madx_wrap(fn):
    @functools.wraps(fn)
    def wrapper(self, *args, madx=None, **kwargs):
        if madx is not None:
            original_madx = self.madx
            try:
                self.madx = madx
                return fn(self, *args, **kwargs)
            finally:
                self.madx = original_madx
        else:
            return fn(self, *args, **kwargs)
    return wrapper

def alt_madx_cls(cls):
    for parent in cls.__mro__:
        for name, method in parent.__dict__.items():
            if not callable(method):
                continue
            if name.startswith('_'):
                continue
            setattr(cls, name, alt_madx_wrap(method))
    return cls

@alt_madx_cls
class R3MADX(
    R3Survey,
    R3TLApprox,
    R3Match,
    R3Twiss
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

        # Perform a geometric survey the configuration & plot it
        self.survey()
