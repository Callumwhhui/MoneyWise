# MoneyWise

Welcome to MoneyWise – your trusted financial ally! 
Crafted by the brilliant minds at  **Code of Duty**, this is a full-stack CRUD web app poised to redefine how you manage your finances.

Meet the extraordinary team behind the curtain:

- [**RyanBullus**](https://github.com/RyanBulluss):  Our GitHub guru and backend maestro.

- [**Callumwhui**](https://github.com/Callumwhhui): The frontend virtuoso, sculpting magic with CSS, JavaScript, and ensuring an impeccable mobile experience.

- [**Viver2nd**](https://github.com/Viver2nd): The ultimate multitasker, seamlessly navigating both frontend and backend realms.

- [**AgatheLouiseLav**](https://github.com/AgatheLouiseLav): A frontend sorcerer, breathing life into the UI with CSS, JavaScript, and unrivaled mobile responsiveness.


MoneyWise simplifies your financial journey, providing a unified platform for orchestrating and optimizing your fiscal world. 

Our journey began with meticulous planning – from designing the [ERD](https://lucid.app/lucidchart/9985c499-91e7-458b-b83d-1e5883719283/edit?invitationId=inv_3caa7902-431a-45ff-8d95-b6348f94f7a1&referringApp=slack&page=0_0#) and [Wireframe](https://www.figma.com/file/fuBNpy4XGEFMZMEx97aOBA/FinanceApp?type=design&node-id=0-1&mode=design) to streamlining tasks through our [Trello](https://id.atlassian.com/login/authorize?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fb%252FumsLnd9q%252Ffinanceappproject3%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D&token=eyJraWQiOiJtaWNyb3Mvc2lnbi1pbi1zZXJ2aWNlL2E1amFwZ2RwOWh0cnM3MTIiLCJhbGciOiJSUzI1NiJ9.eyJtYXJrZWRWZXJpZmllZCI6ImZhbHNlIiwibG9naW5UeXBlIjoic2Vzc2lvblJlZnJlc2giLCJpc3MiOiJtaWNyb3Mvc2lnbi1pbi1zZXJ2aWNlIiwidXNlcklkIjoiNzEyMDIwOmRlZTI2MDY0LTIyZDItNGFhZi1iZWRiLTI0NjI5MzMwYjU4NyIsImlzU2xhY2tBcHBTb3VyY2UiOiJmYWxzZSIsImF1ZCI6Imxpbmstc2lnbmF0dXJlLXZhbGlkYXRvciIsIm5iZiI6MTY5MTY1OTUwNiwic2NvcGUiOiJMb2dpbiIsImV4cCI6MTY5MTY1OTYyNiwiaWF0IjoxNjkxNjU5NTA2LCJqdGkiOiJlNGVhYjcyMS0yYWM2LTQ1N2UtYWNkYy1kZWU3YTQxZDcyZjUiLCJoYXNoZWRDc3JmVG9rZW4iOiI4OTllYWRjMWU3MWM3MzBlZGY0YTg3MjMwZjM1OWI0ZmNjYTNjNDA4ODExYWU1M2ZmMjNhZGIzZDU5NmFiMmU3In0.v3tF2sY6oe4yebbFb_Tp8BQAu5vyR2JvDg974C65Doo9CL42wl0xkjhRimxmYMd0rYOQe4Fb_1ljYM8sfbSylCshCf4zHoSZN_JpyIVm5RgXTHNcH3uj8YGZOkiVRj6QzzUGR97h2BLYUI6quDXPsF4xLr3teicQMgwDDztsNr4161TFs79aOcaNCMogDiat9ykjgZw0DG-pAILww2Lj50fpZ37bVA6dsJJOMShC-aSotUHhR1CpYZQau-6ZOrKfm55GKjmYhcyHGOXOYb2l7k18zqJDJ9p5ZqUtHwbi14F6X-uCIOXSsPWVRRT3NoxFpWR6Bj-auaqtz_MUe1JfEg) board.

## Screenshots:

<img src="./main_app/static/images/mainwireframe_bis.png" alt="MoneyWise Wireframe" width="200px">

<img src="./main_app/static/images/mainerd.png" alt="MoneyWise ERD"  width="350px">

## Technologies Used:

- HTML,
- CSS,
- Bootstrap,
- Unicons,
- JavaScript,
- Charts.js,
- Python,
- Django,
- PostgreSQL,
- NeonDB,
- Git,
- GitHub,
- Alpha vantage stock API.

## Visite Our APP:

<a href="https://moneywise-fin-app-cfc615d6c6e8.herokuapp.com/accounts/login/">Link to MoneyWise</a>

Our project has crossed the finish line! As a team, we've checked off all the boxes: MVP is in place, along with mobile responsiveness, dark mode, authentication, dynamic graphs, and seamless CRUD operations. Our collaboration has been a driving force behind our success!

## Key Learnings

Our journey with MoneyWise has been an incredible learning experience, encompassing both technical and collaborative aspects. As we developed this full-stack CRUD web app, we gained valuable insights that have expanded our skill sets and enriched our teamwork. Here are some key learnings from our MoneyWise adventure:

1. **Collaboration is Key**: Building a complex project like MoneyWise required seamless collaboration between backend and frontend developers. Regular communication, code reviews, and addressing challenges as a team greatly contributed to our success.

2. **Dynamic Graphs**: The integration of Charts.js allowed us to present data dynamically with interactive graphs. This taught us how to visualise complex data sets and present them in an easily digestible format.

3. **Version Control**: Utilising Git and GitHub throughout the project underscored the importance of version control in collaborative development, enabling efficient code management and tracking changes.

## My Part In This Project

I took the lead in enhancing the project's frontend, implementing critical interactivity with JavaScript, including the introduction of a dark mode and optimizing the navbar for responsiveness. Most notably, I personally spearheaded the project's styling, ensuring a polished and visually appealing user experience.

### Darkmode 

Something I am most proud of implementing into the project would be the dark mode. 

Here is the function I wrote to help toggle the dark mode. 
```
function toggleDarkMode() {
			body.classList.toggle("dark");
			// Store the dark mode preference in localStorage
			localStorage.setItem('darkMode', body.classList.contains('dark'));
		}
```
Here Is the Event Listener. 
```
modeToggle.addEventListener("click", () => {
			toggleDarkMode();
		});
```
And here is the code that checks in local storage if the dark mode has been toggled or not. 
```
const isDarkMode = JSON.parse(localStorage.getItem('darkMode'));
		if (isDarkMode) {
			body.classList.add('dark');
		}
```

## The Brief 

☐ Be a full-stack Django application.

☐ Connect to and perform data operations on a PostgreSQL database (the default SQLLite3 database is not acceptable).

☐ If consuming an API (OPTIONAL), have at least one data entity (Model) in addition to the built-in User model. The related entity can be either a one-to-many (1:M) or a many-to-many (M:M) relationship.

☐ If not consuming an API, have at least two data entities (Models) in addition to the built-in User model. It is preferable to have at least one one-to-many (1:M) and one many-to-many (M:M) relationship between entities/models.

☐ Have full-CRUD data operations across any combination of the app's models (excluding the User model). For example, creating/reading/updating posts and creating/deleting comments qualifies as full-CRUD data operations.

☐ Authenticate users using Django's built-in authentication.

☐ Implement authorization by restricting access to the Creation, Updating & Deletion of data resources using the login_required decorator in the case of view functions; or, in the case of class-based views, inheriting from the LoginRequiredMixin class.

☐ Be deployed online using Heroku. Presentations must use the deployed application.

The app may optionally:
☐ Upload images to AWS S3

☐ Consume an API (installation of the Requests package will be necessary)

## Timeframe/ Working Team

MoneyWise is the result of an intensive collaborative effort within a group of dedicated developers, including myself. We embarked on this project with a shared vision to revolutionize financial management. Despite having just one week to bring this idea to life, our team, consisting of both frontend and backend developers, poured their expertise and creativity into every aspect of MoneyWise.


This challenging timeframe not only tested our technical skills but also honed our ability to work cohesively as a team under pressure. It taught us the value of effective communication, time management, and quick decision-making. We found innovative solutions to complex problems by leveraging each team member's unique strengths, making this project a testament to the power of collaboration in the fast-paced world of software development.



## My biggest challenge

☐ Github/ version control - Being my inaugural experience in a collaborative development setting, I encountered a notable challenge that was ensuring the absence of merge conflicts while simultaneously working on the project with my team members. 


