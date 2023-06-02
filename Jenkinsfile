node {
    def app

    stage('Clone Repository') {
      

        checkout scm
    }

    stage('Build Image') {
  
       app = docker.build("dockersampath/packages")
    }

    stage('Test Image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push Image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
