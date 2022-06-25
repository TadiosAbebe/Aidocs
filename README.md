# Aidocs

This is a project that I have done in my final years of Electrical and Computer Engineering Education at Haramaya University. It is a web-based document similarity analyzer written in python which can compute document similarity with two different approachs.

# Objectives
## General Objective
To create a web application an average user can perform document similarity analysis in both semantic and syntactic methods using NLP and machine learning algorithms through a simple interface.
## Specific Objective
- demonstrate TF-IDF algorithm for syntactic feature extraction from a text document
- demonstrate Word2Vec algorithm for semantic feature extraction from a text document
- develop and web application that can perform text similarity analysis
- demonstrate the use of similarity algorithms through a plagiarism detector

# Walkthrough and Screenshots
### Authentication
Through the authentication setup, users of the system can sign up if they are first-time users or can sign in if they have already created an account on the system
![image](https://user-images.githubusercontent.com/65541338/175792559-a75dc33f-bac9-4ec0-a584-55b2d01aff05.png)
When clients are signing up for the first time, they will be required to fill out a form that asks them for their username, first name, last name, email, and password.
![image](https://user-images.githubusercontent.com/65541338/175792573-b5aa7e9d-d0f3-4054-b939-8a71f61b0b5b.png)
![image](https://user-images.githubusercontent.com/65541338/175792586-b352cf52-e626-470d-8cba-2b7f6174f828.png)
If a user is signed-in with a valid user identity the navbar of the application shows the username of the signed-in user and it also gives the user the ability to sign out of the system with a button beside its username.
![image](https://user-images.githubusercontent.com/65541338/175792606-9facb221-2429-4dc1-8fac-d14fb78c3e5a.png)
### Home
The home element is what any user receives when navigating to the root of the web application's URL. The server will respond with a home page where users are introduced with alittle intro about what the web app does and a call-to-action button to get them started.
![image](https://user-images.githubusercontent.com/65541338/175792650-b071220a-2d31-4cc4-a6b1-305df23d9ea2.png)
Apart from that further down the page, it answers the question, of what document similarity is, how it works, and what is it used for.
![image](https://user-images.githubusercontent.com/65541338/175792656-abdb78bb-4288-48ee-8eb9-66ef8ff36162.png)
### Projects
"Projects" is the part of the web app that is presented after users have successfully signed into the system. This is the section where users can create a project and perform all the analysis they need. On the first time after signing up for the system when users navigate to the projects page, they are only able to see the "Plagiarism Detection Database" project that is created by the admin of the site and accessible through all users' accounts.
![image](https://user-images.githubusercontent.com/65541338/175792687-36f9a871-6858-430d-a3c4-fceb14c48060.png)
Apart from that, there will not be any listed projects under that user's projects page. There is a button with the plus icon at the header of the page that redirects the users to create a new project. On the new projects page, the client is required to give their project a name and add files to the project with a file picker. When choosing a file users have the flexibility to choose a document that has a .pdf format or a .txt format, both formats are allowed under one corpus. After filling in all the information, when the user clicks on the button "create project" the backend will process all the input files and determine their file type automatically. If a file has a .txt file type it will get automatically saved to the database but if a file has a .pdf file type it is going to be converted to a .txt file by iterating through the page and extracting all the text information.
![image](https://user-images.githubusercontent.com/65541338/175792719-6dbc06a2-0b24-41bc-ac22-9e9474bd2075.png)
On successful completion of project creation, users are redirected to the projects page again to see the list of the created projects by that user.

When users select a project from the list of projects that they have created they are going to be redirected to that specific project’s page that allows them to add additional files or remove the project. Apart from the users will see a list of added files and an option to compute document similarity on the corpus.
![image](https://user-images.githubusercontent.com/65541338/175792743-f6c5c85f-56b6-4471-9f20-987c169edc5e.png)
when the user clicks on the compute document similarity button they are redirected to a page where they find a list of ways of computing document similarity. Mainly in our project, there are two ways of computing document similarity these are, syntactically and semantically. The syntactic way of computing document similarity is presented as a TF-IDF cosine similarity method and the semantic way of computing document similarity is presented as a Word2Vec cosine similarity method. Besides the two users have the flexibility to click on an option called plagiarism detection, which uses both the semantic and syntactic way of computing document similarity and gives the average value of the two results.
![image](https://user-images.githubusercontent.com/65541338/175792762-f72f1ba2-b938-47e0-9cf1-150881721976.png)
Once a user selects an algorithm, they are redirected to a page that allows them to select one file with a dropdown menu from the corpus of documents that the user needs to compare against the rest of the corpus
![image](https://user-images.githubusercontent.com/65541338/175792771-773824e2-8018-46d1-9608-207fe5099847.png)
Once the user selects the file and clicks on the button "compare", the backend will process all data in the corpus-based on the algorithm selected by the user and respond with a value of how much the documents in the corpus seemed similar to the selected document.
![image](https://user-images.githubusercontent.com/65541338/175792781-e60dd879-a262-4a6f-b781-be477afac204.png)










