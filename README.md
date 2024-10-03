# Book a skydive

Book a skydive is a fictional Skydiving Dropzone company. The app is a management system for the dropzone allowing them to control the available courses and time slots. It also provides customers with a simple booking system where the experienced jumpers can view and manage bookings. The other customers booking tandems and courses may only create a booking.  
The live link can be found here: [Live Site - Book a skydive](https://book-a-skydive-3bb0c8212a26.herokuapp.com/)

## Table of Contents
- [User-Experience-Design](#user-experience-design)
  - [The-Strategy-Plane](#the-strategy-plane)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The-Scope-Plane](#the-scope-plane)
  - [The-Skeleton-Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
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
The site will allow the dropzone to easily manage the available courses, tandems and plane departures (for experienced jumpers) through the admin user interface.

The site will also provide a platform for experienced skydivers where after creating an account they can book a slot on a plane and then view/manage that booking either from the plane details page or within the profile area.

Also a customer with an account will be able to book a course or tandem and view/manage from the profile area

### Agile Planning

Agile planning for the "Book a Skydive" project was organized into two sprints, each defined by milestones within GitHub. The first sprint focused on backend development, while the second sprint concentrated on frontend development.

#### Epics

Epics are large bodies of work that can be broken down into smaller tasks or user stories. For this project, the following epics were created for each sprint:

### Agile Planning

Agile planning for the "Book a Skydive" project was organized into two sprints, each defined by milestones within GitHub. The first sprint focused on backend development, while the second sprint concentrated on frontend development.

#### Epics

Epics are large bodies of work that can be broken down into smaller tasks or user stories. For this project, the following epics were created for each sprint:

1. **Sprint 1: Backend Development**
   - **Logged in user can book, update, delete bookings**: Implement the functionality for users to manage their bookings by creating, updating, or deleting entries in the database.
   - **Admin can access and edit all models**: Implement an admin panel that allows administrators to view and modify all data models, including users, bookings, courses, and plane schedules.
   - **Implement user login authentication**: Set up secure user authentication, allowing users to log in, log out, and manage their sessions effectively.

2. **Sprint 2: Frontend Development**
   - **User Authentication**: Design and implement the frontend interfaces for user registration and login, ensuring a seamless user experience.
   - **Experienced app area designs**: Create intuitive layouts for experienced jumpers, including booking forms and dashboards to view flight information and past bookings.
   - **Courses and tandems areas**: Develop user-friendly pages for booking tandem jumps and courses, ensuring all necessary information is captured efficiently.
   - **General frontend designs**: Ensure a cohesive design across the application by applying consistent styling, responsive layouts, and accessible navigation elements.


#### User Stories

User stories are smaller, manageable tasks derived from the epics. They define specific requirements from the perspective of the end user. Below are examples of user stories for each epic:

**Epic 1: Logged in user can book, update, delete bookings**
Experienced skydiver can Book a plane

Experienced skydiver can Delete a booking

Experienced skydiver can Edit a booking

Booking a skydive course 

Editing a skydive course booking

Deleting a skydive course booking

Book a tandem skydive

Editing a tandem skydive booking

Deleting a tandem skydive booking

**Epic 2: Admin can access and edit all models**
Admin can manage all plane departure

Admin can manage Course and tandem dates

**Epic 3: Implement user login authentication**
Account registration

User can login

**Epic 4: User Authentication**
Design the registration page

Design the login page

**Epic 5: Experienced app area designs**
View paginated list of plane departures

Design the booking form for experienced app

Design the experienced home page

**Epic 6: Courses and tandems areas**
Design the tandem booking page

Design the frontend book a course page

Design the booking form in order to book a tandem

Design the form page for booking a course

**Epic 7: General frontend designs**
Design the home page 

Design the navigation bar

Design the footer

## The-Scope-Plane

* CRUD functionality on Bookings and Plane departures
* Restricted role based features
* Home page with site information
* Responsive Design - Devices 320px and up
* Hamburger menu for mobile devices

## The-Skeleton-Plane
### Wireframes
<details>
<summary>Home</summary>

![Home Page](docs/wireframes/home-wireframe.png)

</details>

<details>
<summary>Courses</summary>

![Courses Page](docs/wireframes/courses-wireframe.png)

</details>

<details>
<summary>Tandems</summary>

![Tandems Page](docs/wireframes/tandems-wireframe.png)

</details>

<details>
<summary>Experienced</summary>

![Experienced Wireframes](docs/wireframes/experienced-wireframes.png)

</details>

<details>
<details>
<summary>Profile</summary>

![Profile Page](docs/wireframes/profile-wireframe.png)

</details>
<summary>Plane Details</summary>

![Plane Detail Page](docs/wireframes/plane-details-wireframe.png)

</details>

<details>
<summary>Booking Form</summary>

![Booking Form Page](docs/wireframes/booking-form-wireframe.png)

</details>

<details>
<summary>Login</summary>

![Login Page](docs/wireframes/login-wireframe.png)

</details>

<details>
<summary>Register</summary>

![Register Page](docs/wireframes/register-wireframe.png)

</details>

<details>
<summary>Logout</summary>

![Logout Page](docs/wireframes/logout-wireframe.png)

</details>

### Database-Design
The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is at the heart of the application as it is connected the the main booking and menu tables, linked by primary/foreign key relationships.

The experienced model (JumpSlot) holes users currently booked on that jump by a many to many relationship, this allows a number of users to appear on the same JumpSlot. Whereas Jump booking is specific to the user and has a foreign key to state which JumpSlot the user has booked.

The TandemsDay model sets dates on which a tandem jump can be available on. 
While Tandem Timeslot will add a number of time slots throughout the day, a maximum of 6 tandems can be booked per time slot, this is affected when a VisitorDetails table is created for that time slot.

<details>
<summary>Database diagram</summary>

![Database diagram](docs/database-diagram.png)

</details>


### Security

The "Book a Skydive" application employs several security measures to protect user data and ensure safe interactions. 

User authentication is enforced through Django’s built-in authentication system, requiring users to log in before accessing critical features like booking management. Sensitive information, such as passwords and API keys, is securely stored using environment variables and not hard-coded into the source code. Additionally, role-based access controls prevent unauthorized users from accessing or modifying data, while the messages framework provides user feedback for actions related to permissions and errors, enhancing overall security and user experience.

## The-Structure-Plane
### Features

<details>
<summary>Navigation Menu</summary>

![Navigation Menu](docs/components-and-pages/navigation-menu.png)

</details>

<details>
<summary>Home Page</summary>

![Home](docs/components-and-pages/home.png)

</details>

<details>
<summary>Tandem Page</summary>

![Tandem Page](docs/components-and-pages/tandem.png)

- Tandem choose Time slot

<details>
<summary>Tandem Choose Time Slot</summary>

![Tandem Choose Time Slow](docs/components-and-pages/tandem-time.png)

</details>

- Tandem Booking Form

<details>
<summary>Tandem Booking Form</summary>

![Tandem Booking Form](docs/components-and-pages/tandem-booking-form.png)

</details>

</details>

<details>
<summary>Courses Page</summary>

![Courses Page](docs/components-and-pages/courses.png)

- Courses Booking Form

<details>
<summary>Courses Booking Form</summary>

![Courses booking form](docs/components-and-pages/courses-booking-form.png)

</details>

</details>

<details>
<summary>Experienced Page</summary>

![Experienced page](docs/components-and-pages/experienced.png)

- Plane Details

<details>
<summary>Plane Details Page</summary>

![Plane details page](docs/components-and-pages/plane-details.png)

</details>

- Experienced Booking Form

<details>
<summary>Experienced Booking Form</summary>

![Experienced Booking Form](docs/components-and-pages/experienced-booking-form.png)

</details>

</details>

<details>
<summary>Authentication Pages</summary>

![Login](docs/components-and-pages/log-in.png)

![Logout](docs/components-and-pages/log-out.png)

![Register](docs/components-and-pages/register.png)

</details>

### Features Left To Implement
- In the future releases, I'd like to add more business logic for smoother user experience when using as the admin or manager. This would include things like not allowing experienced jumpers to cancel their booking less than 20 mins before take off. Also a ticket system where the user would have to buy tickets in order to book a slot on a plane.

## The-Surface-Plane
### Colour-Scheme

Two complementing colors helped to bring the right vibe to the website , i believe it looks inviting and lively. 

#0d6efd

![Blue color used](docs/blue.png)


#dc1c84

![Pink color used](docs/pink.png)

### Typography

The "Book a Skydive" application utilizes the default Bootstrap typography to achieve a clean and professional look. Bootstrap's typography settings provide a well-structured and responsive font system that enhances readability across devices. By incorporating a font stack of `Helvetica Neue`, `Helvetica`, `Arial`, and sans-serif, the application ensures a modern aesthetic. The use of predefined font sizes and weights for headings and body text creates a consistent visual hierarchy, making it easy for users to navigate and absorb content. This choice of typography not only improves the overall user experience but also aligns with best practices in web design.

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

* Django Class based views (ListView) - Used for the classes
* Mixins (LoginRequiredMixin) - Used to enforce login required on classes

**External Python Modules**

* crispy-bootstrap5==0.6 - This was used to allow bootstrap5 use with crispy forms
* cryptography==37.0.2 - Installed as dependency with another package
* defusedxml==0.7.1 - Installed as dependency with another package
* dj-database-url==0.5.0 - Used to parse database url for production environment
* dj3-cloudinary-storage==0.0.6 - Storage system to work with cloudinary
* Django==4.0.5 - Framework used to build the application
* django-allauth==0.51.0 - Used for the sites authentication system, sign up, sign in, logout.
* django-crispy-forms==1.14.0 - Used to style the forms on render
* django-model-utils==4.2.0 - Installed as dependency with another package
* gunicorn==20.1.0 - Installed as dependency with another package
* idna==3.3 - Installed as dependency with another package
* oauthlib==3.2.0 - Installed as dependency with another package
* psycopg2==2.9.3 - Needed for heroku deployment
* pycparser==2.21 - Installed as dependency with another package
* PyJWT==2.4.0 - Installed as dependency with another package
* python3-openid==3.2.0 - Installed as dependency with another package
* requests==2.27.1 - Installed as dependency with another package
* requests-oauthlib==1.3.1 - Installed as dependency with another package (allauth authentication)
* six==1.16.0 - Installed as dependency with another package
* sqlparse==0.4.2 - Installed as dependency with another package
* tzdata==2022.1 - Installed as dependency with another package
* urllib3==1.26.9 - Installed as dependency with another package
* whitenoise==6.2.0 - Used to serve static files directly without use of static resource provider like cloundinary

## Testing

### Functional testing
### Unit testing
### Accessibility 
### Validator testing
**w3 HTML Validator**
All pages were run through the w3 HTML Validator. All of these issues were corrected and all pages passed validation.

Due to the django templating language code used in the HTML files, these could not be copy and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.

**Pep8**
All pages were run through the official Pep8 validator to ensure all code was pep8 compliant. Some errors were shown due to blank spacing and lines too long, 1 line instead of 2 expected. All of these errors were resolved and code passed through validators with the exception of the settings.py file.

**JSHINT**
JavaScript code was run through JSHINT javascript validator. 

### Lighthouse report

### Responsiveness


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

The live link can be found here: [Live Site](https://book-a-skydive-3bb0c8212a26.herokuapp.com/)

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