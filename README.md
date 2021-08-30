# Edge Detection

This is a simple demo that illustrates four edge detection algorithms in OpenCV.

### Usage

This program was run under the following versions.

- `Python 3.9.5`
- `OpenCV 4.5.2`
- `Numpy 1.19.5`

The main program folder should contain `main.py` and `kitty.jpg`. Navigate to the folder in OS X from the command line and run `python main.py`. This should work in other operating systems.

The image in the upper left is the original image. In the upper right is the image with the selected edge detection algorithm applied. The algorithm can be chosen by clicking on the desired algorithm in the lower left. To adjust parameters (applicable only to the Canny and Sobel algorithms), click on the slider bar in the lower left.

### Canny Edge Detection

Canny edge detection is the most popular edge detection algorithm, and in this case it gives the crispest results. See the [OpenCV documentation](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html) for details on how it works.

A 5x5 Gaussian filter is applied first.

The slider can be used to vary the minimum and maximum thresholds for edge detection. These values indicate the sensitivity with which edges are detected, with more edges detected for smaller values.

### Sobel

See [this presentation](https://www.cs.auckland.ac.nz/compsci373s1c/PatricesLectures/Edge%20detection-Sobel_2up.pdf) for details on the Sobel filter for edge detection. We apply a 5x5 Gaussian filter first.

The upper slider indicates the Sobel kernel size, with possible values being 1, 3, 5, and 7.

### Prewitt

See this [code snippet](https://gist.github.com/rahit/c078cabc0a48f2570028bff397a9e154) for applying a Prewitt filter.

### Laplacian

See the [OpenCV documentation](https://docs.opencv.org/3.4/d5/db5/tutorial_laplace_operator.html) for information about the Laplacian filter.

### About the Image

The photograph is of Natsu, taken on April 24, 2021 when he was about eight weeks old. You can try this with other images as well.