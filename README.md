# Teachable Character Classifier

This project uses a TensorFlow image classification model trained with [Teachable Machine by Google](https://teachablemachine.withgoogle.com/) to classify images of two characters from Game of Thrones: **Daenerys Targaryen** and **Jon Snow**.

##  Project Overview

- **Model Format**: TensorFlow SavedModel
- **Classes**: Daenerys, Jon Snow
- **Test Images**: Provided inside `test_images/`
- **Language**: Python 3.10
- **Libraries Used**: TensorFlow, OpenCV

##  Project Structure

```
teachable-character-classifier/
├── model/
│   ├── saved_model.pb
│   ├── assets/
│   └── variables/
│       ├── variables.index
│       └── variables.data-00000-of-00001
├── test_images/
│   ├── khaleesi1.jpg
│   └── jonsnow1.jpg
├── main.py
├── labels.txt
├── output.png           # Screenshot of terminal output (add this file)
└── README.md            # This file
```

##  How to Run

1. Create a virtual environment using Anaconda (recommended):

   ```
   conda create -n teachable-machine python=3.10
   conda activate teachable-machine
   ```

2. Install the required packages:

   ```
   pip install tensorflow==2.12.1
   pip install opencv-python
   ```

3. Run the script:

   ```
   python main.py
   ```

##  Sample Output

Make sure you have a screenshot of the terminal output like the one below, showing predicted results:

![Output](output.png)

##  Submission Checklist

- [x] Python script: `main.py`
- [x] Exported model in TensorFlow format: `model/`
- [x] Test images: `test_images/`
- [x] Screenshot of output: `output.png`
- [x] README file with instructions
