Setup for "retina retinopathy" Image Classification
---------------------------------------------------

Install Caffe (http://caffe.berkeleyvision.org/)

For computers with Nvidia GPUs:
Install CUDA 8.0

For Ubuntu Linux:
	With GPU: sudo apt install caffe-tools-gpu
	No GPU: sudo apt install caffe-tools-cpu
	
For Windows:
	Download prebuilt binaries from https://github.com/BVLC/caffe/tree/windows and extract
	Recommended: set PATH environment variable to "bin" directory of extracted Caffe path
	
For Mac (not recommended):
	See http://caffe.berkeleyvision.org/install_osx.html

Get training data file img_left_train.hdf5 from https://drive.google.com/drive/folders/1--_BJZX5bhxlUjGRPJ7ZioDO0oXHeHT2 and place in root of project

To start training:

	Linux with GPU:
		./train-gpu
		
	Linux without GPU:
		./train-cpu
	
	Windows with GPU:
		train-gpu.bat
		
	Windows without GPU:
		train-cpu.bat
		

Training Data
-------------

Original training data source: https://www.kaggle.com/c/diabetic-retinopathy-detection/data
Processed version of data can be download here: https://drive.google.com/open?id=1YzuUE0EM7u9i4gJpdHssrgx07paxGSI-