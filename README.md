This repository is dedicated to the projects developed during the Dabotics internship, 
showcasing a spectrum of solutions and hands-on experiences in the field of software engineering and technology. 

<h2>Projects Overview:</h2>

<h4>1. Task 001: Python Alarm Clock with Tkinter and Pygame</h4>
A user-friendly alarm clock application combining Tkinter for the graphical interface and Pygame for immersive alarm sounds.
This is the first task in the Dabotics repository, focusing on creating a Python alarm clock. The application utilizes Tkinter for the graphical user interface and Pygame for playing alarm sounds.
Users can easily set alarms, receive notifications at the specified times, and dismiss alarms when needed.

<h3>Features:</h3>

User-friendly GUI with Tkinter.
Integration of Pygame for alarm sounds.
Set and dismiss alarms seamlessly.


<h3>Instructions:</h3>

- Clone the repository to your local machine.
- Install the required dependencies (tkinter and pygame).
- Run the alarm_clock.py script to launch the application.
- Set alarms, receive notifications, and dismiss alarms as needed.


<h3>Dependencies:</h3>

- Tkinter: <code>pip install tk</code>
- Pygame: <code>pip install pygame</code>
- Feel free to contribute, report issues, or suggest improvements related to this specific task!

<h4>2. Task 002: OTP Email Script</h4>
This Python script generates a 6-digit OTP (One-Time Password), sends it to the user's email address, and verifies the entered OTP using MailHog as a mail testing tool.

<h3>Prerequisites</h3>
Before running the script, make sure you have the following installed:
<ul>
  <li>Python (Download from [Python Official Website](https://www.python.org/downloads/))</li>
  <li>Go (for installing MailHog, Download from [Go Official Website](https://golang.org/dl/))</li>
  <li>MailHog (Install using `go get github.com/mailhog/MailHog`)</li>
</ul>

<h3>How to Run</h3>
1. Start Mailhog
2. run <code>python otp_email.py</code>
3. Enter Email Address
3. Check MailHog Web UI:
Open your web browser and go to http://localhost:8025 to view the sent email containing the OTP.
4.Enter OTP:
Enter the OTP received in your email when prompted.
5.Verify OTP:
The script will verify the entered OTP.

<h3>Configuration</h3>
<p>Update the sender_email variable in the script with your email address.</p>
<p>Ensure "Less secure app access" is enabled in your Google account settings if using Gmail for sending emails.</p>

<h4>Note</h4>
<li>This script assumes MailHog is running locally on the default ports (1025 for SMTP and 8025 for the web UI).</li>
<li>Adjust SMTP settings in the script if MailHog is running on a different setup.</li>





3.(Future Project)
