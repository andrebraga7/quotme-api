# Quotme API
Quotme API was developed to serve [Quotme](https://quotme.herokuapp.com) front end project. The API has the following apps that help make the fron end project versatile and robust: *Profiles*, *Quotes*, *Authors*, *Likes*, *Saved*, *Comments*, *Replies* and *Followers*. You can find out more about the **Quotme** front end project by having a look at the readme file and Github repository [here](https://github.com/andrebraga7/quotme/blob/main/README.md).

# Table of content

- [**User Stories**](#user-stories)
- [**Data Model**](#erd---entity-relatinship-diagram)
- [**Technologies Used**]()
- [**Validator Testing**]()
- [**Known Bugs**]()

# User Stories
In order to plan the develop of the project I created the following issues using **Github Board**:

![Issues](assets/readme-images/user_stories.png)

[Back to top](#table-of-content)

# ERD - Entity Relatinship Diagram
The ERD diagram was deeloped used [Lucidchart](https://www.lucidchart.com/) and it helped me to visualize all the necessary models to make the front end project possible.
The Django built in user model was used along with the following custom models:

- **Profile (user profile)** - Useed to store user aditional information like *name*, *bio* and *profile image*;
- **Quotes** - Stores all information for the quote;
- **Authors** - This model generates gets or creates a new author instance when creating a quote;
- **Likes** - Store likes information for quotes;
- **Saved** - This model is used to store user saved quotes information;
- **Comments** - Used to store comment information for each quote;
- **Replies** - The replies model is related to the comment and store replies for each comment;
- **Followers** - Model used to store followers information for users.

![ERD](assets/readme-images/erd.png)

 # **Technologies used**

 ## Languages

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the backend API.

## Frameworks & Software
- [Django REST](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [Github](https://github.com/) - Used to host and edit the website;
- [Gitpod](https://www.gitpod.io) used to push changes to the GitHub repository;
- [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal in gitpod;
- [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to;
- [Cloudinary](https://cloudinary.com/) - A service that hosts all static files in the project;
- [CI PEP8 Linter](https://pep8ci.herokuapp.com/) - used to validate the Python code.

[Back to top](#table-of-content)

## Libraries

In the list below are all the libraries used in the project, these are located in *package.json*:

- [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI;
- [cloudinary](https://pypi.org/project/cloudinary/) - The Cloudinary Python SDK allows you to quickly and easily integrate your application with Cloudinary. Effortlessly optimize, transform, upload and manage your cloud's assets;
- [dj-database-url](https://pypi.org/project/dj-database-url/) - Used to configure Django application.
- [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [django-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
- [django-filter](https://pypi.org/project/django-filter/) - Django-filter is a generic, reusable application to alleviate writing some of the more mundane bits of view code.
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - Simple JWT is a JSON Web Token authentication plugin for the Django REST Framework.
- [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
- [oauthlib](https://pypi.org/project/oauthlib/) - OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
- [Pillow](https://pypi.org/project/Pillow/) - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
- [PyJWT](https://pypi.org/project/PyJWT/) - A Python implementation of RFC 7519.
- [python3-openid](https://pypi.org/project/python3-openid/) - OpenID support for modern servers and consumers.
- [pytz](https://pypi.org/project/pytz/) - This is a set of Python packages to support use of the OpenID decentralized identity system in your application, update to Python 3
- [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) - Provides first-class OAuth library support for Requests.
- [sqlparse](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

[Back to top](#table-of-content)
