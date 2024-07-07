# E-commerce-Website-DRF

## DRF E-commerce Platform

An advanced e-commerce platform built with Django and Django REST Framework (DRF). This project provides a robust backend solution for managing products, orders, users, and payments, with a focus on clean architecture, scalability, and security.

## Features

1. **User Management**:
   - Secure user registration, authentication (using JWT), and profile management.

2. **Product Management**:
   - CRUD operations for products with support for images and inventory management.

3. **Shopping Cart**:
   - Persistent shopping cart functionality for authenticated users.

4. **Order Management**:
   - Order creation, tracking, and management.

5. **Payment Processing**:
   - Integration with Stripe for secure payment processing.

6. **Admin Interface**:
   - Django admin integration for easy management of all entities.

7. **API Documentation**:
   - Automatically generated API documentation using DRF's built-in tools.

8. **Security**:
   - JWT-based authentication, secure password storage, and best practices for API security.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default, easily switchable to PostgreSQL, MySQL, etc.)
- **Authentication**: JWT (JSON Web Tokens) using djangorestframework-simplejwt
- **Payments**: Stripe API
- **Testing**: Django's built-in testing framework with DRF's API test tools

## Installation

1. Clone the repository:
   ```
   git clone ¹
   cd drf-ecommerce-platform/ecommerce
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Create a superuser to access the admin interface:
   ```
   python manage.py createsuperuser
   ```

7. Access the API at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) and the admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or feedback, please reach out to feyzisiyavash@gmail.com.

---

