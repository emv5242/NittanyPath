#NittanyPath

##Description

### Context

This application adds and deletes patient from a database for a hospital and randomly assigns a pid to each new patient.

### Features

The application’s home page has a dropdown that asks the user to pick which action they would like to perform between the options of add a patient and delete a patient. On the input page, the user will type in the first and last name of the patient that they want to add. Once they do this they hit the “Input” button which will automatically produce the table of the database that will have the added patient. The delete page looks similar to the input page. The user can again type in the patient that they want to delete. If the patient that has been entered is already in the system, it will be deleted and the updated table will appear below. Once the “Delete Patient” button is pushed, a modal will appear asking if the user is sure that they want to delete the patient, and once they hit the “Save Changes” button the patient will be deleted. 

### Organization

In theis project there are three html files that correspond to the template of the three pages and one python file that handles all of the functions and navigating through the pages. In the python file it has two functions valid\_name\_delete and valid\_name that power what happens when you input the names in both the add and delete pages. They both check if the name inputted is valid (meaning its not null) and then the valid\_name function adds the name to the database and then displays the updated database on the page. The valid\_name\_delete function checks the database for the name and then deletes the name if it is in the database. Like the valid\_name function, valid\_name\_delete also then displays the updated database.

### Instructions

After you unzip the file to the preferred location, then open the file in Pycharm you can hit the green button in the top corner to run the program and then after going to the localhost the home page should appear. Once on the homepage, you will select which action that you would like to take. If you want to add a patient, on the add page you will type in the first and last name of the patient. Then you will hit input. The website will then show the updated database. Similarly to delete a patient type in their name on the delete patient and then hit the Delete Patient button. After doing so, there will be a popup asking if you are sure, hit Save Changes and then your patient will be deleted. After this the updated database will appear at the bottom of the page.
