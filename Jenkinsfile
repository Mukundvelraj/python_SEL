pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/Mukundvelraj/python_SEL.git', branch: 'main')
      }
    }

    stage('RUN Python') {
      steps {
        bat 'python Class_Self.py'
      }
    }

  }
}