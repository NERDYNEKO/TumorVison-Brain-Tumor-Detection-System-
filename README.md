## 🔬 Architecture & Methodology
This project utilizes Transfer Learning with the MobileNetV2 architecture. By using a model pre-trained on the ImageNet dataset, the system leverages existing knowledge of shapes and textures, which is then fine-tuned to identify the specific features of brain tumors.

## Why MobileNetV2?
Inverted Residuals: Efficiently passes information through the network.
Linear Bottlenecks: Prevents non-linearities from destroying too much information in low-dimensional spaces.
Depthwise Separable Convolutions: Dramatically reduces the number of parameters compared to standard CNNs.

## 📂 Dataset Structure
The model was trained on a dataset containing 7,023 MRI images. The data is organized into four classes:
## Glioma:
A type of tumor that occurs in the brain and spinal cord.
## Meningioma: 
A tumor that forms on the membranes that cover the brain.
## Pituitary:
Tumors that grow in the pituitary gland.
## No Tumor:
Healthy brain scans.
