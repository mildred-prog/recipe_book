# Recipe Book

Recipe Book is a simple and welcoming web app where people from all cultures can share their favorite recipes, explore dishes from around the world, and even plan their meals for the month. Users can sign up, create a profile, upload photos, and add step-by-step instructions for their recipes. It’s all about celebrating food, culture, and making meal planning a little easier — one recipe at a time.   
Live link: https://recipe-book-app-345a4345dace.herokuapp.com/

![Screen Mock-up](static/documentation/readme/screen-mockup.webp)

## Overview
What makes The Recipe Book special is its focus on people. Anyone can sign up, create a profile, and start contributing their favorite recipes — complete with photos, cooking steps, and even monthly meal planning. It’s a beautifully responsive site that works on any screen, making it easy to browse on the go or in the kitchen. Built with Bootstrap 5, it offers a clean, modern look while staying flexible and intuitive. It’s not just about food — it’s about connection, community, and keeping culinary traditions alive.

## Features

__Existing features:__

- **Home page**
  
  - **Hero Section:** The hero section features a warm and inviting image of a beautifully decorated cupcake, and a spoon placed on a recipe book, — symbolizing creativity, tradition, and the joy of homemade meals. This visually striking banner sets the tone for the site, welcoming users into a space where recipes from diverse cultures are celebrated and shared.                                                                        ![Home screen](static/documentation/readme/home.jpg)  
  
  - **Introductory Text:**   Sets the tone with a heartfelt message about the importance of food, community, and diversity, encouraging users to contribute and connect.                                                                  
  ![Welcoming Text](static/documentation/readme/intro-text.jpg) 

  -  **Mobile-Responsive layout:**  Built with Bootstrap 5 to ensure a clean, functional design on all devices.

- **Recipe Search**
   - **Search Bar:** Users can search for recipes using keywords, making it easier to find specific dishes on the website.                                                                                                                          !
  
  ![Search bar](static/documentation/readme/searchbar.jpg)   
    
- **Navigation Menu:** Quick access to all major sections:
   - **Home:** Return to the landing page
   - **Recipes:** Browse all available recipes
   - **New:**  Add a new recipe to the collection.
   - **Profile:** View and manage user profile.
   - **Logout:**  Securely end user session            


  ![Navigation Bar](static/documentation/readme/navbar-mobile.jpg) 
  
- **Recipes Pages:**
   - **View recipes:** Displays a list of all contributed recipes from various users.
   - **Responsive layout:** Recipes are shown in an organized grid or card format.
   - **Search filter support:** Works with the search bar for real-time recipe filtering.
  ![Recipes Mobile layout](static/documentation/readme/recipes-layout1.jpg)
  ![Recipes grid](static/documentation/readme/recipes-layout2.jpg)
  ![Recipes full screen](static/documentation/readme/recipes-layout3.jpg)

- **Add Recipes Page:**
   - **User Submission Form:**  Allows registered users to submit a new recipe, including title, description, ingredients, steps, and an image.
   - **Rich Text Support:** With the use of Summernote, users can format recipe instructions (e.g., bold text, bullet points).
   - **Image Upload:** Uploads recipe photos.                                                                                                                         
   ![Add recipe](static/documentation/readme/add-recipe.jpg)

- **User Profile Page:**
  - **View Personal Info:** Displays the user's profile information;name, date joined and recipes added.         
                                                    
  ![Profile](static/documentation/readme/profile.jpg)

  - **Edit Profile:** Users can update their profile details, image.
  ![Profile Edit](static/documentation/readme/profile-edit.jpg)                                                                                                                               
- **Meal Planner:**
   - **Plan Monthly Meals:** Helps users organize their recipes; breakfast,lunch or dinner — perfect for family or personal meal scheduling.
   - **Custom Recipes:** Users can add their own recipes and assign them to specific days.                                                    

   ![Meal Planner](static/documentation/readme/monthly-planner.jpg)


- **Authentication:**
   - **Logout:** Ends a user session securely.
  ![Sign out](static/documentation/readme/sign-out.jpg)
   - **Registration/Login:**  Users can create an account or log in to access features like profile management and recipe posting.


     ![Sign up](static/documentation/readme/sign-up.jpg)
      ![Sign in](static/documentation/readme/sign-in.jpg)                                                                               
- **CRUD Functionality:** 
   - **Create::** Logged-in users can add new recipes through a submission form. After adding a recipe, a pop-up success message (toast notification) confirms that the recipe was successfully created.
   - **Read:** All users (logged in or not) can browse and search the available recipes. Each recipe can be viewed on a dedicated detail page that shows full ingredients and instructions.
   - **Update:** Logged-in users can edit their own recipes directly from the recipe detail page. After making edits, a success toast notification appears to confirm that the recipe has been updated.
   - **Delete:** Users can delete their own recipes securely. After deletion, a toast notification pops up confirming that the recipe was removed successfully.
![Edit](static/documentation/readme/crud.jpg)
![Delete](static/documentation/readme/delete.jpg)
![Notification](static/documentation/readme/toast.jpg)                                                                               
- **Responsive Design:**
  - Built using Bootstrap 5: 
    - Ensures consistent layout across mobile, tablet, and desktop:
    - Easy-to-use navbar and components for better UX.

- **Social Media Footer:**
   - **Social Links:**  Icons linking to Facebook, Instagram, X (Twitter), and YouTube.
   - **Accessible:**   All links include aria-labels and rel="noopener" for safe external navigation.
![Footer](static/documentation/readme/footer.jpg)

- **Toast Notifications:**
   -  A position-fixed toast container is included, suggesting support for alert messages like form success, recipe submission confirmation, or profile updates.  
   

## Agile

For the Agile process utilized within Github project board and user stories. Detailing the production process and highlighting issues when they arose. 

### Project Issues

![Issues](static/documentation/readme/issues.jpg)
 

A MOSCOW framework has been utilized. 

**Mo:** Core functionalities like User Authentication, Recipe Management (CRUD), and Recipe Browsing/Search were essential for the app to function. \
**S:** Profile Feature Personalization and Admin Review were implemented to enhance user experience and maintain quality control. \
**Co:** Meal Planning was added as extra features to enrich the platform but were not critical at launch. \
**W:** Advanced features like AI-based recipe recommendations or real-time chat support were considered but intentionally left out for future   versions.                                           


## User Stories

User stories were used to keep track of the MOSCOW framework and project MVP as working through the project. 

![User story](static/documentation/readme/user-stories.jpg)


| **User Story** | **Details** | **Acceptance Criteria** |
|:--------------|:------------|:-------------------------|
| **User Authentication** | Users want to sign up, log in, and update their profile. | 1. Register with email/password<br>2. Redirect on login<br>3. Login with credentials<br>4.Update name and bio |
| **Recipe Management (CRUD)** | Users want to add, edit, delete, and view recipes with title, ingredients, instructions, and image. | 1. Create, edit, delete recipes<br>2.Recipes have title, ingredients, instructions, image<br>3. Users modify only their own recipes |
| **Recipe Search** | Users want to search for recipes by name or ingredients. | 1. Search by keywords<br>2. Display relevant results |
| **Meal Planning** | Users want to plan meals by adding recipes to a monthly planner either for breakfast, lunch or dinner | 1. Add recipes to monthly planner<br>2. Edit/remove meals from planner |
| **Admin Recipe Review** | Admins want to manage users and approve or remove recipes. | 1. Review new recipes<br>2.Remove inappropriate recipes |
| **Comment Moderation** | Admins want to moderate and delete inappropriate comments. | 1. View all comments<br>2.Delete violating comments<br>3. Deleted comments disappear from recipes |
| **Profile Personalization** | Users want to manage profiles. | 1.Create/view/update profile<br>2.Delete profile if desired |
| **AI-Based Recommendations (Future Feature)** | Users want personalized recipe suggestions based on their activity. | 1.Suggest recipes based on user actions<br>2.Update recommendations dynamically<br>3. Add "Recommended for You" section<br>4. Allow opt-in/opt-out |

> ⚠️ **Note on User Story Location**
>  
> Initially, the user story for this project was mistakenly created on a different GitHub repository. After review by my mentor, the error was corrected, and the user story was properly added to the main project repository as a subfolder. This ensures all project documentation is now centralized.
[GitHub Projects](https://github.com/mildred-prog/django-recipe-book)

## Site Testing 

Please see [TESTING.md](TESTING.md) document.

## UX/UI Wireframing

- **Logo and Branding:**
  - The site features a custom-designed logo that combines a **cupcake, a spoon, and a book**, symbolizing the blend of food, creativity, and learning.
  - The text **"Recipe Book"** is stylishly integrated into the logo, custom styled in **purple** to create a warm, inviting, and creative feel.
  - The primary fonts used are **Raleway**, **Roboto**, and **sans-serif**, offering a clean, modern, and readable appearance that complements the casual yet polished theme.

- **Navigation:**
  - The navigation bar is clear and simple, ensuring users can easily move through the site.
  - It includes the following links:
    - **Home**: Takes users to the main landing page.
    - **Recipes**: Displays all available recipes.
    - **New**: Allows users to add a new recipe.
    - **Profile**: Allow users to edit profile and plan meals for the month and display profile details; date joined, number of recipes added,.
    - **Logo**: Placed prominently.
  - The navbar is fully **responsive**, collapsing neatly into a hamburger menu on mobile devices.

- **Hero Section and Welcome Message:**
  - Positioned directly under the navbar is a **hero banner** featuring a welcoming **paragraph**:
    - **"Welcome to Our Recipe Book"**
  - Below the heading is a **short welcoming text** introducing the platform, inviting users to discover, create, and share recipes that align with their lifestyle, tastes, and goals.

- **User Interaction and Feedback:**
  - Users can **register**, **log in**, and **personalize** their profiles.
  - **Toast-style pop-up notifications** appear to confirm successful actions like adding, editing, or deleting a recipe, enhancing user feedback.
  - Only authenticated users can modify their own recipes, ensuring privacy and control.

- **Design and Visual Style:**
  - The color palette centers around **shades of purple** with clean, light backgrounds to maintain an inviting and appetizing atmosphere.
  - **Custom CSS** works alongside **Bootstrap 5** to ensure responsiveness and beautiful, consistent styling across all devices.
  - Design elements include rounded buttons, soft shadows, and spacious forms for improved usability.

- **Search and Recipe Management:**
  - A **search bar** allows users to find recipes by keywords such as title or ingredient.
  - Recipes are presented with featured images, ingredients, and clear cooking instructions to enhance readability.

 - **Social media icons** (Instagram, Twitter) are featured in the footer, encouraging users to stay connected with the Recipe Book community.
  
 - **Error Pages:**

  - Redirects users to an error page template set up for relevant error type, and prompts users to return to the home page with 'Go Back to Home' button.

  ![Error Message Page](static/documentation/readme/error-404.jpg) 

- **Future Engagement:**
  - Future upgrades include **AI-powered personalized recipe suggestions**, offering smarter recommendations based on user activity.


### Wireframe

![Wireframe Desktop Home](static/documentation/readme/desktop-home.png)
![Wireframe Mobile Home](static/documentation/readme/mobile-home.png)


![Wireframe Recipe Desktop](static/documentation/readme/desktop-recipe.png)
![Wireframe Recipe Mobile](static/documentation/readme/mobile-recipe.png)


![Wireframe Profile Desktop](static/documentation/readme/desktop-profile.png)
![Wireframe Profile Page](static/documentation/readme/mobile-profile.png)

### UI Color Palette

Purple (#a048a8): This rich, warm hue infuses the app with a cozy and inviting atmosphere, making users feel at home as they explore and create recipes.​

Background (#3f006a0f): A subtle, translucent shade that provides a gentle backdrop, allowing recipe images and content to stand out without distraction.​

Black (#000000): Utilized for primary text and icons, this classic color ensures readability and a sleek, modern aesthetic throughout the app.​


Off-White (#f6f6f6): Serving as a soft contrast to the darker elements, this color is used for secondary backgrounds and sections, contributing to a clean and organized layout.​

White (#ffffff): Employed for main content areas and text, this crisp color enhances clarity and provides a fresh, uncluttered look.

---

###  User Experience

#### **User Feedback**

Once all styling and error handling were completed, the site was deployed and shared via a live URL with a small test group. The goal was to gather useful insights on navigation, layout, and any functional issues encountered while interacting with the app.

Participants were asked to:
- [x] Register a new account  
- [x] Log out and log in again  
- [x] Create a recipe  
- [x] Edit and delete a recipe  

The following table summarizes the key feedback received, actions taken, and the outcomes:

###  Feedback Summary

The following table summarizes the key feedback received, actions taken, and the outcomes:

| **Feedback**                                        | **Action Taken**                                                   | **Outcome**                                                       |
|----------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Navigation between pages felt slightly delayed     | Optimized route handling and reduced unnecessary reloads           | Navigation became smoother and more responsive                     |
| Form validation wasn't clearly visible             | Added visible error messages and real-time input validation        | Users could identify and fix issues before submission              |
| Recipe edit button was hard to locate              | Moved edit/delete buttons to a more prominent, consistent area     | Users could easily find and use the edit/delete functions          |
| Confusion after submitting forms                   | Implemented toast-style success notifications                      | Users received clear confirmation of successful actions            |
| Meal planner options weren't intuitive             | Improved dropdown menu labels                                      | Users interacted with the planner more confidently                 |
| Profile picture upload returned a 403 error        | Changed `ForeignKey` to `OneToOneField` on the profile model       | Users were able to upload profile pictures without authorization errors |


## Solution Model

This app provides the following core views:

| Route                           | View Function         | Description                                                   | Access         |
|--------------------------------|-----------------------|---------------------------------------------------------------|----------------|
| `/`                             | `home`                | Displays a welcome page with navigation options.              | Public         |
| `/login/`                       | `login_view`          | Displays login form and authenticates users.                  | Public         |
| `/logout/`                      | `logout_view`         | Logs out the current user and redirects to the home page.     | Authenticated  |
| `/recipes/`                     | `recipes`             | Lists all submitted recipes.                                  | Public         |
| `/recipes/add/`                | `add_recipe`          | Allows users to add a new recipe.                             | Authenticated  |
| `/recipes/meal_planner/`       | `monthly_meal_planner`   | Lets users add a meal plan for the month either breakfast,lunch or dinner                     | Authenticated  |
| `/profiles/user/1/`     | `profile`             | Shows user profile with picture, bio, and recent activity.    | Authenticated  |
| `/profiles/edit/`              | `edit_profile`        | Enables users to update their profile details and picture.   | Authenticated  |

### Summary

- **Home View**  
  Renders the homepage and  greets the logged-in user.

- **Recipes View**  
  Displays all public recipes added by users.

- **New Recipe View**  
  Shows a form to add a new recipe (with image upload). Only available to logged-in users.

- **Monthly Meal Plan View**  
  Allows users to submit or update their selected meals for the month..

- **Profile View**  
  Shows detailed user profile with profile picture, bio, and linked recipes or meal plans.

- **Edit Profile View**  
  Handles editing profile info and profile picture upload .

- **Logout View**  
  Ends the user session and redirects to the homepage.


### ERD Design

![ERD Design](static/documentation/readme/erd.png)

I have used `pygraphviz` to auto-generate an ERD.


## Technologies Used

### Languages

__Application Structure__

- **Frontend:**
  - HTML5/CSS3: Provides structure and styling for reviews and user interactions.
  - Bootstrap: Responsive design for easy navigation on various screen sizes.
  - JavaScript: Enhances interactivity (dynamically toggling comments visibility).

- **Backend:**
  - Django Framework (Python): Handles routing, user authentication etc.

### Libraries & Frameworks

- Django v4.2.17
- Django AllAuth v0.57.2
- Django Crispy Forms v2.0
- Crispy Bootstrap5 v0.7
- Django Summernote v0.8.2
- Cloudinary v1.36.0
- Python v3.13.0

### Other Sites

- Testing & Validation
  - HTML: https://validator.w3.org/nu/
  - CSS: https://jigsaw.w3.org/css-validator/#validate_by_uri
  - JavaScript: https://jshint.com/
  - Python: https://pep8ci.herokuapp.com/
  -  [WAVE](https://wave.webaim.org/) to evaluate the accessibility of the site.
 

- Responsive Screen Preview
  -Am I responsive?: https://ui.dev/amiresponsive

- Images downloaded under licensed user
  - Adobe Stock: https://stock.adobe.com/
  - Unsplash:https://unsplash.com/photos/purple-and-white-icing-cake-on-white-ramekin-bowl-l-paVYNvewQ for hero image
  - All recipes images was gotten from -https://unsplash.com/
  - All recipes history, ingredients and instruction was gotten from [ google](https://www.google.com/)
  

- Turning FontAwesome icon into sized favicons
  - Favicon: https://favicon.io/
    
- Image assets reduced with online platforms
  - TinyPNG: https://tinypng.com/

- Assisted problem solving sites:
  - https://docs.djangoproject.com/
  - https://developer.mozilla.org/
  - https://stackoverflow.com/
  - https://www.w3schools.com/
  - https://chatgpt.com/


## Django Project Setup

1. Install Django and supporting libraries: 
   
- ```pip install 'django<4' gunicorn```
- ```pip install dj_database_url psycopg2```
- ```pip install django-cloudinary-storage```  
  
2. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip freeze --local > requirements.txt``` command in the terminal.  
3. Create a new Django project in the terminal ```django-admin startproject main .```
4. Create a new app eg. ```python manage.py startapp profiles```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'reviews',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python manage.py createsuperuser```
7. Migrate the changes with commands: ```python manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<copiedURLfromPostgresSQL>"```
- ```os.environ["SECRET_KEY"]="my_super^secret@key"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:
- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn main.wsgi```
12. Make the necessary migrations again.

## Cloudinary API 

Cloudinary provides a cloud hosting solution for media storage. All users uploaded images in The Recipe_book project are hosted here.

Set up a new account at [Cloudinary](https://cloudinary.com/) and add your Cloudinary API environment variable to your **env.py** and Heroku Config Vars.
In your project workspace: 

- Add Cloudinary libraries to INSTALLED_APPS in settings.py 
- In the order: 
```
   'cloudinary_storage',  
   'django.contrib.staticfiles',  
   'cloudinary',
```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Set Cloudinary as storage for media and static files in settings.py:
- ```STATIC_URL = '/static/'```
```
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌  
  MEDIA_URL = '/media/'  
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## Postgres SQL

A new database instance can be created on [Postgres SQL](https://www.postgresql.org/) for your project. 

- From your user dashboard, retrieve the important 'postgres://....' value. Place the value within your **DATABASE_URL**  in your **env.py** file and follow the below instructions to place it in your Heroku Config Vars.


## Deployment

### Cloning of the Repository Code locally
- The terminal function and template for the deployable application was provided by Code Institute
  - Go to the Github repository that you want to clone
  - Click on the Code button located above all the project files
  - Click on HTTPS and copy the repository link
  - Open the IDE of your choice and paste the copied git url into the IDE terminal
  - The project is now created as a local clone

| **STEPS** | **CODE** | 
| --------- | -------- |
| **In GitHub** |
| Create a new Github Repo | Github > new Repository |
| Open Repo | If your Github is utilising the plugin click 'Open' to launch your preferred IDE |
| **In IDE**|
| Install Django: | pip3 install Django~=4.2.1 |
| Create requirements file | pip3 freeze --local > requirements.txt |
| Create Project | Django-admin startproject recipebook . |
| Run Server | python manage.py runserver |
| Add Servers to ALLOWED_HOSTS in settings.py | ALLOWED_HOSTS = ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com'] |
| Create App (app_name) | python3 manage.py startapp app_name |
| Add to INSTALL_APPS in settings.py | INSTALLED_APPS = [… 'app_name',] |
| **Set Up Heroku** |
| Heroku Dashboard | https://www.heroku.com/ |
| Create new Heroku App | Choose unique name / select close region |
| Add Config Vars | Config Vars > Reveal Config Vars > Add New Key > DISABLE_COLLECTSTATIC value 1 |
| **In IDE** |
| Install web server Gunicorn and freeze | pip3 install gunicorn~=20.1 \ pip3 freeze --local>requirements.txt |
| Create Procfile | create Procfile in root directory |
| Declare Procfile | Add `web : gunicorn main.wsgi` in Procfile |
| **In Heroku** |
| Connect Repository | Navigate to Deploy tab > connect to Github Repo |
| Check Add ons & Dynos | Inside app resources make sure to use Eco Dynos. Delete PostGres DB Add-ons |
| **Database** |
| Create Postgres Database | CI Database Creator - https://dbs.ci-dbs.net/ |
| **In IDE** |
| Install Database Packages | pip3 install dj-database-url~=0.5 psycopg / then pip3 freeze --local > requirements.txt |
| Create env.py file | Root directory add env.py and add to .gitignore |
| **In env.py** |
| import OS | Top line 'import os' |
| set environment variables | os.environ["DATABASE_URL"] = "Paste in PostgreSQL database URL" |
| Secret Key | os.environ["SECRET_KEY"] = "Make up your own randomSecretKey" |
| **In Heroku** | 
| Add Secret Key to Config Vars |  SECRET_KEY, “randomSecretKey” |
| Add a Config Var called DATABASE_URL | DATABASE_URL, 'yourDBUrlGoesHere' |
| **In settings.py** |
| Link to env.py | from pathlib import Path, import os, import dj_database_url, if os.path.isfile("env.py"): import env |
| Remove secret key | SECRET_KEY = os.environ.get('SECRET_KEY') |
 | Comment out old Database section | # DATABASES = { } ( # on each line ) |
| Add new Databases section | DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} |
| **Migrate Database** |
| Save all files and Migrate | python manage.py migrate |
| **Create Super User** |
| Create Super User | python manage.py createsuperuser |
| **In settings.py** |
| Set DEBUG to false | DEBUG = False |
|**Redeploy** |
| Push all Git changes and commits | Redeploy to Heroku |

### Version Control
- The Recipe_book was created using Visual studio code editor and pushed to Github to the remote repository 'recipe_book'
- Git commands were used throughout the development to push the code to the remote repository
- The following git commands were used:
  - git add .  to add the files to the staging area before being committed
  - git commit -m "commit message", to commit changes to the local repository queue that are ready for the final step
  - git push, to push all committed code to the remote repository on Github
  - pip3 install imports, for python library loads
  - add loaded packages to requirements.txt file for Heroku:
    - Run `pip freeze > requirements.txt` in the terminal


## Credits 
- Recipe Images: https://unsplash.com/s/photos/images-of-different-food-from-different-cultures
- Recipe Instructions and Ingredient: https://www.google.com/

- Heroku Deployment steps taken from https://github.com/SchoemanClaudia/TheScoop/blob/main/README.md

## Acknowledgements
- I would like to thank the Code Institute tutor team for their assistance with troubleshooting and debugging some project issues.
  
- I also want to appreciate my Husband for always cheering me up when imposter syndrome was kicking in.
  
- Chrysanthus Obinna for his guidance  https://github.com/chrysanthusobinna
  
- My mentor for reviewing the project and providing feedback.
  
