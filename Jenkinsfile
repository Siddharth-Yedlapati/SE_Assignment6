pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Siddharth-Yedlapati/SE_Assignment6'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x GetElement.py"
                sh "./GetElement.py"
            }
        }
        stage('Pass Test Code') {
            steps {
                sh "chmod u+x PassTestCases.py"
                sh "./PassTestCases.py"
            }
        }
        stage('Fail Test Code') {
            steps {
                sh "chmod u+x FailTestCases.py"
                sh "./FailTestCases.py"
            }
        }
    } 
}
