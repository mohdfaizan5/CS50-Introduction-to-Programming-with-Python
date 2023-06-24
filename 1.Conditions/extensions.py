#Program which outputs the extintion of a file given
ex = input("File name: ").lower().strip()

if ex.endswith(".gif"):
    print("image/gif")
    
elif ex.endswith(".jpg") or ex.endswith(".jpeg"):
    print("image/jpeg")
    
elif ex.endswith(".pdf"):
    print("application/pdf")

elif ex.endswith(".png"):
    print("image/png")

elif ex.endswith(".txt"):
    print("text/plain")

elif ex.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
"""
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
"""