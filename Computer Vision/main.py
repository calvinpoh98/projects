import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the floor plan image
floor_plan = cv2.imread('Test Images/test.png')

# Convert the image to grayscale
gray = cv2.cvtColor(floor_plan, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Noise removal using Morphological Closing operation
kernel = np.ones((3,3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

# Sure background area using Dilation
sure_bg = cv2.dilate(closing, kernel, iterations=3)

# Finding sure foreground area using the distance transform and thresholding
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labelling
_, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

# Apply the Watershed algorithm
cv2.watershed(floor_plan, markers)

# Coloring the segmented areas
floor_plan[markers == -1] = [255,0,0]  # Boundary markers in red
segmented = np.zeros_like(floor_plan)

for label in np.unique(markers):
    if label == 0:
        continue
    # Color each segment
    segmented[markers == label] = np.random.randint(0, 255, size=3)

# Convert colors to make them distinguishable
segmented = cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB)

# Show the result
plt.figure(figsize=(15, 15))
plt.imshow(segmented)
plt.axis('off')
plt.show()