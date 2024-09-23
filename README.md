# SENASoft 2024 Project - Local Development Setup
[Ver en Español](./README_SP.md)

This README provides instructions for setting up the development environment for the SENASoft 2024 project. Follow these steps to get the project running on your local machine.

## Prerequisites

Before you begin, ensure you have the following software installed on your system:

1. **Python**: Version 3.12 or higher
   - Download from: https://www.python.org/downloads/
   - Verify installation: `python --version`

2. **Node.js**: Latest LTS version (18.x or higher)
   - Download from: https://nodejs.org/
   - Verify installation: `node --version`

3. **npm**: Comes with Node.js installation
   - Verify installation: `npm --version`

4. **Git**: Latest version
   - Download from: https://git-scm.com/downloads
   - Verify installation: `git --version`

5. **Visual Studio Code**: Latest version
   - Download from: https://code.visualstudio.com/
   - Recommended extensions:
     - Python
     - Pylance
     - Vue.js Extension Pack
     - ESLint
     - Prettier

## Project Setup

1. **Clone the Repository**
   ```
   git clone https://github.com/your-repo/senasoft-2024.git
   cd senasoft-2024
   ```

2. **Backend Setup (Python/FastAPI)**
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Frontend Setup (Vue.js)**
   ```
   cd frontend
   npm install
   ```

4. **Environment Variables**
   - Copy `.env.example` to `.env` in the `backend` or `frontend` directory you are working on
   - Fill in the necessary environment variables

## Running the Application

1. **Start the Backend Server**
   ```
   cd backend
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

2. **Start the Frontend Development Server**
   ```
   cd frontend
   npm run serve
   ```
   The frontend will be available at `http://localhost:8080`

3. **Access the Application**
   Open your web browser and navigate to `http://localhost:8080`

## Development Workflow

1. Make changes in your local environment
2. Test changes locally
3. Commit changes to Git
4. Push changes to the remote repository
5. CI/CD pipeline will handle deployment to Render

## Troubleshooting

If you encounter any issues during setup or development, please refer to the project documentation or create an issue in the GitHub repository.

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Vue.js Documentation](https://vuejs.org/guide/introduction.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

Happy coding!