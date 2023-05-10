# Quotme API
Quotme API was developed to serve [Quotme](https://quotme.herokuapp.com) front end project. The API has the following apps that help make the fron end project versatile and robust: *Profiles*, *Quotes*, *Authors*, *Likes*, *Saved*, *Comments*, *Replies* and *Followers*. 

# Table of content

- [**User Stories**](#user-stories)
- [**Data Model**]()
- [**Flow Chat**]()
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
