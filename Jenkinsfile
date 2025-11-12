pipeline {
    agent {
        docker {
            image 'python:3.9-alpine'  // Or use your custom image
            args '-v /var/jenkins_home:/workspace -p 5000:5000'
            reuseNode true
        }
    }
    
    environment {
        APP_NAME = 'aws-python-app'
        PYTHON_VERSION = '3.9'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/thummasaikiran/AWS-Services-pythonApp-CI-implementation.git'
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh '''
                    python --version
                    pip --version
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install -r requirements.txt
                    pip install pytest pytest-cov flake8 bandit safety
                '''
            }
        }
        
        stage('Code Quality') {
            steps {
                sh '''
                    echo "Running code quality checks..."
                    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                '''
            }
        }
        
        stage('Security Scan') {
            steps {
                sh '''
                    echo "Running security scan..."
                    bandit -r . -f html -o bandit_report.html || true
                    safety check || true
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running tests..."
                    python -m pytest tests/ -v --cov=. --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('Build Application') {
            steps {
                sh '''
                    echo "Building application..."
                    # Add any build steps here
                '''
            }
        }
    }
    
    post {
        always {
            echo "Pipeline ${currentBuild.result} - ${env.BUILD_URL}"
            archiveArtifacts artifacts: 'bandit_report.html', fingerprint: true
        }
        success {
            echo "Pipeline succeeded! "
        }
        failure {
            echo "Pipeline failed! "
        }
    }
}
