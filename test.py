import cv2
img = cv2.imread('/content/drive/MyDrive/5.jpg')
target_img = cv2.imread('/content/drive/MyDrive/5.jpg')
rec_img = cv2.imread('/content/drive/MyDrive/5.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)

rev_img = cv2.bitwise_not(target_img)

for cnt in contours:
  appox = cv2.approxPolyDP(cnt, cv2.arcLength(cnt, True)*0.02, True)

  x, y, width, height = cv2.boundingRect(cnt)
  
  if (width > 180 and height > 180) and img.shape[1] != width:
    cv2.rectangle(rec_img, (x, y), (x+width, y+height), COLOR, 3)
    rev_img[y:y+height, x:x+width] = img[y:y+height, x:x+width]
  

cv2.imwrite("rev.png", rev_img)
cv2.imwrite("rec.png", rec_img)