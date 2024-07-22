pipeline {
    agent any

    environment {
        VENV_PATH = "./venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git 'https://github.com/Tthh123/test12'
            }
        }

        stage('Set Up Environment') {
            steps {
                // Set up the virtual environment and install dependencies
                sh 'python -m venv ${VENV_PATH}'
                sh '. ${VENV_PATH}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Dependency Check') {
            steps {
                // Perform dependency check
                sh '. ${VENV_PATH}/bin/activate && pip install safety && safety check'
            }
        }

        stage('Lint') {
            steps {
                // Perform code linting
                sh '. ${VENV_PATH}/bin/activate && pip install flake8 && flake8 .'
            }
        }

        stage('Run Tests') {
            steps {
                // Run unit tests
                sh '. ${VENV_PATH}/bin/activate && pip install pytest && pytest'
            }
        }

        stage('UI Testing') {
            steps {
                // Start Flask application
                sh '. ${VENV_PATH}/bin/activate && FLASK_APP=app.py flask run --host=0.0.0.0 &'
                sleep 10 // Give Flask app time to start

                // Perform UI tests (example using Selenium)
                sh '. ${VENV_PATH}/bin/activate && pip install selenium'
                // Add your UI test commands here

                // Stop Flask application
                sh 'pkill -f "flask run"'
            }
        }

        stage('Deploy') {
            steps {
                // Deploy using Docker Compose
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            // Clean up actions, e.g., archiving logs or reports
            archiveArtifacts artifacts: '**/test-reports/*.xml', allowEmptyArchive: true
            junit '**/test-reports/*.xml'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
