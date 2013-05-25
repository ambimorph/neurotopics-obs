# Neurotopics/test/test_DataSet.py

import unittest, pickle

from code import DataSet

class TestDataSet(unittest.TestCase):

    def setUp(self):
        pickle_file_name = 'data/pickleddata.pkl'
        self.dataset = pickle.load(open(pickle_file_name, 'r'))
        self.img = 'allvoxel/atlas_labels_combined.img'
        self.word_counts_file_name = 'data/word_counts'

    def test_dataset_init(self):
       ds = DataSet.DataSet(self.dataset,  self.img, self.word_counts_file_name)
       

if __name__ == '__main__':
    unittest.main()
