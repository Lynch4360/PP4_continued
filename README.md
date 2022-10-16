
# Wired Out

![Wired Out - Responsive](AM I RESPONSIVE IMAGE HERE FROM INSIDE STATIC FOLDER)

[View the live project here](LINK TO DEPLOYED SITE HEROKU.APP)

## Version Control

Github was used to track the progress of this project. Commits were a little all over the place because of the gap between first handing in the project and resubmitting was quite great, but I tried my best to segment differant pieces of work on the project to different commits.

## Introduction

This is the fourth of five Portfolio Projects that I must complete during my Full Stack Software Development program with Code Institute.

This project was created entirely for educational purposes. This blog is about educational Coding articles and news, the name 'Wired Out' playing on a scene from [The Social Network](https://en.wikipedia.org/wiki/The_Social_Network)

[Back to top ⇧](#Wired-Out)

To create a comprehensive and appealing website. I Researched other Blog based websites to discover what features and functionality would be required. This information created the above user stories and is developed further below.

### User stories
User stories were created and managed via github
LIST OF ALL THE USER STORIES

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
  - Home: the landing page of the site, containing the list of posts/articles that have been written by the authors on the site and approved by an admin.
  - Post Detail: The page that contains the content of a post so that a user can read it fully. Each post is available to comment on, flag as liked to show approval or bookmark so that a user can save the post to read at a later time. These features are fully authenticated so are only available if a user is registered and is currently logged in.
  
  
  - Entity Relationship Diagram for the database models.
    [ERD structure](INSERT ERD DIAGRAM IMAGE HERE FROM STATIC/MEDIA)

### Skeleton
#### Wireframes

The final result is slightly different as during the development stage the way htings were displayed was not as user friendly as expected and I decided to be more minimalistic and focus on the scope of the Assesment Criteria.

* [Homepage - Large Screen](SAVED IMAGE OF THE HOMEPAGE WIREFRAME STORED IN STATIC/MEDIA)
* [Homepage - Medium Screen](SAVED IMAGE OF THE HOMEPAGE WIREFRAME STORED IN STATIC/MEDIA)
* [Homepage - Small Screen](SAVED IMAGE OF THE HOMEPAGE WIREFRAME STORED IN STATIC/ME
* [Account Page - Large Screen](SAVED IMAGE OF THE ACCOUNT WIREFRAME STORED IN STATIC/MEDIA)
* [Account Page - Medium Screen](SAVED IMAGE OF THE ACDCOUNT WIREFRAME STORED IN STATIC/MEDIA)
* [Account Page - Small Screen](SAVED IMAGE OF THE ACCOUNT WIREFRAME STORED IN STATIC/MEDIA)
* [Post details Page - Large Screen](SAVED IMAGE )
* [Post details Page - Medium Screen](SAVED IMAGE )
* [Post details Page - Small Screen](SAVED IMAGE )

#### Colour Scheme

The Color scheme is a variationn of the [Discord Desktop app](https://discord.com/), I used PowerToys, which I mainly use to partition my windows but they also have a color picker tool. I then saved these Hex codes and added them as CSS variables so that they could be easily interchanged if I decided to use a different theme. 

This display screenshot was taken from HTML Colours. [Color Scheme Image](https://github.com/Lynch4360/PP4_continued/blob/main/static/media/color_scheme.png)

#### Logo

The Logo was created by using [Canva](https://www.canva.com/), I was going to make a Logo Icon for smaller screen sizes but decided against it, beleiving that a more uniform look was more professional.

[Logo Image](https://github.com/Lynch4360/PP4_continued/blob/main/static/media/logo.png)

[Back to top ⇧](#Wired-Out)


## Features

Navigation bar
Home Page Post List
Post details page
About Page
Register, Log in, Log out pages
Commenting on post
Liking a post
Adding a post to favouites

### Features to Implement in the future

- **404 Page**
  - A modified 404 page to suit the style of the website.
  - 
- **500 Page**
  - A modified 500 page to suit the style of the website.

- **Sharing Images in Comments**
  - This feature would have allowed users to upload images in the comment section to make the commenting infrastructure more robust.

- **Saving Drafts to a Profile Page**
  - This feature would have allowed users to create a draft of an article which would be saved on a profile page and would allow them to complete the draft at a later date and release the article on to the site.
- **Merchandise Store**
  - I would link to add an online e-commerce  element to the current app to sell merchandise like Cups and hats branded like the blog.

[Back to top ⇧](#Wired-Out)

## Data Models
* ### PostList
* ### Comment

## Issues and Bugs

**Bug** -

- **_Solution_**:



[Back to top ⇧](#Wired-Out)

## Technologies

### Main Languages Used

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)> "Link to Python Wiki")
  - Used to implement Django functionality, including building models, forms and views for the app.
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")

### Additional Languages Used

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
  - Used to implement the Summernote feature that allowed the user to add styling to the recipe in the form.

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

### Media Credits
- Blog posts images were found on [The Conversation](https://theconversation.com/)
- Default placeholder image for a blog post was taken from Code Institute's "I think therefore I blog" tutorial series
- Logo was created by using [Canva](https://www.canva.com/)
- Icons were gotten from [Flaticon](https://www.flaticon.com/)
- Coulor Pallette was created using [HTML Colours](https://htmlcolors.com/create-palette)

### Content Credits
- Most of my content for the blog posts and information found on the site were found on [The Conversation](https://theconversation.com/europe/topics/coding-5877)
  
### Code Credits
- Overall concept was developed by using Code Institute tutorials and other tutorials by [Very Academy](https://www.youtube.com/c/veryacademy)
  
  #### References used:

- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [Colorlib](https://colorlib.com/ "Link to Colorlib page")
- [Django Docs](https://docs.djangoproject.com/en/3.2/ "Link to Django's Docs for Version 3.2")
- [Summernote GitHub Docs](https://github.com/summernote/summernote, "Link to Summernote's GitHub page")
- [Cripsy Forms Docs](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to Crispy Forms documentation")
  
### Other Credits
- The Diagram's in this Project were created using [diagrams.net](https://app.diagrams.net/)
## Acknowledgements

- I had lots of help from Malia my mentor making sure there were no glaring issues with my code and that my documentation was up to scratch.

[Back to top ⇧](#Wired-Out)

---

