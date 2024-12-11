# Scrum_Lords
COSC_625 Group Project Repo
Our RecipeMatcher project gives users an easy, efficient way to find new recipes that they can make themselves with ingredients that they already have at home. Our application uses an AI chatbot to speak with users and help them find the perfect meal. The user can use our ChatBot page to speak directly with the chatbot and have it recommended meals, or they can use our Meal Query page and use predetermined options like meal of the day and flavor profile to have the chatbot pull a recipe for them based on the selected criteria. 

This project is useful because it provides users with an easy way to find their next meal and potentially their new favorite recipe. Our application removes the hassle of flipping through the pages of a cookbook or painstakingly searching the internet for a recipe that not only sounds delicious but can readily be made with the ingredients stocked in users’ homes.  

Upon opening our RecipeMatcher folder, you will see there are two folders inside, the RecipeMatcher and the RecipeMatcher_Database files. The RecipeMatcher_Database folder contains SQL scripts that are used to create our SQL databases used for storing meal and user information. The RecipeMatcher folder contains the rest of the crucial files for our project.  

Inside of the RecipeMatcher folder you will see a handful of folders and standalone files. The folders are the src folder, our front end, the backEnd folder, a folder for instantiating a virtual environment, or venv, and the logs folder. One of these standalone files is the requirements.txt file. This file is crucial as it will be used to install all of the dependencies necessary to run our application. 

Inside of our source (src) folder are the pages folder, and python files used for launching (__main__.py) and running (app.py) our application. There are also files for authenticating users (user_auth.py) and building the user profile page (user_profile.py).  

Inside of the pages folder are python scripts for creating all the pages in our application. These include a page to speak with our chatbot (chatBotPage.py), the home page (homePage.py), our login page (loginPage.py), the page used for pulling meals from TheMealDB API (mealdbTest.py), the page used for querying TheMealDB with our chatbot (mealQueryPage.py), and the page used for generating recipes (recipeGeneration.py). These files are crucial to our project as they create what users will be interacting with to use our application. This folder also contains api.py, the file used for establishing links to use TheMealDB.  

The venv folder is used for creating a virtual environment that can be used for running our application. The virtual environment is used for running Flask, which will be used for establishing communication between our application and our SQL databases. 

The backEnd folder contains files necessary for the application to communicate with our SQL databases stored on a MySQL server. __init__.py creates our Flask application, which hosts the communication and allows our databases to be viewed through a localhost webpage. models.py uses SQLAlchemy to create the SQL databases to be used by our application, they mirror what can be seen in the MySQL server. Then, routes.py uses Flask to set and get information from our MySQL databases.  
