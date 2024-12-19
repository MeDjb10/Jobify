### **Jobify - Recruitment Platform**

---

## **🚀 Project Overview**

Welcome to **Jobify**, a platform designed to streamline the recruitment process by automatically matching candidates' skills with job descriptions. Using matching algorithms, it simplifies the job application process for candidates and provides recruiters with more effective candidate recommendations. The goal is to create an efficient, user-friendly recruitment solution for both job seekers and employers.

---

## **🎯 Features & Highlights**

### **For Recruiters**
- **Job Post Management**: Add, modify, and delete job offers with specific requirements.
- **Candidate Recommendations**: Receive recommendations for candidates with transferable skills.
- **Job Application Notifications**: Get notified when candidates match job requirements.
- **Resume Feedback**: Receive insights on the candidates’ resumes and their matching scores.

### **For Candidates**
- **Job Matching**: View a list of job offers ranked by relevance.
- **Resume Submission**: Submit resumes for AI analysis and get matched with relevant job offers.
- **Application Status**: Receive feedback on resume status to track progress in the recruitment process.

---

## **🔗 AI Integration**

Jobify integrates with the **AI-Resume Analyzer**, an open-source project by [Deepak Padhi](https://github.com/deepakpadhi986/AI-Resume-Analyzer). This tool parses information from resumes using natural language processing (NLP) to:
- Extract keywords.
- Cluster skills into sectors based on keywords.
- Provide recommendations, predictions, and analytics to the applicant.

The **AI-Resume Analyzer** enhances the resume analysis and matching process in Jobify, making the system more efficient and accurate.

> **AI-Resume Analyzer Repository**: [https://github.com/deepakpadhi986/AI-Resume-Analyzer](https://github.com/deepakpadhi986/AI-Resume-Analyzer)

---

## **🧑‍💻 Tech Stack**

Jobify uses modern technologies to ensure a seamless and scalable user experience:

- **Frontend**: Angular, TypeScript, HTML5, CSS3, Bootstrap
- **Backend**: Django (Python), REST APIs
- **Database**: MySQL
- **Authentication**: JSON Web Tokens (JWT)
- **Deployment**: Nginx, Gunicorn, SSL for secure connections
- **AI Resume Parsing**: NLP-based **AI-Resume Analyzer**

---

## **💼 Agile Methodologies and Scrum Framework**

Jobify was developed following **Agile methodologies** with the **Scrum framework**. This approach ensured iterative development, collaboration, and adaptability throughout the project.

### **How We Worked with Scrum**
- **Sprints**: The development process was divided into three sprints, each lasting two weeks. Each sprint focused on delivering specific user stories and functionalities:
  - **Sprint 1**: Initial setup, authentication, and job posting features.
  - **Sprint 2**: Candidate resume submission, job matching, and recruiter notifications.
  - **Sprint 3**: Enhancements, bug fixes, and deployment readiness.
  
- **Sprint Backlog**: Tasks were broken down into smaller subtasks and assigned to team members during sprint planning.

- **Daily Standups**: Brief meetings were held daily to discuss progress, challenges, and next steps.

- **Sprint Review**: At the end of each sprint, we demonstrated completed features and gathered feedback.

- **Retrospectives**: We reflected on successes and areas for improvement after every sprint, enabling continuous process refinement.

### **Agile Benefits in Jobify**
- **Transparency**: Regular communication and sprint reviews kept the team aligned with the project's goals.
- **Flexibility**: Agile allowed us to adapt to changes in requirements and priorities.
- **Incremental Delivery**: Working in sprints ensured a steady progression of features, with usable functionality at the end of each iteration.

---

## **💡 How to Get Started**

Follow these simple steps to set up **Jobify** locally:

### Step 1: Clone the Repository

```bash
git clone https://github.com/MeDjb10/Jobify
cd jobify
```

### Step 2: Install Frontend Dependencies

```bash
cd frontend
npm install
```

### Step 3: Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Step 4: Configure the Database
- Set up a MySQL database and configure the database settings in `backend/settings.py`.

### Step 5: Migrate Database

```bash
cd backend
python manage.py migrate
```

### Step 6: Run the Application

#### Frontend:
```bash
cd frontend
ng serve --open
```

#### Backend:
```bash
cd backend
python manage.py runserver
```

You're all set! Access the platform at `http://localhost:4200` for the frontend and `http://localhost:8000` for the backend API.

---

## **🔍 Key Screenshots & Demos**

Here's a preview of the app with screenshots for key interfaces:

### **Recruiter Interface**
- Manage job postings: add, modify, or delete.
![Manage Job Postings](screenshots/JobOfferCrud.png)

- Notifications for candidate applications.
![Recruiter Notifications](screenshots/Notifications.png)

### **Candidate Interface**
- View job matches ranked by relevance.
![Job Matches](screenshots/Matches.png)

- Submit resume for AI analysis.
![Resume Submission](screenshots/upload.png)

### 🎥 Video Demo

Watch the full demo video [here](https://www.dropbox.com/scl/fi/iflbpdznupui19fz3mrcb/Demo-Jobify-Made-with-Clipchamp_1733850143846.mp4?rlkey=600z2uw4pqjpq4uulbtdr61ng&dl=0).

---

## **🔑 API Documentation with Swagger**

Swagger was integrated into the backend to provide an interactive and easy-to-navigate API documentation interface:

- **API Endpoints**: All backend endpoints are documented automatically using **drf-yasg**.
- **Interactive UI**: Test API calls directly from the Swagger UI, located at `/swagger/` in the app.
- **Benefits**: With Swagger, developers and external users can understand and test the backend API seamlessly.

---

## **📈 Contribution Guidelines**

We welcome contributions to **Jobify**! Here’s how you can contribute:
1. Fork the repository on GitHub.
2. Create a new branch: `git checkout -b feature-xyz`.
3. Make your changes and commit them: `git commit -am 'Add feature XYZ'`.
4. Push your branch: `git push origin feature-xyz`.
5. Create a pull request for review.

We follow the **GitFlow** workflow for new features and bug fixes.

---

## **🔒 Security**

Jobify integrates **JWT Authentication** for secure user login, ensuring that both recruiters and candidates can access only their designated features.

---

### **🎨 UI/UX Design**

Jobify boasts a clean, intuitive interface with smooth transitions between job listings, applications, and candidate notifications. The platform is designed to be user-friendly, ensuring ease of use for non-technical users.

---

### **🚀 Ready to Get Started?**

Clone the repository, follow the setup instructions, and begin using **Jobify** today! Streamline your recruitment process with intelligent job matching and a seamless user experience.
