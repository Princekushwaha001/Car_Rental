# Car Rental

A comprehensive car rental platform built with Django. This project allows users to browse, book, and review rental cars, while providing an admin interface for managing the fleet and bookings.

## Features

*   **User Authentication**: Secure user registration and login, including social authentication with Google.
*   **Car Listings**: Browse a catalog of available cars with details and images.
*   **Booking System**: Easily book cars for specific date ranges.
*   **Payment Integration**: Seamless payments using Razorpay.
*   **User Reviews**: Users can leave reviews and ratings for cars.
*   **Admin Dashboard**: A dedicated dashboard for administrators to manage cars, bookings, users, and more.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.8+
*   pip
*   Virtualenv (recommended)

### Installation

1.  **Clone the repository**
    ```sh
    git clone https://github.com/Princekushwaha001/Car_Rental.git
    cd Car_Rental
    ```

2.  **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**
    -   Copy the example environment file:
        ```sh
        cp .env.example .env
        ```
    -   Open the `.env` file and fill in your actual credentials for the Django secret key, email server, Google OAuth, and Razorpay.

5.  **Run database migrations**
    ```sh
    python car_rental/manage.py migrate
    ```

6.  **Run the development server**
    ```sh
    python car_rental/manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

*   `DJANGO_SECRET_KEY`: A strong, unique secret key for your Django application.
*   `DEFAULT_FROM_EMAIL`: The default email address for sending emails.
*   `EMAIL_HOST_USER`: Your email service username.
*   `EMAIL_HOST_PASSWORD`: Your email service password.
*   `EMAIL_PORT`: The port for your email service (e.g., 587 for TLS).
*   `GOOGLE_CLIENT_ID`: Your Google OAuth client ID.
*   `GOOGLE_CLIENT_SECRET`: Your Google OAuth client secret.
*   `RAZORPAY_KEY_ID`: Your Razorpay test key ID.
*   `RAZORPAY_KEY_SECRET`: Your Razorpay test key secret.

## Built With

*   [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
*   [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/) - For beautiful forms.
*   [Django Allauth](https://django-allauth.readthedocs.io/) - For social authentication.
*   [Pillow](https://python-pillow.org/) - For image processing.
*   [Bootstrap 4](https://getbootstrap.com/docs/4.6/) - For front-end styling.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
