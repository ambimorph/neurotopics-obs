import neurosynth.analysis.reduce as nr
import nibabel
import pickle
import numpy

pickle_file_name = 'data/pickleddata.pkl'
dataset = pickle.load(open(pickle_file_name, 'r'))

#this is a nifti file with different values for each ROI in the brain
atlas_file = 'allvoxel/atlas_labels_combined.img'
atlas_file = 'allvoxel/rbrodmann.nii'
#atlas_file = 'allvoxel/ROI_MNI_V4.nii'
atlas_labels = 'allvoxel/names.txt'


res = nr.average_within_regions(dataset,atlas_file)
f = open(atlas_labels,'r')
names = f.readlines()
names = [x.strip('\n') for x in names]

#csv_file = open('data/roi_features.txt','w+')
#numpy.savetxt(csv_file,res,delimiter=' ',newline='\n')
#load the atlas file with nibabel (just for reference)
#img = nibabel.load(atlas_file)
#data = img.get_data()
