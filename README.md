
# Wired Out

![Wired Out - Responsive]( 'Shows responsive views of site')

[View the live project here]('Link to deployed site - Wired out')

## Table of contents

- [Wired Out](#wired-out)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [UX](#ux)
    - [User Stories](#user-stories)
      - [Users:](#users)
    - [Development Planes](#development-planes)
    - [Strategy](#strategy)
      - [Scope](#scope)
      - [Structure](#structure)
    - [Skeleton](#skeleton)
      - [Colour Scheme](#colour-scheme)
      - [Logo](#logo)
      - [Typography](#typography)
      - [Imagery](#imagery)
  - [Features](#features)
    - [Design Features](#design-features)
    - [Existing Features](#existing-features)
    - [Features to Implement in the future](#features-to-implement-in-the-future)
  - [Issues and Bugs](#issues-and-bugs)
  - [Technologies](#technologies)
    - [Main Languages Used](#main-languages-used)
    - [Additional Languages Used](#additional-languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Deploying on Heroku](#deploying-on-heroku)
    - [Forking the Repository](#forking-the-repository)
    - [Creating a Clone](#creating-a-clone)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Other](#other)
  - [Acknowledgements](#acknowledgements)

---

## Introduction

This is the fourth of five Portfolio Projects that I must complete during my Full Stack Software Development program with Code Institute.

REST OF INTRODUCTION HERE

[Back to top ⇧](#Wired-Out)

## UX

### User Stories

#### Users:

1. USER STORIES

### Development Planes

To create a comprehensive and appealing website. I Researched other Blog based websites to discover what features and functionality would be required. This information created the above user stories and is developed further below.

### Strategy

Broken into three categories, the website will attempt to focus on the following target audiences:

- **Roles:**
  - User
  - Admin
- **Demographic:**

  - People interested in Coding
  - People looking for a news article styled programming site
  - Beginner's and advanced coders alike

- **Psychographics:**
  - Personality & Attitudes:
    - Educational
      - Interesting
  - Values:
    - Interested in reading about different coding languages
    - Lifestyles:
      - Anyone interested in coding information / Developer tips

The website needs to enable the **user** to:

- browse the articles.
- comment on/like different articles
- register and login to enable them to comment and see their profile

The website need to enable the **admin** to:

- approve article uploads and comments.
- create drafts so they can be completed later.

With the user stories in mind, I created the below strategy table to determine the trade-off of importance and viability with the following results:

![Strategy Table]('Strategy Table')

#### Scope

A scope was defined to identify what needed to be done to align features with the strategy previously defined. This was broken into two categories:

- **Content Requirements**

  - The user will be looking for:
    - A comprehensive list of programming articles.
    - A list of comments so that the can read the conversation about the article / topic / dev tip
    - View the user's profile details

- **Functionality Requirements**
  - The user will be able to:
    - Easily navigate the site to find the information they want.
      - Be able to select articles and such to read
      - Like the different content on the page
      - Be able to edit their profile settings

#### Structure

This information architecture was organized in such a way as to ensure the users can navigate through the site easily.
![Site map structure]('Site Map)

Entity Relationship Diagram for the database models.
![ERD structure]('Entity Relationship DIagram')

### Skeleton

Wireframe mockups were created using [Balsamiq](https://balsamiq.com/ "Balsamiq Website").

Home Page:
![Home Page Wireframe]('Home Page - Wireframe')

About Page:
![About Page Wireframe]('About Page - Wireframe')

Article Details Page:
![Article Details Page Wireframe]('Article Details Page - Wireframe')

Create/Edit Article Page:
![Create/Edit Article Page Wireframe]('Create/Edit Article Page - Wireframe')

Edit Profile Page:
![Edit Profile Page Wireframe]('Edit Profile Page - Wireframe')

#### Colour Scheme

#### Logo

#### Typography

#### Imagery

All of the article images are from [Pixabay](https://pixabay.com/ "Pixabay website").
The header image is from [Unsplash](https://unsplash.com/ "Unsplash website")

[Back to top ⇧](#Wired-Out)

## Features

### Design Features

Each page of the website features a consistent navigational system:

- The **Header** contains a conventionally placed logo in the top left of the page (whereby clicking this will redirect users back to the home page) and a navigation bar also starting on the left after the logo. On smaller screens, the navigation bar condenses into a dropdown with navigation options.

- The **Header Image** on the home page,

- The **Footer** is intentionally

### Existing Features

- **Example Feature** - This is an example explanation of what the feature is

### Features to Implement in the future

- **Favorites Page**
  - **Feature** - This feature would have been used to display all of the articles that a User has liked, so that they could find them more easily.
  - **Reason for not featuring in this release** - The reason for not releasing this feature was that I ran out of time to implement the feature before the project's due date. This will be developed further in the future after grading is complete.
- **Sharing Images in Comments**
  - **Feature** - This feature would have allowed users to upload images in the comment section to make the commenting infrastructure more robust.
  - **Reason for not featuring in this release** - Again, I ran out of time to implement this feature before the project's due date. This will also be developed further in the future after grading is complete.
- **Saving Drafts to a Profile Page**
  - **Feature** - This feature would have allowed users to create a draft of an article which would be saved on a profile page and would allow them to complete the draft at a later date and release the article on to the site.

[Back to top ⇧](#Wired-Out)

## Issues and Bugs

**Bug** -

- **_Solution_**:

**Bug** -

- **_Solution_**:

**Bug** -

- **_Solution_**:

**Issue**

**Issue**

[Back to top ⇧](#Wired-Out)

## Technologies

### Main Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")

### Additional Languages Used

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
  - Used to implement the Summernote feature that allowed the user to add styling to the recipe in the form.
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)> "Link to Python Wiki")
  - Used to implement Django functionality, including building models, forms and views for the app.

### Frameworks, Libraries & Programs Used

- [Django](https://www.djangoproject.com/ "Link to Django Project website")
  - Django was used to build the models, forms and views of the app, and was the backbone of this project.
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page")
  - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [Cloudinary](https://cloudinary.com/ "Link to Cloudinary page")
  - Cloudinary was used as free cloud storage for images uploaded to the site through the recipe forms.
- [Summernote](https://summernote.org "Link to Summernote page")
  - Summernote was used to allow users to add styling when adding a recipe to the site. This is particularly useful for using bullet points for ingredients or numbering the steps for the recipe.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to the Crispy Forms documentation")
  - Crispy Forms was used to style the add and edit recipe forms, allowing more than one field to occupy a line on the form.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
  - Google fonts were used to import the fonts "INSERT FONT HERE" and "INSERT FONT HERE" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
  - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [Git](https://git-scm.com/ "Link to Git homepage")
  - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
  - GitHub was used to store the project after pushing
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
  - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.

[Back to top ⇧](#Wired-Out)

## Testing

Testing information can be found in a seperate [ testing file](TESTING.md "Link to testing file").

## Deployment

This project was developed using a [GitPod](https://gitpod.io/ "Link to GitPod") workspace. The code was commited to [Git](https://git-scm.com/ "Link to Git") and pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

### Deploying on Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:

   - Select "Create new app" in Heroku.
   - Choose a name for your app and select the location.

2. Attach the Postgres database:

   - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:

   - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
   - In your GitPod workspace, create an env.py file in the main directory.
   - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
   - Add the SECRET_KEY value to the Config Vars in Heroku.
   - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
   - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
   - In settings.py add the following sections:
     - Cloudinary to the INSTALLED_APPS list
     - STATICFILE_STORAGE
     - STATICFILES_DIRS
     - STATIC_ROOT
     - MEDIA_URL
     - DEFAULT_FILE_STORAGE
     - TEMPLATES_DIR
     - Update DIRS in TEMPLATES with TEMPLATES_DIR
     - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
   - Create three directories in the main directory; media, storage and templates.
   - Create a file named "Procfile" in the main directory and add the following:
     - web: gunicorn project-name.wsgi
   - Log in to Heroku using the terminal heroku login -i.
   - Then run the following command: **heroku git:remote -a your_app_name_here** and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
   - After linking your app to your workspace, you can then deploy new versions of the app by running the command **git push heroku main** and your app will be deployed to Heroku.

### Forking the Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://INSERTGITHUBREPO "Link to GitHub Repo").
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

### Creating a Clone

How to run this project locally:

1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
4. Locate the [GitHub Repository](https://INSERTGITHUBREPO "Link to GitHub Repo").
5. Click the green "GitPod" button in the top right corner of the repository.
   This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://INSERTGITHUBREPO "Link to GitHub Repo").
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.

```
git clone https://github.com/USERNAME/REPOSITORY
```

8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Link to GitHub troubleshooting")

[Back to top ⇧](#Wired-Out)

## Credits

Boutique ado, Dennis Ivy, Tutors, ETC ETC ETC

### Content

Most article's were acquired from ETC ETC ETC

### Media

- The images have been sourced from [Pixabay](https://pixabay.com/) and [Unsplash](https://unsplash.com).

### Code

References used:

- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [Colorlib](https://colorlib.com/ "Link to Colorlib page")
- [Django Docs](https://docs.djangoproject.com/en/3.2/ "Link to Django's Docs for Version 3.2")
- [Summernote GitHub Docs](https://github.com/summernote/summernote, "Link to Summernote's GitHub page")
- [Cripsy Forms Docs](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to Crispy Forms documentation")

### Other

- [Visio](https://www.microsoft.com/en-gb/microsoft-365/visio/flowchart-software "Link to Visio on Microsoft's website")
  - Visio was used for the diagrams in this Readme document

[Back to top ⇧](#Wired-Out)

## Acknowledgements

- I would like to thank ETC ETC ETC

[Back to top ⇧](#Wired-Out)

---

