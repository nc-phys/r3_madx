import code
import matplotlib.pyplot as plt
from cpymad.madx import Madx
from src import R3MADX

if __name__ == "__main__":
    # Initialize MAD-X
    mad = Madx()
    # Load R3 config to MAD-X
    sim = R3MADX(mad)

    # Plot the geometric layout
    survey_data = sim.retrieve("survey_data")
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(survey_data[5], survey_data[7], color='black')
    ax.set_xlabel('x (m)')
    ax.set_ylabel('z (m)')
    plt.savefig('data/survey_plot.pdf')
    plt.close(fig)

    # Apply thin lens approximation and edit ring sequence to increase resolution
    sim.tlapprox()
    # Match the accelerator optics to desired parameters
    sim.match()
    # Perform Twiss calculations and plot the beta function
    #twiss_data = sim.twiss()
    # R3MADX methods can be called directly without the need for class loading
    twiss_data = R3MADX().twiss(madx=mad)

    # Plot the Twiss beta functions
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.plot(twiss_data['s'], twiss_data['betx'], label=r'$\beta_x$', color='black')
    ax.plot(twiss_data['s'], twiss_data['bety'], label=r'$\beta_y$', color='black', linestyle='--')
    ax.set_xlabel('Path length S [m]')
    ax.set_ylabel(r'Beta function $\beta_{x,y}$ [m.rad]')
    ax.legend()
    plt.savefig('data/twiss_plot.pdf')
    plt.close(fig)

    # Drop into REPL for custom user commands
    code.interact(local=locals())
