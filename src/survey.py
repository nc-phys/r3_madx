import matplotlib.pyplot as plt
import numpy as np

class R3Survey:
    def survey(self):
        """
        Perform a geometric survey of the ring and plot the layout.
        """
        # Perform survey and save the data
        self.madx.survey(sequence='full_ring', file='data/r3_survey.out')

        # Load and process the survey data
        survey_data = np.transpose(np.genfromtxt('data/r3_survey.out', skip_header=8))

        # Plot the geometric layout
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.plot(survey_data[5], survey_data[7], color='black')
        ax.set_xlabel('x (m)')
        ax.set_ylabel('z (m)')
        plt.savefig('data/survey_plot.pdf')
        plt.close(fig)
