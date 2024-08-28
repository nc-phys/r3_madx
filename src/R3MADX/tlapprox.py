import numpy as np

class R3TLApprox:
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
        for s in np.linspace(start=0, stop=self.circumference, num=1000):
            self.madx.command.install(element='Marker', at=s)
        self.madx.command.flatten()
        self.madx.command.endedit()

        # Select the modified sequence
        self.madx.use(sequence='full_ring')
