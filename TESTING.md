# Testing

Testing file for Recipe Book [README.md](README.md).

## Testing User Stories

### Developer Stories

- [x] Frontend and Backend of the project created.
- [x] Database is connected to the project.
- [x] App deployed on Heroku.

### User Stories

- [x] User Authentication	
- [x] Recipe Management
- [x] Recipe Browsing and Search
- [x] Admin Review
- [x] Meal Planning
- [x] To Moderate Comment
- [x] Profile Feature Personalization
- [x] Data Base Design with ERD	
- Advanced features like AI-based recipe
  

## Validation

### Validation Errors



### HTML Validation Corrected

- [x] HTML validation all passed:

**Home page**  
![Home Page HTML Validation](static/documentation/testing/home-html.jpg)

**Recipes Page**  
![Recipe Post Page HTML Validation](static/documentation/testing/addrecipe-html.jpg)

**Recipes Add Page**  
![Recipe Add Page HTML Validation](static/documentation/testing/addrecipe-html.jpg)

**Profile Page**  
![Profile Page HTML Validation](static/documentation/testing/profile-html.jpg)

**Edit Profile Page**  
![Edit Profile Page HTML Validation](static/documentation/testing/edit-profile-html.jpg)

**Menu Planner Page**  
![Menu Planner Page HTML Validation](static/documentation/testing/menu-planner-html.jpg)

**Login Page**  
![Login Page HTML Validation](static/documentation/testing/login-html.jpg)

**Logout Page**  
![Logout Page HTML Validation](static/documentation/testing/logout-html.jpg)


### CSS Validation Corrected
![The Page CSS Validation](static/documentation/testing/css-validator.jpg)

### JSHint

- [x] JavaScript tests all passed.

![JSHint](static/documentation/testing/jshint.jpg)

### CI Python Linter

- [x] Python tests all passed.

- [x] Recipes:
![forms](static/documentation/testing/recipe-forms.jpg)
![models](static/documentation/testing/recipe-models.jpg)
![views](static/documentation/testing/recipes-views.jpg)

- [x] Profile:
![forms](static/documentation/testing/profile-forms.jpg)
![models](static/documentation/testing/profile-models.jpg)
![views](static/documentation/testing/profile-views.jpg)

- [x] Menu-planner:
![models](static/documentation/testing/menu-models.jpg)
![views](static/documentation/testing/menu-views.jpg)


    All Python files containing the project's code have been tested. 
    All the errors were fixed, and after running the CI Python Linter, it shows there are no errors.

| **Feature**     | **admin.py** | **apps.py** | **forms.py** | **models.py** | **urls.py** | **views.py** |
|-----------------|:------------:|:-----------:|:------------:|:-------------:|:-----------:|:------------:|
| Recipes         | no errors    | no errors   | no errors    | no errors     | no errors   | no errors    |
| Profile         | no errors    | no errors   | no errors    | no errors     | no errors   | no errors    |
| Meal-planner    | no errors    | no errors   | no errors    | no errors     | no errors   | no errors    |


## Lighthouse Test

- [x] Mobile view:

    **Home**  
    ![Lighthouse Home](static/documentation/testing/lh-home.jpg)

    **Recipes Page**  
    ![Lighthouse Report Recipes](static/documentation/testing/lh-recipes.jpg)
    
    **Add Recipes Page**  
    ![Lighthouse Report Add Recipes](static/documentation/testing/lh-add-recipes.jpg)

    **Profile Page**  
    ![Lighthouse Report Profile](static/documentation/testing/lh-profile.jpg)

    **Menu Planner Page**  
    ![Lighthouse Report Menu Planner](static/documentation/testing/lh-menu-plan.jpg)

    **Log-in page**  
    ![Lighthouse Report Sign-In Page](static/documentation/testing/lh-login.jpg)

    **Logout Page**  
    ![Lighthouse Report Logout](static/documentation/testing/lh-logout.jpg)


- [x] Desktop view:  
  
     **Home Page**  
    ![Lighthouse Home](static/documentation/testing/desk-lh-home.jpg)

    **Recipes Page**  
    ![Lighthouse Report Recipes](static/documentation/testing/desk-lh-recipes.jpg)
    
    **Add Recipes Page**  
    ![Lighthouse Report Add Recipes](static/documentation/testing/desk-lh-add-recipes.jpg)

    **Profile Page**  
    ![Lighthouse Report Profile](static/documentation/testing/desk-lh-profile.jpg)

    **Menu Planning Page**  
    ![Lighthouse Report Profile](static/documentation/testing/desk-lh-menu-plan.jpg)

    **log-in page**  
    ![Lighthouse Report Sign-In Page](static/documentation/testing/desk-lh-login.jpg)

    **Logout Page**  
    ![Lighthouse Report Logout](static/documentation/testing/desk-lh-logout.jpg)


 ## Manual Testing

### User Input / Form Validation

Testing was carried out on desktop using a Chrome browser to ensure all forms take the intended input and process the input appropriately.
Manual testing by checking the following:

### Navigation Testing

| Test Case | Test Steps | Expected Result | Pass/Fail |
|-----------|------------|-----------------|-----------|
| Home Button Navigation | 1. Click on the home button | User is redirected to the home page |Pass |
| Recipe Button Navigation | 1. Click on the recipe button | All recipes are displayed on the page |Pass |
| New Recipe Navigation | 1. Click on the "New" button | User is directed to the recipe creation form |Pass |
| Profile Navigation | 1. Click on the profile button | User is taken to their profile page |Pass |
| Meals Navigation | 1. Click on the meals button | User is directed to the monthly meal planner |Pass |
| Login Navigation | 1. Click on the login button | User is directed to the sign-up/login page |Pass |

### Recipe Management Testing

| Test Case | Test Steps | Expected Result | Pass/Fail |
|-----------|------------|-----------------|-----------|
| Recipe Display | 1. Click on any recipe | Recipe details (instructions, image, calories, cuisine) are displayed |Pass |
| Create New Recipe | 1. Fill out the recipe form<br>2. Click the create button | New recipe is created and added to the recipe list |Pass |
| Edit Recipe | 1. Click the edit button on a recipe<br>2. Make changes<br>3. Save changes | 1. Edit form opens<br>2. Changes are saved<br>3. Success notification appears |Pass |
| Delete Recipe | 1. Click the delete button on a recipe<br>2. Confirm deletion | 1. Confirmation dialog appears<br>2. Recipe is deleted<br>3. Success notification appears |Pass |

### Profile Management Testing

| Test Case | Test Steps | Expected Result | Pass/Fail |
|-----------|------------|-----------------|-----------|
| Edit Profile | 1. Click on edit profile<br>2. Update profile information<br>3. Save changes | Profile information is updated successfully |Pass |

### Meal Planning Testing

| Test Case | Test Steps | Expected Result | Pass/Fail |
|-----------|------------|-----------------|-----------|
| Meal Type Selection | 1. Click on dropdown menu<br>2. Select meal type (breakfast/lunch/dinner) | Selected meal type is displayed for planning |Pass |
| Update Meal Plan | 1. Select meal type<br>2. Choose recipe<br>3. Save plan | Meal plan is updated for the selected period |Pass |

### Search Functionality Testing

| Test Case | Test Steps | Expected Result | Pass/Fail |
|-----------|------------|-----------------|-----------|
| Recipe Search | 1. Enter search term in search bar<br>2. Press enter or click search | Relevant recipes are displayed based on search term |Pass |

### Social Media Integration Testing

| Test Case | Test Steps | Expected Result | Pass/Fail |
|-----------|------------|-----------------|-----------|
| Footer Links | 1. Click on any social media link in footer | User is redirected to the respective social media platform |Pass |
    

## Bug Documentation

| Bug Description | Error Message/Behavior | Solution | Root Cause | Prevention Tips |
|----------------|----------------------|----------|------------|----------------|
| Form Validation Issues | Missing required fields not caught | Added comprehensive form validation in RecipeForm | Missing client-side validation | Implement both client and server-side validation |
| Image Upload Issues | "Invalid image format" error | Implemented ResizedImageField with WEBP format | Unsupported image formats | Use proper image field with format validation |
| Search Functionality | Incomplete search results | Fixed Q object queries in Recipes view | Incorrect query conditions | Test search functionality with various inputs |
| Meal Planner Logic | Null calories handling | Added default calories value (9999) | Null value conversion error | Add proper null checks and defaults |
| User Authentication | Unauthorized recipe edits | Added UserPassesTestMixin | Missing permission checks | Implement proper authentication checks |
| Rich Text Editor | Summernote initialization errors | Added proper initialization in profile.js | Missing editor initialization | Ensure proper script loading order |
| Database Queries | Slow recipe loading | Added proper indexing and ordering | Missing database optimization | Use proper database indexing |
| Form Error Display | Error messages not showing | Added error message display in templates | Missing error template handling | Implement proper error message display |
| Image Alt Text | Missing alt text validation | Added required alt text field | Missing accessibility features | Always require alt text for images |
| Recipe Deletion | Cascade delete issues | Fixed foreign key relationships | Improper model relationships | Use proper cascade delete settings |

