import code
from cpymad.madx import Madx
from src import R3MADX

if __name__ == "__main__":
    # Initialize MAD-X
    mad = Madx()
    # Load R3 config to MAD-X
    sim = R3MADX(mad)

    # Perform a geometric survey of the ring & plot it
    sim.survey()
    # Apply thin lens approximation and edit ring sequence to increase resolution
    sim.tlapprox()
    # Match the accelerator optics to desired parameters
    sim.match()
    # Perform Twiss calculations and plot the beta function
    #sim.twiss()
    # R3MADX methods can be called directly without the need for class loading
    R3MADX().twiss(madx=mad)

    # Drop into REPL for custom user commands
    code.interact(local=locals())
