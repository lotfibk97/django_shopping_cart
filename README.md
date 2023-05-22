# Shopping Cart Web Application

This is a simple shopping cart web application built with Django.

## Features

- Display a shopping cart with three predefined products.
- Ability to view and edit the inventory of products from the Django admin.
- Validate product availability when submitting the form.
- Display descriptive errors or a confirmation message based on the order status.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/lotfibk97/django_shopping_cart.git
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv ENV
source ENV/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Apply the database migrations:

```bash
python manage.py migrate
```

5. Insert initial data

```bash
python manage.py insert_data
```

6. Create a superuser account for accessing the Django admin:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Open your web browser and navigate to `http://localhost:8000` to access the shopping cart.

## Usage

1. Open the Django admin by navigating to `http://localhost:8000/admin` and log in using the superuser account created
   earlier.

2. In the admin interface, manage the inventory of products by adding, updating, or deleting products as needed.

3. On the shopping cart page, you will see the list of products, their quantities, prices, and the line prices.

4. Adjust the quantity of each product using the input fields. The line prices and total price will be updated
   automatically.

5. Click the "Buy" button to submit the form and process the order. If there are any errors, such as product
   unavailability, you will see a descriptive error message. Otherwise, a confirmation message will be displayed.

6. The quantity adjustment and price updates are done dynamically without refreshing the page.


