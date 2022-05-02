# labdb
Lab database overview

Watch the youtube video - https://youtu.be/4_nJnShlgW4

This project collects and organizes development and sample requests for the KRI-Color Lab. KRI-color is a silicone pigment dispersion company located in Sanford, Maine. We manufacture silicone pigments for use in many industries including automotive, medical, architectural, aerospace, and more. In order to sell our products, our sales people must gather information from prospective customers. This infomration is critical for our team to design a material that will meet all of our customer expectations. This information includes things like color (match an existing part or develop from Pantone for example), FDA compliance required, type of material (Silicone comes in various forms - HCR, RTV, LSR) and much more.

Once the lab receives this information, it is prioritized and worked on according to resources. This database does the following:

1. Allows users to register and login. Once logged in, they will see various menus depending on their credentials. For example, an administrator can see the "users" tab showing all registered users. (Right now this is the only advantage to being an administrator)

2. Users can request a new development project - adding customers, addresses, and contacts along the way. These are typically custom colors. For example, a customer may want us to develop a material that matches the iphone "rosegold" color. They may plan to make a silicone sleeve that matches an iphone.

3. Users can request a new "Internal" project. These projects are projects that do not require customer interaction. For example, we may want to internally evaluate a new pigment for heat stability or as a potential offset to a current pigment.

4. Users can request a standard sample be sent to a customer. These are products that we keep in stock at all times.

5. Users can see all open requests. These requests can be filtered or sorted. 

6. Users can see all closed, or signed-off, requests. This is a historical record of the work. These tables can also be sorted and filtered.

EMAIL - Every time a request is submitted an email is sent to let the whole group know that there is a new request. Right now, I have only added my own email so that I don't bother my team. I will change this when I deploy. When a user registers, they will receive an email welcome. When a request is completed (signed off), an email is sent to the team, letting them know that the request was completed. It will also include UPS tracking information. Again, this currently is set to go to my email so that I don't bother the team.

************************* ENVIRONMENT *****************************

This application users: SQLITE3, CSS, HTML, Javascript, Jinja, Flask, and Python

You must have the following installed (see the requirements.txt for more information):
Python
Flask==2.1.1
Flask-Mail==0.9.1
Flask-Session==0.4.0
greenlet==1.1.2
gunicorn==20.1.0
idna==3.3
itsdangerous==2.1.2
Jinja2==3.1.1
MarkupSafe==2.1.1
psycopg2==2.9.3
requests==2.27.1
SQLAlchemy==1.4.36
sqlparse==0.4.2
termcolor==1.1.0
urllib3==1.26.9
Werkzeug==2.1.1

ENVIRONMENTAL VARIABLES -  You must set your environmental variables prior to use in order for the application to run.
1. KEY MAIL_DEFAULT_SENDER VALUE: type a sender email
2. KEY MAIL_PASSWORD VALUE: type a password to an smtp server
3. KEY MAIL_USERNAME VALUE: type a username to an smtp server

I have deployed this to Heroku and am currently working through transitioning SQLite to PostgreSQL. You will notice the Procfile in my folder. This is only needed for Heroku and not for local use.

You will also see hello_flask folder. This is only used for my virtual environment while running visual studio on my local machine. It is not needed if you will be running this on github VS codespace.

How to use the KC LAB Database

1. The home page before registration.
    a. This shows an embedded google calendar. The live version will utilize my company google calendar. This CS50 will only show the publicly available holiday calendar.
    b. Left side nav tabs. Before registering and logging in, you will only see links to my normal company websites.
    c. Upper right corner shows the registration and login links. You must register before gaining access to additional resources. Once registered, you should receive an email confirmation if environmental variables are set correctly. Once logged in, you can edit your profile if needed from this same location by clicking "profile." This lets you change your name, email, or password.
    d. The "TOGGLE MENU" button allows you to close the nav tab bar on the left for more space.

2. The home page once registered.
    a. Left hand nav tabs.
        1. Request a new development. Walk through for requesting a new (EXTERNAL or INTERNAL) experimental sample.
        2. Open Developments. Shows all open EXTERNAL development requests that need to be fulfilled.
        3. Completed Developments. Shows all historical requests that have been completed.'
        4. Request Standard Sample. Walk through for requesting samples of materials we already produce.
        5. Open Std Requests. Shows all open standard sample requests.
        6. Completed Std Samples. Shows all historical standard sample requests that have been completed.
        7. Open Internal Evals. Shows all INTERNAL experiments.


