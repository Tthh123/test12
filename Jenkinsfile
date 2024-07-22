pipeline {
    agent {
        docker {
            image 'python:3.8-slim'
            args '-u root:root'
        }
    }

    environment {
        VENV_PATH = "./venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/Tthh123/test12']]])
            }
        }

        stage('Set Up Environment') {
            steps {
                sh 'python -m venv ${VENV_PATH}'
                sh '. ${VENV_PATH}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Dependency Check') {
            steps {
                sh '. ${VENV_PATH}/bin/activate && pip install safety && safety check'
            }
        }

        stage('Lint') {
            steps {
                sh '. ${VENV_PATH}/bin/activate && pip install flake8 && flake8 .'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. ${VENV_PATH}/bin/activate && pip install pytest && pytest'
            }
        }

        stage('UI Testing') {
            steps {
                sh '. ${VENV_PATH}/bin/activate && FLASK_APP=app.py flask run --host=0.0.0.0 &'
                sleep 10
                sh '. ${VENV_PATH}/bin/activate && pip install selenium'
                // Add your UI test commands here
                sh 'pkill -f "flask run"'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
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
