import numpy as np

class R3Mutate:
    def match(self):
        """
        Match the optics of the accelerator to the desired parameters.
        """
        # Perform optics matching
        self.madx.command.match(sequence='full_ring')
        self.madx.command.constraint(mux=1.216)
        self.madx.command.vary(NAME='dp_trim->k2', step=0.001, lower=-1.0, upper=1.0)
        self.madx.command.simplex(calls=100000, tolerance=1.0e-12)
        self.madx.command.endmatch()

    def tlapprox(self):
        """
        Apply a thin lens approximation as well as increase the resolution of the output data through the addition of extra monitors.
        """
        # Pre-flatten sequence
        self.madx.command.seqedit(sequence='full_ring')
        self.madx.command.flatten()
        self.madx.command.endedit()

        # Apply approximation
        self.madx.command.select(
            flag='makethin',
            class_='dipole',
            slice_=8,
            thick = True,
        )
        self.madx.command.makethin(sequence='full_ring')

        # Add monitors for increased resolution
        self.madx.command.seqedit(sequence='full_ring')
        for s in np.linspace(start=0, stop=self.survey_data[2][-1], num=1000):
            self.madx.command.install(element='Marker', at=s)
        self.madx.command.flatten()
        self.madx.command.endedit()

        # Select the modified sequence
        self.madx.use(sequence='full_ring')
