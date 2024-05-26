## Rentify - A Modern Rental Website

**## Project Overview**

This project is a full-stack web application built with Django (backend) and React (frontend) to manage and showcase rental properties. It offers a user-friendly experience for both listing owners and potential renters.

**## Tech Stack**

* **Backend:**
    * **Python 3.11:** The core programming language for the Django framework.
    * **Django 4.2:** A high-level web framework for rapid development.
    * **Django REST Framework :** A toolkit for building RESTful APIs within Django (if applicable).
    * **PostgreSQL 16-alpine:** A robust relational database for storing rental data.
    * **Redis 7-alpine:** A high-performance in-memory data store used for caching or background tasks (if used).
    * **Celery:** An asynchronous task queue for handling background jobs efficiently (if used).
* **Frontend:**
    * **React:** A powerful JavaScript library for building dynamic user interfaces.
    * **Webpack :** A module bundler for packaging React components and dependencies (if used).
    * **React Router:** A library for managing client-side routing in React applications (if used).

* **DevOps (optional):**
    * **Docker:** A containerization platform for deploying services in a consistent and isolated environment.
    * **Docker Compose:** A tool for defining and managing multi-container applications.
    * **Nginx:** A high-performance web server for serving static content and reverse proxying requests to the Django backend (if used).

**## Project Structure (High-Level)**

```
rentify-app-django/
├── rentify_core/  # Django project directory
│   ├── settings.py/  # Django project settings
│   ├── ... 
│   ├── 
│   ├── 
│   └── ... (other backend-related files)
├── rentify_api/  # Django app
│   ├── urls.py/  # Django backend urls
│   ├── ... 
│   ├── 
│   ├── 
│   └── ... (other backend-related files)
├── compose
│   ├── local
│       ├── django
│       │   ├── Dockerfile
│       │   ├── celery
│       │   │   ├── beat
│       │   │   │   └── start
│       │   │   ├── flower
│       │   │   │   └── start
│       │   │   └── worker
│       │   │       └── start
│       │   ├── entrypoint
│       │   └── start
│       └── webpack
│           ├── Dockerfile
│           └── start
│   └── production
│       ├── django
│       │   ├── Dockerfile
│       │   ├── celery
│       │   │   ├── beat
│       │   │   │   └── start
│       │   │   ├── flower
│       │   │   │   └── start
│       │   │   └── worker
│       │   │       └── start
│       │   ├── entrypoint
│       │   └── start
│       └── webpack
│           ├── Dockerfile
│           └── start
├── src/  # React project directory
│   ├── components/  # React components and code
│   ├── environment  # React env variables
│   └── ... (other frontend-related files)
├── nginx.conf  # (Nginx config)
├── .env/  # Environment variables
│   ├── development/  # Development environment variables (optional)
│   ├── production/  # Production environment variables (optional)
│   └── ... (other environment files)
├── README.md  # This file
└── ... (other project files)
```

**## Project Setup**

**Prerequisites:**

* Python (version 3.11 or later) installed: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Node.js and npm (or yarn) installed: [https://nodejs.org/en](https://nodejs.org/en) (if using React)
* Docker: [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

## Running Rentify with Docker Compose

This project utilizes Docker Compose for managing its multi-container environment. It provides two configuration files: `local.yml` and `production.yml`. Here's how to get started with each, along with some additional commands:

**1. Local Development with `local.yml`**

This configuration is ideal for development and testing on your local machine. To start the containers:

   ```bash
   docker-compose -f local.yml up 
   ```
if using local change the env imports to localEnviron.js instead of prodEnviron.js in src folder

**Explanation:**

   * `docker-compose`: The command to interact with Docker Compose.
   * `-f local.yml`: Specifies the `local.yml` file for configuration.
   * `up`: Starts the services defined in the compose file.


**2. Production Deployment with `production.yml`**

This configuration is tailored for a production environment where you might have different settings for security, performance, or resource allocation. To deploy:

   ```bash
   docker-compose -f production.yml up 
   ```

**Explanation:**

   * Same as the local setup command, except it uses the `production.yml` file.

**Additional Commands:**

* **Generate Test Data:**
    * You can use your custom management command to generate fake data for testing purposes:

        ```bash
        docker-compose -f local.yml run web python manage.py generate_test_data
        ```

        **Explanation:**
        * `docker-compose -f local.yml run web: Executes the following command inside the `django` container.
        * `python manage.py generate_test_data`: Runs your `generate_test_data` management command.

* **Create a Superuser:**
    * To create a superuser for administrative access, use the following command outside of Docker Compose:

        ```bash
        docker-compose -f local.yml run web python manage.py createsuperuser
        ```

        **Explanation:**
        * Same as above, this runs the `createsuperuser` command inside the `django` container.
        * Follow the prompts to enter your desired username, email, and password.
    * After creating a superuser and generating fake data you can see all the users in the django admin pannel and the password for all users will be 'password123'
    * You can login as different users and play with the web app as wished

**Important Notes:**

* Ensure Docker is installed and running on your system before using these commands.
* Make sure you have built the Docker images for your project beforehand. You can usually do this by running `docker-compose build` in the project directory.
* The `-d` flag is optional but recommended for production use as it allows the containers to run in the background.

**Additional Tips:**

* To view the logs of a running container, use `docker-compose logs <container_name>`.
* To stop all containers, use `docker-compose down`.
* For more advanced usage and troubleshooting, refer to the official Docker Compose documentation: [https://docs.docker.com/compose/](https://docs.docker.com/compose/).

By following these steps, you can effectively utilize Docker Compose to manage your Rentify application in both development and production environments. You can also leverage the provided commands to generate test data and create a superuser for administrative tasks.


## User Roles and Permissions

Rentify offers different user roles with specific functionalities:

**1. Tenant**

- Tenants are users seeking rental properties.
- They can:
    - Create an account and manage their profile information.
    - View rental listings.
    - View their profile and past interactions with owners.
    - See invitation messages from owners regarding specific properties.
    - Express interest in a property by clicking the "I'm Interested" button.

**2. Owner**

- Owners are users who list properties for rent.
- They can:
    - Create an account and manage their profile information.
    - Add new rental properties, including details, photos, and availability.
    - View their listed properties and manage them.
    - View details and profiles of tenants who expressed interest in their properties.
    - Send invitations to interested tenants for specific properties.
    - Access the Django Admin panel to manage users, properties, and other administrative tasks. (Permissions may vary depending on your implementation.)

**Workflow:**

1. A Tenant creates an account and browses available listings.
2. The Tenant can view their profile and past interactions with Owners.
3. When interested in a property, the Tenant clicks "I'm Interested."
4. This creates an "interest" record within the system.
5. The Owner receives a notification or can view interested Tenants in the Django Admin.
6. The Owner can then send an invitation to the interested Tenant(s).
7. The Tenant receives the invitation message and can choose to accept or decline.

**Implementation Notes:**

- You'll need to implement user authentication and authorization mechanisms in Django to differentiate user roles and restrict access to specific functionalities.
- Consider using Django's built-in user model or a third-party library like django-allauth for user management.
- Model the "interest" functionality (Tenant expressing interest) and invitation system appropriately.
- Integrate the "I'm Interested" button action with sending notifications to Owners.
- Grant Owners access to the Django Admin panel with appropriate permissions to view interested Tenants, manage properties, and send invitations.

**Additional Considerations:**

- You may want to implement a messaging system for communication between Owners and Tenants.
- Consider adding review and rating functionalities for both Owners and Tenants.

This structure provides a basic framework for user roles and permissions. You can further customize it based on your specific project requirements.
