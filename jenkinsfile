pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                checkout([$class: 'GitSCM', branches: [[name: 'main']], 
                          userRemoteConfigs: [[url: 'https://github.com/yourusername/your-repo.git']]])
            }
        }

        stage('Build') {
            steps {
                // Compile Python files
                sh 'python3 -m py_compile src/*.py'
            }
        }

        stage('Test') {
            steps {
                // Run tests using pytest
                sh 'python3 -m pytest tests/'
            }
        }
    }
}