# SPREADSHEET-PARSER SETUP STRUCTURE

These guidelines must be adhered to so as to ensure consistency in the API. Make sure to go through it and ask questions 
if you have anything confusing you.

# FOLDER STRUCTURE

spreadsheet-parser/
- └─── excel_parser/   # The main Django Project that contains the settings file.
- └─── excelApi/   # The Django App that contains the view for parsing excel files.
- └─── media/   # This folder is a test folder that contains the excel file.
- └─── parse/   # The Django App that will allow a user to input their excel file and returns JSON.
- └─── static/    # This contains the static files needed for this project
- └─── staticfiles/   # Django Collect static.
- | .gitignore   # Ignores set parameters when pushing to GItHub.
- | manage.py   # Django project file that runs the server.
- | Procfile   # Contains the necessary settings to deploy on Heroku.
- | README.md   # Please read me.
- | requirements.txt   # The utilities folder containing helper functions and modules
- | runtime.txt   # This contains the necessary Python build for Heroku deployment.

# PACKAGES/DEPENDENCIES

Do not install or uninstall any package unless it has been discussed with the team and approved by a team lead or mentor. Your 
work would be invalidated if you do this. 

- asgiref==3.2.10
- certifi==2020.6.20
- chardet==3.0.4
- dataclasses==0.6
- defusedxml==0.6.0
- diff-match-patch==20181111
- dj-database-url==0.5.0
- Django==3.0.8
- django-heroku==0.3.1
- et-xmlfile==1.0.1
- gunicorn==20.0.4
- idna==2.10
- jdcal==1.4.1
- MarkupPy==1.14
- numpy==1.19.0
- odfpy==1.4.1
- openpyxl==3.0.4
- pandas==1.0.0
- psycopg2==2.8.5
- python-dateutil==2.8.1
- python-dotenv==0.14.0
- pytz==2020.1
- PyYAML==5.3.1
- requests==2.24.0
- six==1.15.0
- sqlparse==0.3.1
- tablib==2.0.0
- urllib3==1.25.9
- whitenoise==5.1.0
- xlrd==1.2.0

# CONTRIBUTION GUIDE
If you want to contribute:
- Add the main repository as an upstream `git remote add upstream https://github.com/hngi/spreadsheet-parser.git`.
- Pull the latest version of the repo `git fetch upstream`.
- follow this guide `https://medium.com/@topspinj/how-to-git-rebase-into-a-forked-repo-c9f05e821c8a` if lost.
- Create a feature branch with your feature name, e.g: `<user-pagination>`.
- Create the your feature locally and commit.
- Send a PR after you have test your feature locally with Postman.
- Tell us in your PR in bullet points what you have added.
- Add yourself as a user to the database (this will eventually count for contribution points).
- We have Pandas as part of the dependencies. 
- Make sure you import pandas. You can import pandas as pd.
- To read the excel run, use this function `pd.read_excel('name of file.xlsx')`
- Please make sure you read the file into a variable, acceptable variable names include `d_frame, df, data_frame, etc.`
- To read the data frame into another another file, use this function `d_frame.to_json(name of file.csv)`
- For more information on how to manipulate data using pandas visit `https://pandas.pydata.org/pandas-docs/stable/
user_guide/io.html`.
- For the `Environmental Variable`, change `.envexample`file in excel_parser folder to `.env`. 
- For the `SECRET_KEY` enter 25 RANDOM STRINGS in the `.env`.
