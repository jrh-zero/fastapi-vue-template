pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Frontend') {
            steps {
                sh '''
                cd frontend
                npm install
                npm run build
                '''
            }
        }
        stage('Package Backend') {
            steps {
                sh '''
                pip install fastapi uvicorn pyinstaller
                pyinstaller myapp.spec
                '''
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/myapp/**', fingerprint: true
            }
        }
    }
}
