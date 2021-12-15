from simple_image_download import simple_image_download as simp #some packages and stuffs

response = simp.simple_image_download

lst = ["Google"] #Here in between the quotes type the 'image topic' you want to recieve from google images

for rep in lst:
 response().download(rep, 300)
