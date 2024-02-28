# VisioAuthenticator
"VisioAuthenticator: A Python facial recognition-based authentication system using OpenCV and Tkinter. Seamlessly captures and organizes webcam selfies for successful and unsuccessful logins. Ideal for secure and user-friendly applications. GitHub repository for easy deployment and collaboration."
Algorithm for VisioAuthenticator Without Class:
Step-1: Import Libraries

Import necessary libraries (os, cv2, Tk, messagebox, datetime).
Step-2: Create Images Folder Method (create_images_folder)

Check if the specified folder exists, if not, create it.
Step-3: Capture Image Method (capture_image)

Open the default camera using cv2.VideoCapture(0).
Capture a frame, flip it horizontally, and display it.
Save the captured image in the specified user folder with a timestamped filename.
Release the camera and close the OpenCV window.
Step-4: Validate Login Method (validate_login)

Get the entered username and password.
Open the default camera, capture a frame, flip it, and display it.
Determine the user folder based on login success or failure.
Create the user folder if it doesn't exist.
Save the captured image in the user folder with a timestamped filename.
Release the camera, close the OpenCV window.
If login is successful, close the login window. If not, display an error message and close the login window.
Step-5: Create Login Window Method (create_login_window)

Set up the Tkinter window titled "Login Page" with specific attributes (geometry, background color).
Place labels, entry widgets, and the login button in the window.
Step-6: Main Function (main)

Create the "images" folder using create_images_folder.
Set up the login window using create_login_window.
Start the Tkinter main loop (mainloop).
Step-7: Main Section (`main)*

Call the main function to start the application.
This structured representation includes sub-titles for each step to provide a clear understanding of the algorithm's flow and functionality.
