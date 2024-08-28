import numpy as np

class R3Survey:
    def survey(self):
        """
        Perform a geometric survey of the ring and plot the layout.
        """
        # Perform survey and save the data
        self.madx.survey(sequence='full_ring', file='data/r3_survey.out')

        # Load and process the survey data
        self.survey_data = np.transpose(np.genfromtxt('data/r3_survey.out', skip_header=8))

        # Save circumference of R3 for Resolution Improvement
        self.circumference = self.survey_data[2][-1]
