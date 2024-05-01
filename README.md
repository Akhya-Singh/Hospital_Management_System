# Hospital Management System

This is a Django-based web application for managing patient information in a hospital. The system provides functionality to add, update, and delete patient records, as well as view and manage their medical conditions and prescriptions.

## Features

- User authentication: Users (hospital staff) can log in to access the system.
- Patient management: Add, update, and delete patient records with unique patient IDs.
- Medical history: Store and update patient conditions and prescriptions.
- User-friendly interface: Easy-to-use web interface for managing patient data.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/hospital-management-system.git
```

2. Navigate to the project directory:

```bash
cd hospital-management-system
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Set up the database:

```bash
python manage.py migrate
```

6. Create a superuser account (for admin access):

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

- Log in with your staff credentials (or use the superuser account created during installation).
- Navigate to the "Patients" section to view, add, update, or delete patient records.
- Click on a patient record to view their medical history, including conditions and prescriptions.
- Use the provided forms and interfaces to manage patient data.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## Acknowledgments

- The development team: Aryan Shambharkar, Akhya Singh, and Manan Variya.
- Shah and Anchor Kutchhi Engineering College for providing the project opportunity.
