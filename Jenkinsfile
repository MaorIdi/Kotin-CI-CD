pipeline {
  agent any

  environment {
    IMAGE_NAME = "kmp-ci-cd"
    APK_PATH   = "androidApp/build/outputs/apk/debug/androidApp-debug.apk"
  }

  stages {
    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
      }
    }

    stage('Build APK') {
      steps {
        sh """
          docker run --rm \
            -v \${WORKSPACE}/output:/app/androidApp/build/outputs \
            ${IMAGE_NAME}:${BUILD_NUMBER}
        """
      }
    }

    stage('Test') {
      steps {
        sh """
          docker run --rm \
            ${IMAGE_NAME}:${BUILD_NUMBER} \
            ./gradlew --no-daemon test
        """
      }
    }

    stage('Archive APK') {
      steps {
        archiveArtifacts artifacts: 'output/apk/debug/*.apk', fingerprint: true
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploy step — add distribution logic here (e.g. Firebase App Distribution, S3, etc.)'
      }
    }
  }

  post {
    always {
      sh "docker rmi ${IMAGE_NAME}:${BUILD_NUMBER} || true"
    }
  }
}