"""import numpy
pip install scipy
import matplotlib.pyplot
python -m pip install scikit-learn matplotlib
from sklearn import linear_model
"""
# Start from a slim official Python image
FROM python:3.14

# Set the working directory inside the container
WORKDIR /app

# Install the three packages
RUN pip install --no-cache-dir numpy scipy scikit-learn sklearn

# Copy your script into the container
COPY numpy_learning.py .

# Run the script when the container starts
CMD ["python", "numpy_learning.py"]