import neurosynth.analysis.reduce as nr
import nibabel
import pickle

pickle_file_name = 'data/pickleddata.pkl'
dataset = pickle.load(open(pickle_file_name, 'r'))

#this is a nifti file with different values for each ROI in the brain
atlas_file = 'allvoxel/atlas_labels_combined.img'
atlas_labels = 'allvoxel/names.txt'

res = nr.average_within_regions(dataset,atlas_file,threshold=0.01)
f = open(atlas_labels,'r')
names = f.readlines()
names = [x.strip('\n') for x in names]

#load the atlas file with nibabel (just for reference)
#img = nibabel.load(atlas_file)
#data = img.get_data()
