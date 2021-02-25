## Guide_api

Work in progress

FastApi + React(TS) + MobaX <br>

FastApi <br>

Each user can put a annonse about that he is looking for a guid with a specific language skill (np Norwegian or Spanish)
in specific city, or info that he is the guide with the language skill in the town.

User can give a rating to another user (later an average is display when you take info about user) 
and answers under annonses.

Also he can search for a person with a mandatory language in city or looking for specific person by email.
 

Live: Work in progress

Client Side React(TS): Work in progress

How to run this app ?

copy this to your terminal and specific directory
    
    git clone https://github.com/kdrozdz/guide_api_fastApi.git 

then in terminal go to a project directory

    cd guide_api_fastApi
create a venv

    if you don't have a tool for that:
    sudo apt-get install python3-venv

    python3.6 -m venv venv

activate the venv
    
    source venv/bin/activate

install all requirement
    
    pip install -r requirement.txt

If you first time running this app create a file .env and fill it with all mandatory things.

Then run script for migration and populate your db (you must be in guide_api_fastApi)
    
    python3 migrate_and_populate.py 

Run app:

    python3 core.py

It starts on port 8000, put this to your browser url
    
    http://localhost:8000/
    
