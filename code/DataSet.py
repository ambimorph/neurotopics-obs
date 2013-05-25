# Neurotopics/code/DataSet.py

import neurosynth.analysis.reduce as nsar

class DataSet:

    """
    A DataSet takes a NeuroSynth dataset and extracts the DOI's, and
    word subset of interest.  It uses reduce.average_within_regions to
    get the average activation in the regions of interest (ROIs) of
    the img.
    """

    def __init__(self, neurosynth_dataset, img, word_counts_file):

        self.word_subset = neurosynth_dataset.get_feature_names()
        self.dois = list(neurosynth_dataset.feature_table.ids)
        self.average_activation = nsar.average_within_regions(neurosynth_dataset, img)
        self.get_word_subset_counts(self.word_subset, word_counts_file)

    def get_word_subset_counts(self, word_subset, word_counts_file):
        pass

    


        
