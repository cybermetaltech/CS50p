# extensions

# prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends (case-insensitively)
# in any of these suffixes: .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# if no suffix: output application/octet-stream instead, which is a common default.

# get the user input
user = input("File name: ").lower().strip()

# get the extension
ext = user.split(".")
ext = ext[-1]

# if tree
if ext == "gif":
    print("image/gif")
elif ext == "jpg":
    print("image/jpeg")
elif ext == "jpeg":
    print("image/jpeg")
elif ext == "png":
    print("image/png")
elif ext == "pdf":
    print("application/pdf")
elif ext == "txt":
    print("text/plain")
elif ext == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
