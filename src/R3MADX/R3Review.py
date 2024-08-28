import numpy as np

class R3Review:
    def retrieve(self, var_name):
        """
        Retrieves the value of an instance variable by name.
        """
        if not hasattr(self, var_name):
            raise AttributeError(f"{var_name} doesn't exist in R3MADX instance")
        else:
            return getattr(self,var_name)

    def survey(self):
        """
        Perform a geometric survey of the ring and plot the layout.
        """
        # Perform survey and save the data
        self.madx.survey(sequence='full_ring', file='data/r3_survey.out')
        # Load and process the survey data
        self.survey_data = np.transpose(np.genfromtxt('data/r3_survey.out', skip_header=8))
        return self.survey_data
