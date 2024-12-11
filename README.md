# **EcoHub**

EcoHub is a Django-based e-commerce platform designed to provide users with a sustainable shopping experience. The platform allows users to browse eco-friendly products, add them to a shopping cart, and place orders.

---

## **Key Features**
- 🧑‍💻 **User Accounts**: Registration, login, profile management, and password reset.
- 🛒 **Products**: Browsing, searching, and managing eco-friendly products.
- 📦 **Orders**: Shopping cart and order placement functionality.
- ✍️ **Reviews**: Users can leave testimonials and feedback.
- 🌐 **Common Features**: Homepage, contact form, and custom 404 error page.

---

## **Requirements**
- **Python**: 3.10+
- **Django**: 4.2+
- **PostgreSQL**: Local database
- **Docker**: For running the database locally

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
- 📂 **Database**: The database is hosted in a Docker container. Create your own superuser to manage the application.
- 🖼️ **Media Files**: Product images are stored in the `media/` directory locally. Ensure the directory is writable.
- 🔗 **Footer Links**:
  - A Facebook page (created as a simulated contact option).
  - A YouTube link to a short video, simulating a promotional ad for the products.
- 🎨 **Interactive Footer**: The footer includes links with icons and minor animations for an enhanced user experience.

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

