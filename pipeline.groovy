#!/usr/bin/env groovy

import groovy.json.JsonSlurper

pipeline {
	node {
		stage('Clone sources') {
			git url: 'https://github.com/sdblepas/exl_feed_ctl.git'
		}
	}

	agent none
	stages {
		stage ('pre-processing') {
			steps{
				def get = new URL("http://sd-99892.dedibox.fr:5555/exl_hands_on_lab/feeds.json").openConnection();
				def getRC = get.getResponseCode();
				if (getRC != 200) {
					System.exit(0)
				}else if (GetMaxTemp()) {
					System.exit(0)
				}
			}
		}
		stage ('processing'){
			steps{
				def task = "python exl_json_to_yml.py".execute() $Operation $Args
			}
		}
		stage ('post-processing'){
			steps{
				def task = "python exl_json_to_yml.py".execute()

			}	
		}
	}
	post {
		failure{			
					mail to: 'benjamin.elharrar@exlibrisgroup.com',
					subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
					body: "Something is wrong with ${env.BUILD_URL}"
				}	
	}

}

def GetMaxTemp() {
		def ApiUrl = new URL('https://api.openweathermap.org/data/2.5/onecall?lat=31.76&lon=35.21&exclude=hourly,daily&appid=2e38ebbb02a9b936c8d42f73a94a6dee&units=metric')
		def JSON = new JsonSlurper().parse(ApiUrl)
		Float idValue = JSON.get("current").get("temp");
		if (idValue>$MAXTEMP) {
			return true
		}else {
			return false
		}
}
