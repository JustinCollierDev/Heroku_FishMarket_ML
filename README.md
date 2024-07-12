# AIDI-2004 Lab 4
## Heroku_FishMarket_ML

## Members:
### Justin Collier | 100345263

# Work Distribution:
## Justin Collier:
### * ...

Data Sources/References: https://www.kaggle.com/aungpyaeap/fish-market
 
## Changelog
### July, 10. 2024 - Justin
### Initial Commit / ReadME Formatting
+ Initialized the project repo & readme file

### July, 12. 2024 - Justin
### Classification Model - RF Class, Pickle File Export, Dataset Analysis
+ Added the 'Fish.csv' file to our project
+ Created a simple Random Forest Classification model to classify fish species based on the given fields.
+ Added logic for exporting our model as a .pkl (pickle) file that we can use in our Flask API later

### July, 12. 2024 - Justin
### Front-End - Building our Index.html page
+ Added an index.html page for our form submission
+ Added relevant form attributes to collect the data to later use in our Classification model.
+ Created the app.py file we will use for the next step

### July, 12. 2024 - Justin
### Flask App - Building our Web App
+ Added a templates folder for our index.html
+ Built the app.py and gave it routes for handling the home page form & prediction output
+ Modified fish_classification.py to use a label encoder
