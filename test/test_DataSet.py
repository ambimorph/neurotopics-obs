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

    def test_word_string_to_index(self):
        ds = DataSet.DataSet(self.dataset,  self.img, self.word_counts_file_name)
        for i in range(len(ds.word_subset)):
            self.assertEqual(i, ds.word_string_to_index[ds.word_subset[i]], i)
       

if __name__ == '__main__':
    unittest.main()
