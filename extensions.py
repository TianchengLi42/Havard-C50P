def check(file_name):
    match file_name.split(".")[-1]:
        case"gif":
            return "image/gif"
        case"jpg"|"jpeg":
            return "image/jpeg"
        case"png":
            return "image/png"
        case"pdf":
            return "application/pdf"
        case"txt":
            return "text/plain"
        case"zip":
            return "application/zip"

print(check(input("What is the name of your file?")))