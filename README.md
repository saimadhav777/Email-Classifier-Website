# Spam Mail Classification

## Description

The **Spam Mail Classification** project is a web-based application designed to categorize emails as either spam or ham using machine learning techniques. The application features a Flask backend, a frontend built with HTML, CSS, and JavaScript, and a MySQL database for user data and email classifications.

### Features

- **Email Classification**: Automatically categorizes incoming emails as spam or ham.
- **User Registration and Login**: Secure account creation and authentication for users.
- **Real-Time Email Classification**: Classifies emails in real time as they are received.
- **User Dashboard**: Allows users to view their email history and classification results.
- **Machine Learning Model**: Utilizes a pre-trained model to determine email classifications.
- **Customization**: Users can adjust spam filter settings to better suit their needs.

## Technologies Used

- **Flask** (Python Web Framework): Serves as the backend server.
- **HTML, CSS, and JavaScript** (Frontend): Provide the user interface.
- **MySQL** (Database): Stores user data and email classifications.
- **Machine Learning Libraries** (e.g., Scikit-Learn): Develop and deploy the email classification model.

## Getting Started

Follow these steps to set up and run the Spam Mail Classification application:

### Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package installer)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/saimadhav777/Email-Classifier-Website.git
   cd Email-Classifier-Website
   ```

2. **Set Up the Flask Backend and MySQL Database**:
   - Refer to the provided documentation for detailed instructions on configuring the Flask backend and MySQL database.

3. **Install Required Python Packages**:

   ```bash
   pip install Flask
   pip install nltk
   pip install mysql-connector-python
   ```

4. **Configure the MySQL Database**:
   - Log in to your MySQL server and create the necessary database and table:
   - **Note:** Please Ensure that you have used you root password in the following mysql-connector.

   ```sql
   CREATE DATABASE mysql;
   USE mysql;
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       full_name VARCHAR(255) NOT NULL,
       username VARCHAR(255) UNIQUE NOT NULL,
       email VARCHAR(255) UNIQUE NOT NULL,
       phone VARCHAR(15) NOT NULL,
       password VARCHAR(255) NOT NULL
   );
   ```

5. **Run the Flask Application**:

   ```bash
   python app.py
   ```

   - Open your web browser and navigate to:

   ```bash
   http://127.0.0.1:5000/
   ```

## Author

- **Sai Madhav and Bhargav**

## License

Specify the license under which your project is distributed. For example, you can use the MIT or Apache 2.0 license.

## Acknowledgments

- Special thanks to the developers and communities behind the libraries, tools, and resources used in this project.

---

Feel free to customize this README template to better fit your project's requirements.

## Screen-Shots
![Home-Page](Home-page.png)
![Login-Page](Login-page.png)
![Register-Page](Register-page.png)
![About-section](About-section-1.png)
![Email-classifier](Email-classifier.png)