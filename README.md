# **EcoHub**

EcoHub is a Django-based e-commerce platform designed to provide users with a sustainable shopping experience. The platform allows users to browse eco-friendly products, add them to a shopping cart, and place orders.

---

## **Key Features**
- 🧑‍💻 **User Accounts**: Registration, login, profile management, and password reset.
- 🛒 **Products**: Browsing, searching, and managing eco-friendly products.
- 📦 **Orders**: Shopping cart and order placement functionality.
- ✍️ **Reviews**: Users can leave testimonials and feedback.
- 🌐 **Common Features**: Homepage, contact form, and custom 404 error page.
- 🗺️ **Google Maps Integration**: Displaying locations on Google Maps using an API key.

---

## **Requirements**
- **Python**: 3.10+
- **Django**: 4.2+
- **PostgreSQL**: Local database
- **Docker**: For running the database locally
- **Google Maps API Key**: Optional, if testing the Google Maps integration

---

## **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Emil-Petkov/EcoHub.git
   cd EcoHub
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the PostgreSQL database with Docker**:
   ```bash
   docker run --name ecohub-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=ecohub -p 5432:5432 -d postgres
   ```

5. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

---

## **Important Notes**
> **Summary**: The project requires you to set up your own database, generate a new SECRET_KEY, and optionally provide your own Google Maps API key if you wish to test the map functionality. During the local demonstration, I will use my own keys.

## **Important Notes**
- 📂 **Database**: The database is hosted in a Docker container. Create your own superuser to manage the application.
- 🖼️ **Media Files**: Product images are stored in the `media/` directory locally. Ensure the directory is writable.
- 🔗 **Footer Links**:
  - A Facebook page (created as a simulated contact option).
  - A YouTube link to a short video, simulating a promotional ad for the products.
- 🗺️ **Google Maps**: The project includes integration with Google Maps. For the demonstration, a local Google Maps API key is used. If the examiner wishes to test this feature, they should provide their own API key in the `.env` file under the variable `GOOGLE_MAPS_API_KEY`.
- 🔒 **Django SECRET_KEY**: The `SECRET_KEY` is stored in the `.env` file for security. Ensure you generate your own `SECRET_KEY` if setting up the project.

---

## **Testing**
To run the tests:
```bash
python manage.py test
```

---

## **Project Overview**
EcoHub consists of the following apps:

1. **Accounts**: Handles user authentication and profile management.
2. **Products**: Displays products and allows CRUD operations for administrators.
3. **Orders**: Enables users to manage their shopping cart and place orders.
4. **Reviews**: Provides a platform for users to leave testimonials and feedback.
5. **Common**: Manages shared features like the index page, contact form, and custom error pages.

---

## **Screenshots**

### 1. Home Page
![1](https://github.com/user-attachments/assets/1f6f4f99-9f16-4026-8460-c481cdc30cdd)


### 2. Promotions Section
![2](https://github.com/user-attachments/assets/a2e41406-91f4-4c42-b1c5-30d839fa9647)


### 3. Stats Section
![3](https://github.com/user-attachments/assets/43efd3bd-e487-40dd-b074-542a8c6cdd2c)


### 4. Login Page
![4](https://github.com/user-attachments/assets/0f4a519a-0c45-4318-a8fe-d18b03a6462e)


### 5. Manage Products and Profile
![5](https://github.com/user-attachments/assets/eb475dd0-b292-4379-8b33-56c8dbcef288)


### 6. Shop Page with Filters
![6](https://github.com/user-attachments/assets/5c7a5176-7912-4aec-b71a-e7b026bb9d24)


### 7. Shop Filtered Results
![7](https://github.com/user-attachments/assets/d118567a-9506-43c0-bd52-634d12a7a392)


### 8. Product Details
![8](https://github.com/user-attachments/assets/53e660cc-e744-4fbd-a7eb-21602081d5c3)


### 9. Shopping Cart
![9](https://github.com/user-attachments/assets/68fd4324-a5cb-4dd5-8bee-79f5d70e0ace)


### 10. Checkout Page
![10](https://github.com/user-attachments/assets/3e30b511-ebe5-42ee-9078-7911dd59346a)

### 11. Testimonials Page
![11](https://github.com/user-attachments/assets/ffeded3c-38d7-4203-9ecf-aa9249191d35)


### 12. Contact Page
![12](https://github.com/user-attachments/assets/48c6ca70-e379-4ac1-969e-814b33d810f6)

### 13. 404 Error Page
![13](https://github.com/user-attachments/assets/8994cc07-e7fc-418d-83cb-fe711ddfdab6)


