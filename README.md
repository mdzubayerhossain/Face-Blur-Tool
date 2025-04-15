# Face Blur Tool

A Python tool for automatically detecting and blurring faces in dress model photographs using a natural-looking circular blur.

![Example of face blurring](![free-photo-of-eastern-dresses-2024-shoot-by-dhanno (1)](https://github.com/user-attachments/assets/4581120e-bcc1-46c0-a2d7-e86d202d9db2)
)

## 🔍 Overview

This tool was created to help fashion retailers and e-commerce businesses protect the privacy of their models while showcasing their clothing products. By automatically detecting and applying a circular blur to faces, the tool maintains the focus on the garments while anonymizing the individuals wearing them.

## 🚀 Features

- **Face Detection**: Automatically detects faces in images using OpenCV's Haar Cascade classifier
- **Natural Circular Blur**: Applies a smooth, circular blur rather than a jarring rectangular blur
- **Batch Processing**: Processes entire folders of images in a single run
- **Format Support**: Works with various image formats including JPG, JPEG, and PNG
- **Error Handling**: Includes robust error handling to ensure processing continuity

## 📋 Requirements

- Python 3.6+
- OpenCV
- NumPy

Install required packages:

```bash
pip install opencv-python numpy
```

## 💡 Use Cases

- **Fashion E-commerce**: Anonymize models in product photos before publishing them online
- **Catalog Production**: Create professional catalogs while protecting model identity
- **Social Media Content**: Share outfit ideas without revealing the identity of models
- **Educational Materials**: Use fashion images in educational contexts with privacy protection
- **Secondhand Marketplaces**: Allow individuals to sell clothing items without showing their faces

## 🔧 How It Works

The tool employs a sophisticated approach to face anonymization:

1. **Detection**: Uses Haar Cascade classifiers to locate faces in images
2. **Mask Creation**: Generates a circular mask centered on each detected face
3. **Smart Blurring**: Applies Gaussian blur only to the masked areas
4. **Seamless Blending**: Blends the blurred and original images for a natural transition

## 📁 Directory Structure

```
face-blur-tool/
├── face_blur.py         # Main script
├── Dress/               # Input folder containing original images
├── blur_image/          # Output folder for processed images
└── README.md            # Documentation
```

## 🚀 Usage

1. Place your dress model images in the `Dress` folder
2. Run the script:

```bash
python face_blur.py
```

3. Find your processed images in the `blur_image` folder

## ⚙️ Customization

You can adjust several parameters in the script:

- **Blur Intensity**: Modify the Gaussian blur parameters `(99, 99), 30` for stronger or softer blurring
- **Circle Size**: Change the radius multiplier (`radius * 1.2`) to cover more or less of the face area
- **Detection Sensitivity**: Adjust the `1.1, 4` parameters in `detectMultiScale` for different face detection sensitivity

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

If you have any questions or suggestions, please open an issue in this repository or contact [mdzubayerhossainpatowari@gmail.com](mailto:mdzubayerhossainpatowari@gmail.com).
