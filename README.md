# Book a skydive

The live link can be found here: [Live Site - Book a skydive]()

## Table of Contents
- [User-Experience-Design](#user-experience-design)
  - [The-Strategy-Plane](#the-strategy-plane)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The-Scope-Plane](#the-scope-plane)
  - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The-Skeleton-Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plane](#the-surface-plane)
    - [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Technolgies](#technolgies)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
    - [Run Locally](#run-locally)
    - [Fork Project](#fork-project)
  - [Credits](#credits)

# User-Experience-Design

## The-Strategy-Plane
### Site-Goals
### Agile Planning
#### Epics
#### User Stories

## The-Scope-Plane

* CRUD functionality on Bookings and Plane departures
* Restricted role based features
* Home page with site information
* Responsive Design - Devices 320px and up
* Hamburger menu for mobile devices

## The-Structure-Plane
### Features

**Navigation Menu**

![Navigation Menu](docs/components-and-pages/navigation-menu.png)

**Home Page**

![Home](docs/components-and-pages/home.png)

**Tandem Page**

![Tandem Page](docs/components-and-pages/tandem.png)

- Tandem choose Time slot

![Tandem Choose Time Slow](docs/components-and-pages/tandem-time.png)

- Tandem Booking Form

![Tandem Booking Form](docs/components-and-pages/tandem-booking-form.png)

**Courses Page**

![Courses Page](docs/components-and-pages/courses.png)

- Courses Booking Form

![Courses booking form](docs/components-and-pages/courses-booking-form.png)

**Experienced Page**

![Experienced page](docs/components-and-pages/experienced.png)

- Plane Details

![Plane details page](docs/components-and-pages/plane-details.png)

- Experienced Booking Form

![Experienced Booking Form](docs/components-and-pages/experienced-booking-form.png)

**Authentication pages**

![Login](docs/components-and-pages/log-in.png)

![Logout](docs/components-and-pages/log-out.png)

![Register](docs/components-and-pages/register.png)

**Footer**


### Features Left To Implement
- In the future releases i'd like to add more business logic for smoother user experience when using as the admin or manager. This would include things like not allowing experienced jumpers to cancel there booking less than 20 mins before take off. Also a ticket system where the user would have to buy tickets in order to book a slot on a plane.

## The-Skeletons-Plane
### Wireframes
**Home**

![Home Page](docs/wireframes/home-wireframe.png)

**Courses**

![Courses Page](docs/wireframes/courses-wireframe.png)

**Tandems**

![Tandems Page](docs/wireframes/tandems-wireframe.png)

**Experienced**

![Experienced Page](docs/wireframes/experienced-wireframes.png)

**Plane details**

![Plane Detail Page](docs/wireframes/plane-details-wireframe.png)

**Booking Form**

![Booking Form Page](docs/wireframes/booking-form-wireframe.png)

**Login**

![Login Page](docs/wireframes/login-wireframe.png)

**Register**

![Register Page](docs/wireframes/register-wireframe.png)

**Logout**

![Logout Page](docs/wireframes/logout-wireframe.png)

### Database-Design

### Security

Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, api keys or sensitive information was added the the repository. In production, these variables were added to the heroku config vars within the project.

## The-Surface-Plane
### Colour-Scheme
### Typography
### Imagery

The website logo was created with CoPilot through trial and error in giving commands for the design.

The rest of the images of skydivers were taken by me in my training to become a camera flyer for a local dropzone.

## Technologies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to set the correct url to delete booking 
- Python
  - Python was the main programming language used for the application using the Django Framework.
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#
- cloudConvert
  - This was used to compress the images for optimal load times

**Python Modules Used**

**External Python Modules**

## Testing

Test cases and results can be found in the [TESTING.md](TESTING.md) file. This was moved due to the size of the file.

## Deployment

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘book-a-skydive’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site]()

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

## Credits

[Bootstrap](https://getbootstrap.com/docs/5.2/components/buttons/#examples)

[AllAuth](https://docs.allauth.org/en/latest/installation/quickstart.html)

[Font Awesome](https://fontawesome.com/)

[Django Design Philosophies](https://docs.djangoproject.com/en/4.2/misc/design-philosophies/)