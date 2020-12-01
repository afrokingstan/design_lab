# Design Lab

This project is a site to sell your graphic design services, Users are able to purchase graphical designs to address their needs 
while the site owner Earn money for doing freelance design work.
 
## UX
 
In this project I paid attention to user story to achieve an easy to use website for both shopper and site user
- As a Shopper, I want to be able to view and navigate through services and freelance portfolio easily, so that I can select a service to purchase and see previous work
- As a Site User, I want to be able to register an account, receive a confirmation email when I have registered and easily recover my password in case I ever forget it, So that I can have a personal account and be able to view my profile, access my personal information and verify my account registration was successful.
- As a Shopper, I want to be  able to easily select size and quantity of a design before I purchase it, so that I don't accidentally select the wrong design size and quantity.
- As a Site USer, I want to be able to write down the description of the type of design i want, so that I know that my requirements are communicated to the designer and that my needs are met.

- [wireframes](https://github.com/afrokingstan/design_lab/tree/master/wireframes)

## Features

In this section, I will go over the different parts of this project, and describe each in a sentence or so.
 
### Existing Features
- All Designs - allows Shopper to easily navigate all the design categories that the site has, by having them user the navigation menu
- Our Portfolio  - allows Site owner to easily Showcase prior work for Site Users, by having all prior work presented on the portfolio page available to all users.
- Reviews - allows Site user to easily read customer testimonials and also allowing Site user to write a review, by having site user signin or signup to leave a review on showcased work in the Portfolio
- Reviews  - allows Site owner to have control over removing reviews that are not genuine or containing offensive language, by ensuring reviews are not automatically made public when submitted by Site Users and having the Site owner signin as and admin to approve reviews
- Checkout - allow Shopper to  order a particular graphic to suit their goals , by having the Shopper fill out a form describing their needs, including fields such as type.

Additional features to be implemented in the future:

### Features Left to Implement
- Project Management - allows Site owner to be able to see a list of all orders, and then upload their completed work which would be made available, by having Site owner login as a special user.
to the customer
- Completed project - allow Site users to be able to see and download their completed design projects that they paid for, by having them signup or login and then access the completed project page. 

## Technologies Used

All of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, 
I have provided its name, a link to its official site and a short sentence of why it was used.

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - The project uses **HTML** to define the meaning and structure of the web content.
- [Python](https://www.python.org/)
    - The project uses **Python** to create, host and manage modules.
- [Json](https://www.json.org/json-en.html)
    - The project uses **Json** to simplify DOM manipulation.
- [Django](https://www.djangoproject.com/)
    - The project uses **Django** to simplify building better Web apps more quickly and with less code.
- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** to simplify design and customize responsive mobile-first sites with.
- [Stripe](https://stripe.com/gb)
    - The project uses **Stripe** to simplify online payment handling.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - The project uses **CSS** to simplify styling for better user experience.
- [Google fonts](https://fonts.google.com/)
    - The project uses **Google fonts** to simplify css font styling.
- [GMAIL](https://mail.google.com/)
    - The project uses **GMAIL** to simplify email functionality during deployment.
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - The project uses **django-allauth** to simplify user login and authentication.
- [SLQlite](https://sqlite.org/docs.html)
    - The project uses **SLQlite** as an embedded SQL database engine as the project database handler during testing.
- [Postgresql](https://www.postgresql.org/docs/)
    - The project uses **Postgresql** to simplify object-relational database management when during deployment.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
    - The project uses **django-crispy-forms** to provide support for bootstrap and forms like simplified form validation.
- [csrf](https://docs.djangoproject.com/en/3.1/ref/csrf/)
    - The project uses **csrf** to The CSRF middleware and template tag to provide easy-to-use protection against 
    Cross Site Request Forgeries
- [DjangoAdmin](https://docs.djangoproject.com/en/3.1/ref/django-admin/)
    - The project uses **DjangoAdmin** as command-line utility to simplify administrative tasks.
- [Pycharm](https://www.jetbrains.com/pycharm/)
    - The project uses **Pycharm** as a Python IDE for developing the project.
- [Anaconda Navigator](https://www.anaconda.com/)
    - The project uses **Anaconda Navigator** a desktop GUI that comes with Anaconda Individual Edition that makes it easy 
    to launch applications and manage packages and environments without using command-line commands.
- [Ngrok](https://ngrok.com/)
    - The project uses **Ngrok** to simplify Webhook handler simulation during testing.
- [github](https://github.com/)
    - The project uses **github** to simplify version control.
- [Amazon Webservices](https://aws.amazon.com/)
    - The project uses **Amazon Webservices** to simplify storage of static files.
- [Image URL Generator](https://imgbb.com/)
    - The project uses **Image URL Generator** to generate image url.
- [Heroku](https://www.heroku.com/)
    - The project uses **Heroku** to simplify Deployment and web hosting of this project.
    
    
## Testing

Testing on this project was not automated below is a list of how I performed testing on this project

1. All designs:
    1. Go to the landing page (also known as home page)
    2. Try to navigate to the all design page by using the shop now button, you may also use the nav menu and verify if any error appears 
    3. Try to filter the designs based on the available category, by using the category buttons  and verify if the specified category was loaded
    4. Try to click on a design pack and verify if you were presented with more information about that design pack.

2. Portfolio:
    1. Go to the "Portfolio" page as a Shopper who doesnt have a user account, by using the portfolio nav menu
    2. Try to click on a showcased work in the portfolio page and verify if you can see leave a review without signing up first.
    3. Try to click on the image and verify if you are redirected to the signup page.
    4. Try to click on the signup or signin button and verify if you are presented with an error or if you are redirected to the signup or signin page.

3. Register/Sign Up:
    1. Go to the "Sign Up" page by using the "My Account" menu at the top right hand of any page and try select Register
    2. Try to create a Site user account, filling in the form and verify that when you submit the form you see an Alert stating Confirmation e-mail sent to your email.
    3. Try to confirm if to have received an email from design_lab prompting you to click a link to confirm account creation. 
    4. Try to confirm your account creation by clicking the link in the email you received and verify if you get redirected to designlab website and that you get a success message - success you have confirmed your account

4. Reviews:
    1. Go to the "Portfolio" page as a logged in Site user
    2. Try to click on the on any showcased work and verify if you are presented with a form to submit a review accompanied with an alert message
    3. Try to submit the form without any fields filled in and verify that a relevant form validation message appears
    4. Try to submit the form with all inputs valid and verify that a alert message appears.
    
5. Making a purchase:
    1. Go to the "All Designs" page of try click on "shop now" button (as a logged in user or not logged in)
    2. Try to add an item to your shopping bag, by clicking on a design pack and select any size and click on add to bag and verify that you get a success message and the option to go to checkout.
    3. Try to checkout by clicking on the checkout button or bag button and verify if you can securely checkout by clicking the secure checkout button.
    4. Try to secure checkout by submitting the empty form and verify that an error message about the required fields appears.
    5. Try to secure checkout by submit the form with all inputs valid excluding the card details and verify that an error message appears stating "Your card number is incomplete."
    6. Try to secure checkout by submit the form with all inputs valid including the card details for this test use card details "4242 4242 4242 4242 DATE 04/24 CVC 424 ZIP 42424" and verify that you get an overlay screen and you are redirected to checkout_success page.
    7. Try to check if your payment was successful, by verifying that you get a success message and order summary and check that you received an order confirmation email from Design Lab. 


6. Search Feature:
    1. Go to the any page
    2. Try to submit the empty search, by clicking the search button at the top of the page and verify that an error message about You didn't enter any search criteria!
    3. Try to submit the a valid search, by entering key words like logo, logos , icon, icons etc into the search box and then submit, verify that a relevant search response if produced.

6. Screen test:
    1. Go to another device like your phone and open website [Design Lab](https://stan-designlab.herokuapp.com/) on your phone
    2. Try to use any of the features mentioned above and verify that the website is adapted for mobile viewing.
    
7. Bugs during testing:
    1. Favicon.ico was not found, I created a favicon [here](https://favicon.io/) and added it to the static [directory](https://github.com/afrokingstan/design_lab/tree/master/static/favicon) and added a static url to the base.html page which resolved the error.
    2. Webhook handler, during testing the webhook handler was not working which meant i couldn't see the checkout confirmation email in the terminal window.I researched [slack](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1591968859174000?thread_ts=1591966395.172900&cid=C7HS3U3AP), I followed the fix mentioned. I downloaded [ngrok](https://ngrok.io/qx7d4g/checkout/wh/) server and created a public url and a new webhook and then applied these settings and the issue was resolved. 


## Deployment

- In deployment stage I created a heroku app called [stan-designlab](https://stan-designlab.herokuapp.com/) in order to deploy my app and automat static files to amazon webservices.
- I also installed a free adon heroku postgres on heroku and installed gunicorn, django-storages, boto3 on the local app and added it to my requirement.txt file. I made sure to add storages to installed apps in settings.py
- In deployment i also had to set disablecollectstatic   = 1 at the first stage of deployment and then after amazon webservices was set up i removed the disablecollectstatic
- Different values for environment variables: The environment variables in testing was relatively less than that needed 
for deployment as i had to add secret key and secret id generated in Amazon web services storages. i also had to add the
secret variables for gmail to ensure emails can be sent to site users who are access the public domain.
- Different configuration files : settings.py which can be used to run test locally is found at another [git branch](https://github.com/afrokingstan/design_lab/tree/design_lab_for_testing)


## How to run project code locally.
To run my code locally I open Anaconda Navigator and launched Pycharm (all pre installed), then I ensured I had the correct version of the project open before running python manage.py runserver 127.0.0.1:7000 in the terminal.
then I view the url - http://127.0.0.1:7000/  locally on my computer. Debug is set to True in settings.py so that when there is a bug i can handle it before committing my changes to github
by typing git status , git add . , git commit -m "some commit message" , git push origin master in the pycharm terminal

## Credits
Credits to all the tutors who made the course videos and all those that contributed on slack to resolve issues that later on were helpful to this project

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from 
    - [pexels](https://www.pexels.com/)
    - [pixabay](https://pixabay.com/)
### Acknowledgements

- I received inspiration for this project from the example project ideas in this course and [DesignCrowd](https://www.designcrowd.co.uk/) and [99designs](https://99designs.co.uk/)
