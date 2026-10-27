
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t student-registration .'
            }
        }

        stage('Run') {
            steps {
                bat 'docker rm -f student-app 2>NUL || exit /b 0'
                bat 'docker run -d --name student-app -p 5000:5000 student-registration'
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
