# Face Attendance System

## Quick Start Checklist (for New Users)

1. **Use Python 3.10 or 3.11** (do not use 3.13+; some dependencies may not work).
2. **Create and activate a virtual environment** before installing dependencies.
3. **Install all requirements** from `requirements.txt`.
4. **Run migrations** to set up the database.
5. **Create a Django superuser** (admin account).
6. **Start the server and log in to the admin panel**.
7. **Add at least one camera configuration** in the admin panel (required for the app to work).

---

## Project Overview

The Face Attendance System is a modern, AI-powered web application designed for educational institutions and organizations to automate and secure the process of student attendance. Leveraging advanced facial recognition technology, this system eliminates manual roll calls, reduces errors, and enhances security. It provides a seamless experience for both students and administrators, with real-time attendance tracking, email notifications, and a user-friendly dashboard.

### Key Features
- **Face Recognition Attendance:** Uses computer vision to identify and mark student attendance via webcam or IP camera.
- **Student Registration:** Students can register themselves by filling out a form and capturing their photo via webcam.
- **Admin Approval:** All registrations require admin approval for security and data integrity.
- **Multi-Camera Support:** Supports both local webcams and network/IP cameras for flexible deployment.
- **Attendance Management:** Tracks check-in and check-out times, and maintains detailed attendance records.
- **Email Notifications:** Sends confirmation emails to students upon registration and authorization using Gmail SMTP.
- **CSV Export:** Admins can export student and attendance data to CSV for reporting and analysis.
- **Role-Based Access:** Secure login for admins and students, with different permissions.
- **Modern UI:** Clean, responsive dashboard with real-time stats and easy navigation.

### Technology Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap/Tailwind), JavaScript
- **Database:** SQLite (default, can be upgraded to PostgreSQL/MySQL)
- **Face Recognition:** facenet-pytorch, OpenCV
- **Email:** Gmail SMTP (App Password)

### Workflow
1. **Student Registration:**
   - Student fills out a registration form and captures a photo.
   - Data is saved and awaits admin approval.
2. **Admin Approval:**
   - Admin reviews and authorizes student registrations.
   - Upon approval, the student receives an authorization email.
3. **Attendance Marking:**
   - Students check in/out using face recognition at the camera.
   - Attendance is automatically recorded with timestamps.
4. **Reporting:**
   - Admins can view, filter, and export attendance and student data.

### Benefits
- **Accuracy:** Reduces human error and prevents proxy attendance.
- **Efficiency:** Saves time for teachers and students.
- **Security:** Only authorized students can check in/out.
- **Transparency:** Real-time records and easy reporting.
- **Scalability:** Can be deployed in schools, colleges, offices, or events.

---

## Features
- Real-time face detection and recognition
- Multi-camera support (webcam and IP cameras)
- Student registration with webcam capture
- Admin approval and student authorization
- Automatic attendance tracking (check-in/check-out)
- Email notifications (registration and authorization)
- Admin dashboard for student and camera management
- Secure authentication and role-based access

## Prerequisites
- Python 3.10 or 3.11 (do not use 3.13+)
- pip
- (Optional) Virtual environment tool (venv, virtualenv)
- Webcam or IP camera (for face recognition)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Project-Face-attandence-system-version-1.0
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv venv
   # On Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   # On Windows (cmd):
   venv\Scripts\activate.bat
   # On Mac/Linux:
   source venv/bin/activate
   ```
   **If you see 'No module named django' or similar errors, make sure your virtual environment is activated!**

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```
   - Enter a username, email, and password when prompted. Save these credentials.

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   - Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

7. **Log in to the admin panel:**
   - Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Use the superuser credentials you created above.

8. **Add a Camera Configuration (REQUIRED):**
   - In the admin panel, find **Camera Configurations**.
   - Click **Add** and fill in:
     - **Name:** (e.g., Default Camera)
     - **Camera Source:** `0` for your default webcam, or the stream URL for an IP camera.
     - **Threshold:** (leave default or set as needed)
   - Save the configuration.
   - Without this, you will see an error: "No camera configurations found. Please configure them in the admin panel."

---

## Common Errors & Fixes

- **No module named 'django'**
  - Solution: Activate your virtual environment before running any Django commands.
- **No camera configurations found**
  - Solution: Log in to the admin panel and add a camera configuration as described above.
- **Migrations not applied / Internal Server Error**
  - Solution: Run `python manage.py migrate` after activating your virtual environment.
- **Wrong Python version / Dependency install errors**
  - Solution: Use Python 3.10 or 3.11. Do not use 3.13+.
- **Admin login not working**
  - Solution: Make sure you created a superuser with `python manage.py createsuperuser` and are using the correct credentials.

## Email Notifications Setup

This project uses Gmail SMTP to send registration and authorization emails to students.

1. Enable 2-Step Verification on your Gmail account.
2. Generate an App Password for "Mail" and "Other (Custom name)" in your Google Account.
3. In `Project101/settings.py`, set:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your_email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your_app_password'
   DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
   ```
4. Restart your Django server.

**Note:** Never commit your real Gmail or app password to public repositories.

## Usage
- **Student Registration:** Students register via the registration page (with webcam capture).
- **Admin Approval:** Admin reviews and authorizes students.
- **Attendance:** Mark attendance using face recognition (webcam or IP camera).
- **Email Notifications:** Students receive emails on registration and authorization.
- **Admin Dashboard:** Manage students, attendance, and cameras.

## Troubleshooting
- **Email not sent:**
  - Double-check Gmail and App Password in `settings.py`.
  - Make sure 2-Step Verification is enabled on your Gmail.
  - Check your spam/junk folder.
- **Face recognition issues:**
  - Ensure good lighting and camera quality.
  - Make sure student photos are clear and well-lit.
- **Database errors:**
  - Run migrations again: `python manage.py migrate`

## Contributing
- Fork the repository and create a feature branch.
- Submit a pull request with a clear description of your changes.
- For major changes, open an issue first to discuss what you'd like to change.

## License
Specify your license here.

---

**For any questions or support, contact the development team.**

## Project Structure

```
Project-Face-attandence-system-version-1.0/
├── app1/                    # Main application directory
├── media/                   # Media files (student photos)
├── templates/              # HTML templates
├── Project101/            # Project settings
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── db.sqlite3            # Database file
```

## Security Considerations

- The system uses Django's built-in authentication
- Admin approval required for student registration
- Secure password storage
- CSRF protection enabled

## Troubleshooting

1. **Camera Access Issues**:
   - Ensure camera is properly connected
   - Check camera permissions
   - Verify camera configuration in admin panel

2. **Face Recognition Issues**:
   - Ensure good lighting conditions
   - Check camera focus and positioning
   - Verify student photos are clear and well-lit

3. **Database Issues**:
   - Run migrations if database errors occur
   - Check database permissions
   - Verify database configuration in settings.py

## Support

For any issues or questions, please contact the development team.

## License

[Specify your license here] 
