pipeline {
    agent any

    environment {
        COMPOSE_FILE = './compose.yaml'
        FLASK_APP_DIR = './flask_app'
    }

    stages {
        stage('Build and Start Services') {
            steps {
                script {
                    // Build and start Docker services
                    sh 'docker-compose -f $COMPOSE_FILE up -d --build'
                }
            }
        }

        stage('Dependency Check') {
            steps {
                script {
                    // Run dependency check (example for Python dependencies)
                    sh 'docker exec -w /usr/src/app flask_app pip check'
                }
            }
        }

        stage('Integration Test') {
            steps {
                script {
                    // Run integration tests
                    sh 'docker exec -w /usr/src/app flask_app pytest tests/integration'
                }
            }
        }

        stage('UI Test') {
            steps {
                script {
                    // Run UI tests
                    sh 'docker exec -w /usr/src/app flask_app python ui_test.py'
                }
            }
        }
    }

    post {
        always {
            // Clean up
            script {
                sh 'docker-compose -f $COMPOSE_FILE down'
            }
        }
    }
}
