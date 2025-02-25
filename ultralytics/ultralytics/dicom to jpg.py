import os
import pydicom
import numpy as np
import matplotlib.pyplot as plt

def convert_dicom_to_jpg(input_path, output_path, dpi=300):
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.lower().endswith('.dcm'):
                dicom_path = os.path.join(root, file)
                output_filename = os.path.splitext(file)[0] + '.jpg'
                output_path_jpg = os.path.join(output_path, output_filename)

                ds = pydicom.read_file(dicom_path)
                image = np.stack([ds.pixel_array])
                image = image.squeeze()

                plt.imshow(image, cmap='gray')
                plt.axis('off')
                plt.savefig(output_path_jpg, dpi=dpi, bbox_inches='tight', pad_inches=0)
                plt.close()

if __name__ == "__main__":
    input_folder = r''  # Replace with your input folder
    output_folder = r''  # Replace with your output folder

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    convert_dicom_to_jpg(input_folder, output_folder, dpi=800)
