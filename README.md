# Sprinkles-SprinkleSafely_SCDFXIBM
SCDF Innovation Challenge 2020\
Problem Statement: **Climate Change**\
\
*Climate change is inevitable, with projected increase in temperatures leading to phenomena such as the Urban Heat Island effect. This leads to an environment and climate where it is increasingly physically challenging for First Responders to train and operate to maximum efficiency and performance. How might SCDF **leverage wearables or other technologies** to provide **relief or enhancement in harsh operating conditions** and **maximise the safety, health and performance of First Responders** during **training** and **operations**?*


## Contents
1. [Short Description](#short-description)
2. [Pitch Video](#pitch-video)
3. [Architecture of Solution](#architecture-of-solution)
4. [Detailed Solution](#detailed-solution)
5. [Getting Started](#getting-started-installation)
6. [Running the Tests](#running-the-tests)
7. [Live Demo](#live-demo)
8. [Built With](#built-with)

## Short Description
We are not familiar with the full system of how SCDF handles training and operation safety. In the light of climate change, we have decided to tackle the problem of the impact of climate on physical condition, in order to address the health of First Responders, for example higher temperatures in the surrounding environment. Vital signs of the trainees will also be taken and used to predict danger signs. 

## Pitch Video
Video: (Marcus put here when its done)

Description:
We introduce the environmental factors which affect one's body vitals and the possible health risks associated with these environmental factors.

We show demonstrate how our solution, the fitbit device, allows one to detect the changes in external environment temperature, as well as one's heart rate. The information provided to the fitbit device will remind the trainee with notifications such as "Reduce Training Intensity, High Heart Rate" when necessary, to ensure the safety and health of the trainee.

Next, we demonstrate how using our solution allows one to monitor their body's vitals and their external environment to ensure that training is conducted safely.

## Architecture of Solution
Weather data: https://data.gov.sg/dataset/realtime-weather-readings

Weather forecast: https://data.gov.sg/dataset/weather-forecast

Algorithm:
Collect real-time weather data with training.
Collect real-time data of trainee’s vitals during training. (Include parameters such as initial hydration, heartbeat, uninterrupted rest time)
Process both data to look for correlations. Use well-founded indicators to determine dangerous boundaries in data.
With prolonged use, this can be used to aid in adapting future safety measures to keep up with climate change trends. (instead of changes that follow after operation accidents)

Frontend: If the system proves sound and reliable, any officer can interact with it directly to decide on rest times, sustained training durations, intensities. They do not have to take guesses on the trainees’ physical conditions, this allows for personalised monitoring of every individual so that if there are vulnerable trainees, they can be quickly identified.

## [Detailed Solution](DESCRIPTION.md)

## Getting Started (Installation)

## Running the Tests

## Live Demo

## Built with
* IBM Cloudant
* IBM Watson Assistant - Voice-enabled chatbot frontend
* IBM Watson Studio (Data Refinery, Auto AI)

## Authors
Johnathan, Marcus, Xuan Ming, YiJia


