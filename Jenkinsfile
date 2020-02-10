pipeline {

  agent any

    stages {

      stage('TEST') {
        steps {
          sh 'pytest'
        }
      }

      stage('BUILD') {
        steps {
          sh 'rm -r -f dist'
          sh 'python3 setup.py sdist'
          sh 'pip install --upgrade psutil'
       }
      }

      stage('UPLOAD') {
        steps {
          sh 'python3 -m twine upload dist/* -u vipervit'
        }
       }

      stage('DEPLOY') {
        steps {
          sh 'pip install --upgrade viperlib'
        }
       }

       stage('DOCKER: Make image') {
        steps('remove old and build new image')     {
          sh 'docker rmi vipervit/viperlib:latest --force'
          sh 'docker build -t vipervit/viperlib:latest .'
        }
      }

      stage('DOCKER: Push image') {
        steps('push image') {
          sh 'docker push vipervit/viperlib:latest'
        }
      }


    }
}
