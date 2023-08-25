import cv2

img = cv2.imread("galaxy.jpg", 1)


print(type(img))
print(img) 
print(img.shape) # resolution
print(img.ndim) # dimension

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))) # resize image 


cv2.imshow("Galaxy", resized_image)
# cv2.waitKey(0) # close with pressing any buttons
cv2.imwrite("Galaxy_resized.png", resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows() # close window