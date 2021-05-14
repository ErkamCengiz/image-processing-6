import cv2
# aynı resmin farklı çözünürlüklerinde felan çalışırken kullanıyoruz
resim = cv2.imread('messi.jpg')
up=cv2.pyrUp(resim)#görüntü büyüyor piksel artıyor
down=cv2.pyrDown(resim)#küçültüyor piksel azalıyor


cv2.imshow('orjinal',resim)
cv2.imshow('up',up)
cv2.imshow('down',down)










cv2.waitKey(0)
cv2.destroyAllWindows()