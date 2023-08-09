# PlacementGo - Problem Set Platform

PlacementGo is a web application built to help aspiring software engineers enhance their Data Structures and Algorithms (DSA) skills. The platform is developed using Django, PostgreSQL, and Django Rest Framework, and it offers a rich set of features to engage users in practicing and improving their problem-solving abilities.

## Features

### User Authentication and Authorization

PlacementGo utilizes a powerful authentication system based on JSON Web Tokens (JWT) to provide secure user registration and login functionality. Users can create accounts, log in, and access the platform's features securely.

### DSA Problem Set

The heart of PlacementGo is its comprehensive DSA problem set. Users can explore a wide range of coding challenges and exercises, each designed to improve their DSA knowledge. The problem set is neatly categorized and tagged, making it easy for users to find problems that match their skill level and interests.

### Voting and Bookmarking

Users can vote for their favorite problems, allowing the community to identify the most popular challenges. Additionally, users can bookmark problems to save them for later review or practice. This feature helps users keep track of problems they find particularly useful or challenging.

### Sorting Options

PlacementGo provides users with various sorting options to enhance their problem-solving experience. Users can sort problems based on tags, votes, and relevance. This flexibility enables users to focus on specific topics, identify trending challenges, and tailor their practice sessions according to their preferences.

## Installation

To set up PlacementGo locally, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/placementgo.git`
2. Navigate to the project directory: `cd placementgo`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Create a PostgreSQL database and update the database settings in `settings.py`.
5. Apply database migrations: `python manage.py migrate`
6. Create a superuser account: `python manage.py createsuperuser`
7. Launch the development server: `python manage.py runserver`

Access the PlacementGo platform by opening a web browser and navigating to `http://localhost:8000/`.

## Contributing

Contributions to PlacementGo are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-new-feature`
3. Make your changes and commit them: `git commit -m "Add new feature"`
4. Push the changes to your fork: `git push origin feature-new-feature`
5. Open a pull request detailing your changes.

Please ensure your code follows the project's coding standards and practices.

## Feedback and Support

If you encounter any issues, have suggestions for improvement, or need assistance, please don't hesitate to open an issue on the GitHub repository. Your feedback is valuable and will help make PlacementGo a better platform for everyone.

Start enhancing your DSA skills with PlacementGo today! Happy coding! 🚀
