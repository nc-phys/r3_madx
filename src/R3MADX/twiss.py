class R3Twiss:
    def twiss(self):
        """
        Perform Twiss calculations and plot the Twiss beta functions.
        """
        # Perform Twiss calculations
        self.twiss_data = self.madx.twiss(deltap='-0.005,0.0,0.005')
        return self.twiss_data
