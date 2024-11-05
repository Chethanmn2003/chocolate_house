# Chocolate House Management System
Chocolate House is a simple web-based management system for managing seasonal flavors, ingredients, and customer feedback for a chocolate shop. This application allows users to:
1. Add and view seasonal flavors.
2. Track ingredients inventory.
3. Collect and view customer feedback, including any allergy concerns.


# Prerequisites
- Docker
- Git
- python 3.9 or higher

# Setup and Installation
**Clone the repository**:
- git clone https://github.com/Chethanmn2003/chocolate_house
- cd chocolate_house

# Create a virtual environment and activate it
python -m venv venv
venv\Scripts\activate

# install packages
pip install -r requirements.txt

# Run the application
python server.py
You should now be able to access the application at http://localhost:5000

# To run the application using Docker, follow these steps:
1. In the project directory, build the Docker image with:
- docker build -t chocolate_house .
2. Run the Docker Container
- docker run -d -p 5000:5000 chocolate_house
You should now be able to access the application at http://localhost:5000
3. To view docker logs:
- docker logs <container_id>
4. To stop the container:
- docker stop <container_id>



# Database setup
- The Application uses SQLAlchemy for the interactions with SQLLite database
- To recreate the database, delete the existing database and run the application again

# Endpoints and Functionality

/seasonal_flavor
{
  "name": "Pumpkin Spice",
  "price": 4.99
}

/ingredient
{
  "name": "Cocoa Powder",
  "quantity": 100
}

/feedback
{
  "suggestion": "Add more vegan options",
  "allergy_concern": "No nuts please"
}