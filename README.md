### Solar Leads Visualization App 

This is a Django web application designed for a photovoltaic company to help streamline the work of its sales team. The app allows users to upload a file containing leads exported from their CRM, filter leads based on a date range, and visualize them on an interactive map. Each lead is displayed with additional details.
  
![Image of Visualization Sunroute](https://github.com/darkchiii/Sunroute/blob/main/visualization-sunroute-1.png)

#### Purpose
The app helps sales teams:
- Quickly identify lead distribution across regions.
- Optimize resource allocation and prioritize sales efforts.
- Enhance operational efficiency by integrating lead data with geographic visualization.

## Features
- **File Upload**: Users can upload an Excel file containing leads from their CRM.
- **Date Filtering**: Leads can be filtered by a selected start and end date.
- **Geolocation**: Postal codes from the uploaded file are geocoded to coordinates (latitude and longitude) using the OpenStreetMap API.
- **Interactive Map**: A map is generated using Folium, showing the filtered leads with markers that display relevant details when clicked.

![Image of Visualization Sunroute](https://github.com/darkchiii/Sunroute/blob/main/visualization-sunroute-2.png)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/darkchiii/Sunroute.git
cd Sunroute
```

### 2. Set up the virtual environment

It’s recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure database

The application uses SQLite by default. You can change the database configuration in the `settings.py` file if needed.

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional, for accessing Django admin)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000`.

## How it works

### File Upload
- The user uploads an Excel file containing leads, which must have columns such as:
  - **Imię i nazwisko** (Name)
  - **Telefon** (Phone)
  - **Kod pocztowy** (Postal Code)
  - **Wysokość mc opłat** (Monthly Fee)
  - **Miejsce instalacji** (Installation Location)
  - **Kiedy instalacja** (Installation Date)
  - **Uwagi** (Notes)

### Date Range Filter
- After uploading the file, the user can choose a start and end date. The application will filter the leads based on the "Data przekazania" (Transfer Date) field within the chosen date range.

### Geocoding
- The application uses the OpenStreetMap Nominatim API to geocode postal codes from the uploaded leads to latitude and longitude coordinates. If geocoding fails for a specific postal code, that lead will be excluded from the map.

### Map Rendering
- The filtered leads are displayed on an interactive map using Folium. Each lead is represented by a marker on the map with a popup displaying relevant information, such as name, phone number, postal code, monthly fee, installation location, installation date, and any notes.

## URL Routes

- `leads/upload/`: A page where users can upload their Excel file with leads and select the date range for filtering.
- `leads/map/`: A page that shows the map with the filtered leads. The map is generated using Folium and includes clickable markers with detailed information for each lead.

#### Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Mapping**: Folium (for interactive maps)
- **Geocoding**: Geopy (to convert postal codes to geographic coordinates)
- **Pandas**: Used for handling and processing the Excel data.
- **SQLite**: Default database used for storing application data (can be configured to use others, like PostgreSQL).

---
