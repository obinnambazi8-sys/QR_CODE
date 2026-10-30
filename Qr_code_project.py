import qrcode
import cv2

def encode():
    name=input("Enter your name: ").strip()
    input1=input("Enter a text or URL: ").strip()
    filename= input("Enter your desired filename: ")
    if input1 == "":
        print("You have to enter a url or text. ")
    elif filename =="":
        print("You have to enter a filename")

    else:
        if not filename.endswith("png"):
            filename+=".png"

        img= qrcode.make(input1)
        img.save(filename)
      
        print(f"{name} your {img} has printted successfully")
        print(f"View your file: {filename}")

def decode():
    file=input("Enter filename to decode: ").strip()
    if file =="":
        print("You have to enter filename. ")
    else:
        if not file.lower().endswith(".png"):
            print("Error,file must be a .png file ")
        else:
            read= cv2.imread(file)
            if read is None:
                print("image cannot be opened")
            else:   
                detector= cv2.QRCodeDetector()
                data,points,straight_qrcode = detector.detectAndDecode(read)
                if not data:
                    print("No qr code could be decoded.")
                else:
                    print(f"Data loaded sucessfully: {data}")
def Main_menu():
    while True:
        print("1: Enter 1 to create a qr code")
        print("2: Enter 2 to decode your qr code")
        userchoice=input("Enter an option from 1-3: ")
        if userchoice == "1":
            encode()
        elif userchoice == "2":
            decode()
        else:
            break
Main_menu()
            
   
