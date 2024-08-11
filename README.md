# DA5401 Assignment #1: Data Acquisition, Transformation and Visualization

## Overview

This project is part of the DA5401 Data Analytics Laboratory course at IIT Madras.This project is a hands-on exploration of the data science pipeline, transforming a hand-drawn sketch into a digital dataset, applying matrix operations, and visualizing the results. The assignment encompasses data acquisition, cleansing, transformation, and visualization without relying on advanced image processing libraries.

## Objectives


Data Acquisition: Convert a hand-drawn sketch into a set of X-Y coordinates.
  
Data Cleansing & Loading: Process and structure the data for analysis.

Transformation: Apply matrix operations to rotate and flip the image.

Visualization: Generate scatter plots to visualize the transformed images.

## Process Summary


1. Sketch Creation:                                                                                                                                                       
                                                                                                                                                                          
- Drew a favorite object on paper and captured a square-format photograph.

2. Data Conversion:

- Utilized StarryData to transform the image into X-Y coordinate data.
- Defined fiducial points to set the axes and specified the range for X and Y.
     
3. Data Processing:

- Imported the CSV data into a pandas DataFrame.
- Performed data cleansing to ensure validity.
- Discretized the data into a 1000x1000 boolean matrix using NumPy for enhanced image clarity.
  
4. Matrix Operations:

- Rotation: Rotated the matrix by 90 degrees clockwise.
- Flipping: Flipped the matrix horizontally.
- Converted the resulting matrices back into X-Y coordinates.
  
5. Visualization:

- Created scatter plots of the original, rotated, and flipped images using Matplotlib.
- Ensured high-resolution visualizations by adjusting the matrix size.

  
## Learning Outcomes


- Gained proficiency in transforming physical drawings into digital datasets.
- Enhanced skills in data cleansing and structuring using pandas and NumPy.
- Applied matrix algebra to perform image transformations.
- Developed visualizations to represent data transformations effectively.

  
## How to Use This Repository


1. Prerequisites:

- Python 3.x
- Libraries: pandas, numpy, matplotlib

2. Running the Code:

- Clone the repository.
- Ensure all prerequisites are installed.
- Execute the Jupyter Notebook or Python scripts provided to replicate the process.

3. Customization:

- Replace the sample sketch image with your own to experiment with different drawings.
- Adjust the matrix size in the discretization step for varying image resolutions.

  
## Repository Contents


- data/: Contains the original CSV data extracted from the sketch.
- notebooks/: Jupyter Notebooks detailing each step of the process.
- images/: Visualizations of the original, rotated, and flipped sketches.
- scripts/: Python scripts used for data processing and visualization.


## Acknowledgments
- StarryData: For providing the tool to convert images into datasets.

## Conclusion
This project provided practical experience in data acquisition, matrix algebra, and data visualization, enhancing my understanding of these key concepts in data science.

