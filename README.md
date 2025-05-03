# Django Auto Shop

A simple, sample Django web application for running an automobile repair shop. Includes support for VIN lookups, scheduling appointments, and sending email reminders.

## Features

1. Automates retieval of car information such as its model, model year, make, body, and trim by inputting the car's VIN.

2. Randomized inquiry and appointment IDs as URL GET parameters for secure links to a customer's inquiry status and appointment scheudling.

3. Using the Django Appointment library, the web application can:
   * Customize time slots for the auto shop
   * Manage appointments and approve customer repair requests
   * Use Django Q to send email with links for retrieving inquiry status, scheduling appointments, and rescheduling appointments.

4. To prevent Cross Site Request Forgeries when inputting information into forms, `csrf_token` template flags are used along with input verification such as ensuring a maximum length.

## How to Run

1. Clone or download the repo.

    ```bash
    git clone https://github.com/elijahbartolome/django-auto-shop.git
    ```

2. Download dependencies using the package manager [pip](https://pip.pypa.io/en/stable/).

    ```bash
    pip install requirements.txt
    ```

3. Create a `.env` file. It will have the following environment variables:


    * `SECRET_KEY`: Your Django secret key

    * `EMAIL_HOST_USER`: The email used to send reminder or confirmation emails

    * `EMAIL_HOST_PASSWORD`: The password or passkey for the aformentioned email

    You can use `.env.example` as a template.

4. Create the migrations and run them by doing `python manage.py makemigrations` and then `python manage.py migrate`

5. Set up super user or admin using `python manage.py createsuperuser`

6. Run the server using `python manage.py runserver`, and if the automated email sending is set up, do `python manage.py qcluster` in a separate terminal window.

7. Navigate to http://127.0.0.1:8000/admin/ to approve customer inquiries, create appointments, manage configurations, and handle appointment conflicts.

8. To simulate a customer sending an inquiry for a car repair, navigate to http://127.0.0.1:8000/ and input the information about the customer there.

## Credits

This project uses the following libraries and code snippets:

*   [Django Appointment](https://github.com/adamspd/django-appointment) -  Apache License 
    * (Modified to fit scheduling and managing appointments for an auto shop) 

This web application was inspired by an idea from the owner of Bakersfield's Sanchez Mobile Auto Repair shop.