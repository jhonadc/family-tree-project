INDEX
- URL
- PART I - INSTALLATION INSTRUCTIONS
- PART II - PROJECT DOCUMENTATION
  -About
  -Technology
  -Updates
  --version 0.1--
      sign-in
      sign-up
      settings
      add family member
      insert memory
      delete memory


---YOU CAN ACCESS THE WEBSITE WITH THE URL https://morning-forest-34963.herokuapp.com/ ---


PART I
--- Installation Instructions ---

Before you start, you should have Python 3.8.x installed on your computer.


Cloning this Repo
Clone this repository to your computer

Choose (or create) a working directory on your own computer and change directory into it

Clone this repository running git clone xxxxxxxxxxxxx in that working directory.

Get Set Up for Local Development:
Change directory to the recently cloned folder. 

Open tbe terminal and create a new virtual environment (e.g. 'venv') for this project:

virtualenv venv

Activate your virtual environment (Windows: source venv\Scripts\activate; Mac and Linux: source venv/bin/activate)

Download the Python modules listed in requirements.txt using pip:

pip install -r requirements.txt

Run the Flask App:
You are all set to run the app. Make sure the your virtual environment is actived and be sure to be in the root folder.

Run flask using:

flask run

All done! You can access the flask app in your browser either on http://127.0.0.1:8000/ or http://localhost:8000


PART II

--- THE FAMILY TREE PROJECT DOCUMENTATION ---

INTRODUCTION
- About
This project aims to enable family members to safely share, via the internet and cloud storage, digitalized memories (photos, texts, small videos) with other family members for generations to come, in a easy to use interface.

- Technology
The software is being developed using Flask, a Python framework to develop web applications. HTML, CSS and JavaScript are also used for the front-end part of the website, while sql databases are connected to the framework to store and retrieve the data.

For the most future proof data possible, the simpler data format will be used for storage, allowing easier change in the database in case of migration of technology used. For texts, UTF-8 format will be applied; for photograph, .jpg and, for audio, xxx format will apply.

- Updates
Version 0.1 (04.04.2021):
Definition of the technology.
File structure created.
Git repository was created.
The main page template was created with the upper nav bar.
The sign in page was created.
The sign up form was created.
-sign up
The user must access the project webpage on xxxx.com. There, he must choose the option “Sign Up”, insert the necessary data to create a profile and choose the payment form.

-sign in
If there is already an user registered, the consumer have to click on the “Sign In” option and right his email and password to access his main family tree and/or configuration.

How to Use
-settings
The user can click on “settings” on the upper right side of the screen to change his username, profile picture, background color, payment data and personal data. Click save to go back to the settings page.

-add family member
To start creating a family tree, the user must access “My family tree” on the upper menu or click the same option on the dashboard, after logging in. There will be at least one node at the tree, which is the user node. To create another one, the user must click on one of the many transparent nodes around his node, which can be his grandparents, son, brothers, spouse and many others.

-insert memory
At the “My family tree” page, the user must click on his node and chose the pop up option “Add Album” or “Edit Album”. After inserting the name of the folder and uploading the pictures, the user can now choose to what family members that specific date will be shared, among his family members. Also, he can delegate rights to edit the album to some family members.

-delete memory
At the “My family tree” page, the user must click on his node and chose the pop-up option “Add Album” or “Edit Album”.

-filter memories
The user can filter memories by year, parenthood and data. In the image bellow, we can see all the data from the year 1930 provided to the user from all his relatives. To filter, select the filter option at the main user board.

Contact

Get in touch with us: jhonathanaugusto@gmail.com
