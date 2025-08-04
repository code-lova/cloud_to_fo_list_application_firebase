# Overview

This project is a simple command-line To-Do List application that integrates with a cloud-based NoSQL database (Firestore from Google Firebase). The app allows users to add, view, mark as complete, and delete tasks from the cloud in real-time. 

The purpose of building this software is to explore the use of cloud databases in practical applications and to understand how Python can be used to perform CRUD operations on remote databases. This project helps me build foundational knowledge in cloud database integration, which is a valuable skill in modern software development.

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

The cloud database used in this project is **Google Firestore**, a flexible and scalable NoSQL cloud database provided by Firebase. Firestore allows for real-time updates, structured document-based storage, and strong integration with server-side apps using the Firebase Admin SDK.

### Authentication Structure:
- Users "log in" by entering their username (no password — this is a simulated lightweight auth).
- Each user has their own **user document** in the `users` collection.
- Tasks are stored under a **`tasks` subcollection** for each individual user.


### Firestore Structure:
users (collection)
└── {username} (document)
└── tasks (subcollection)
├── {taskID} (document)
│ ├── title: string
│ ├── description: string
│ └── completed: boolean

# Development Environment

- **Programming Language:** Python 3
- **Libraries/Packages:**
  - `firebase-admin`: Python SDK for Firebase
- **Cloud Platform:** Firebase Console with Firestore database
- **Tools Used:**
  - VS Code (Editor)
  - Firebase Console (Database configuration)
  - GitHub (Version control and publishing)
- **Installation:**
    - To install the required library:
    - ```bash
    - pip install firebase-admin



# Useful Websites

- [Firebase Python SDK Setup](https://firebase.google.com/docs/admin/setup)
- [Firebase Firestore Python CRUD Guide](https://firebase.google.com/docs/firestore/quickstart)
- [Firestore Data Model Concepts](https://cloud.google.com/firestore/docs/data-model)
- [YouTube Firestore Python Tutorials](https://www.youtube.com/results?search_query=python+firebase+firestore)

# Future Work

- Upgrade from simulated auth to real Firebase Authentication (email/password)
- Add task due dates and priority levels
- Enable real-time updates with Firestore listeners
- Create a simple web frontend using Flask or React
- Deploy the project with a frontend on Vercel or Render
