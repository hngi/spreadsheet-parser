<<<<<<< HEAD
# Team-Granite-Backend
A Spreadsheet Parser

## Run the App: 
- Fork this repository
- Clone to your local machine
- `cd` into the repository and create a virtual environment
- activate the environmment
- Then run `pip  install -r requirement.txt`
- This will download all the dependencies for this application.
<br/>
- <b> Note: Add the name of your virtual environment to the .gitignore file</b>

## Using the service
- We have Pandas as part of the dependencies. 
- Make sure you import pandas. You can import pandas as pd.
- To read the excel run, use this function `pd.read_excel('name of file.xlsx')`
- Please make sure you read the file into a variable, acceptable variable names include `d_frame, df, data_frame, etc.`
- To read the data frame into another another file, use this function `d_frame.to_json(name of file.csv)`
- For more information on how to manipulate data using pandas visit `https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html`

## Contribute guide
If you're in team-granite-backend:
- Add the main repository as an upstream `git remote add upstream https://github.com/hngi/spreadsheet-parser.git`
- Pull the latest version of the repo `git fetch upstream`
- follow this guide `https://medium.com/@topspinj/how-to-git-rebase-into-a-forked-repo-c9f05e821c8a` if lost.
- Create a feature branch with your feature name, e.g: `<user-pagination>`
- Create the your feature locally and commit
- Send a PR after you have test your feature locally with Postman
- Tell us in your PR in bullet points what you have added
- Add yourself as a user to the database (this will eventually count for contribution points)

### requirement.txt content
- asgiref==3.2.10
- dj-database-url==0.5.0
- Django==3.0.7
- django-heroku==0.3.1
- djangorestframework==3.11.0
- docopt==0.6.2
- gitignore==0.0.8
- numpy==1.18.5
- pandas==1.0.5
- psycopg2==2.8.5
- python-dateutil==2.8.1
- python-dotenv==0.13.0
- pytz==2020.1
- six==1.15.0
- sqlparse==0.3.1
- whitenoise==5.1.0

