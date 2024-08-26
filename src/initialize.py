class R3Config:
    def config(self):
        """
        Configure the simulation by setting the number of turns and loading the sequence.
        """
        # Set number of turns and load sequence
        self.madx.input(f'n_turns = {self.n_turns}')
        self.madx.call(file=self.sequence_file)

        # Configure the beam using the provided configuration
        self.madx.command.beam(**self.beam_config)

        # Select the sequence
        self.madx.use(sequence='full_ring')
