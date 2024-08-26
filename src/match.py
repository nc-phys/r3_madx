class R3Match:
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
