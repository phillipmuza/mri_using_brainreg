# Author: @Phillip Muza
# Date: 03/10/2024
# Title: Convert .nii files to .tif files 

import os
import nibabel as nib
import numpy as np
from tifffile import imsave

def nii_to_tif(nii_file, tif_file):
    """
    Convert a NIfTI (.nii) file to a multi-page TIFF (.tif) file,
    reshaping from sagittal to coronal orientation and rotating 90 degrees to the right.
    """
    # Load the NIfTI file
    nii_img = nib.load(nii_file)
    nii_data = nii_img.get_fdata()

    print(f"Original shape: {nii_data.shape}")

    # Reshape from sagittal to coronal
    # Assuming the current order is [sagittal, axial, coronal]
    # We want to change it to [coronal, axial, sagittal]
    nii_data = np.transpose(nii_data, (2, 0, 1))

    # Rotate each coronal slice 90 degrees to the right
    nii_data = np.rot90(nii_data, k=3, axes=(1, 2))

    print(f"Reshaped and rotated shape: {nii_data.shape}")

    # Save as multi-page TIFF
    imsave(tif_file, nii_data)
    print(f"Converted {nii_file} to {tif_file}")

directories_to_loop = [/directory1, directory2, directory3]

for directory in directories_to_loop:
    os.chdir(directory)
    for dirs in os.listdir():
        if os.path.isdir(dirs):
            os.chdir(dirs)
            if os.path.isfile('output_img.nii'):
                nii_to_tif('output_img.nii', 'output_img.tif')
            os.chdir('..')
