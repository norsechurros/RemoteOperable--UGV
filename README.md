# Website Control for UGV

## Introduction

This is a simple web application for a website to control a UGV using python websockets that link to ROS commands running on localhost to maneuver a UGV whilst recieving live video feed attached onto the bot.

The application uses a basic HTML skeleton alongside JS code to handle button events which are then handled by the python WebSocket to interpret them as valid ROS commands directly input onto the terminal.

## Pre-requisites

The application requires the local host to be booted and running the motor control script alongside with the video feed pre-interfaced with the localhost.An internet connection over VPN allows control of the local host from a remote machine from virtually any wifi connection.
