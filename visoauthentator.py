import os
import cv2
from tkinter import *
from tkinter import messagebox
from datetime import datetime

def create_images_folder(folder_name):
    # Create the specified folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def capture_image(user_folder):
    # Open the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    # Read a frame from the camera
    ret, frame = cap.read()

    # Flip the frame horizontally for a selfie effect
    frame = cv2.flip(frame, 1)

    # Display the frame
    cv2.imshow("Selfie Camera", frame)

    # Capture and save the image
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_filename = os.path.join(user_folder, f"selfie_{timestamp}.png")
    cv2.imwrite(image_filename, frame)
    print(f"Selfie captured and saved as '{image_filename}'")

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

def validate_login(username_entry, password_entry, login_window):
    # Check if the entered username and password are correct
    username = username_entry.get()
    password = password_entry.get()

    # Check if the "images" folder exists, create if not
    create_images_folder("images")

    # Open the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    # Read a frame from the camera
    ret, frame = cap.read()

    # Flip the frame horizontally for a selfie effect
    frame = cv2.flip(frame, 1)

    # Display the frame
    cv2.imshow("Selfie Camera", frame)

    # Automatically capture an image without waiting for user input
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if username == "Sufiyan" and password == "Stylosuf":
        user_folder = os.path.join("images", "successful")
    else:
        user_folder = os.path.join("images", "unsuccessful")

    create_images_folder(user_folder)

    image_filename = os.path.join(user_folder, f"selfie_{timestamp}.png")
    cv2.imwrite(image_filename, frame)
    print(f"Selfie captured and saved as '{image_filename}'")

    # Release the camera
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

    # Check if the entered username and password are correct
    if username == "Sufiyan" and password == "Stylosuf":
        login_window.destroy()  # Close the login window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        login_window.destroy()  # Close the login window

def main():
    # Create the "images" folder
    create_images_folder("images")

    # Create the login window
    login_window = Tk()
    login_window.title("Login Page")
    login_window.geometry("500x580+400+20")
    login_window.config(bg="black")
    Label(login_window, text="Sufiyan welcomes you", bg="black", fg="white", font=("Times new roman", 20, "italic")).place(x=100, y=80)

    # Create and place the username label and entry
    Label(login_window, text="Username:", fg="white", bg="black", font=("Times new roman", 16, "italic")).place(x=50, y=220)
    username_entry = Entry(login_window, font=("TImes new roman", 16, "italic"))
    username_entry.place(x=200, y=220)

    # Create and place the password label and entry (set show="*" to hide the password)
    Label(login_window, text="Password:", fg="white", bg="black", font=("Times new roman", 16, "italic")).place(x=50, y=280)
    password_entry = Entry(login_window, show="*", font=("Times new roman", 16, "italic"))
    password_entry.place(x=200, y=280)

    # Create and place the login button
    login_button = Button(login_window, fg="white", bg="black", activebackground="black", activeforeground="white", font=("Times new roman", 15, "italic"), text="Login", command=lambda: validate_login(username_entry, password_entry, login_window))
    login_button.place(x=200, y=360)

    # Start the Tkinter main loop
    login_window.mainloop()

if __name__ == "__main__":
    main()
