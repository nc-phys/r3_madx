import matplotlib.pyplot as plt

class R3Twiss:
    def twiss(self):
        """
        Perform Twiss calculations and plot the Twiss beta functions.
        """
        # Perform Twiss calculations
        twiss_data = self.madx.twiss(deltap='-0.005,0.0,0.005')

        # Plot the Twiss beta functions
        fig, ax = plt.subplots(1, 1, figsize=(12, 6))
        ax.plot(twiss_data['s'], twiss_data['betx'], label=r'$\beta_x$', color='black')
        ax.plot(twiss_data['s'], twiss_data['bety'], label=r'$\beta_y$', color='black', linestyle='--')
        ax.set_xlabel('Path length S [m]')
        ax.set_ylabel(r'Beta function $\beta_{x,y}$ [m.rad]')
        ax.legend()
        plt.savefig('data/twiss_plot.pdf')
        plt.close(fig)
