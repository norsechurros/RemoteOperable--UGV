#!/usr/bin/env python3.10

import asyncio
import websockets
from geometry_msgs.msg import Twist
import rospy

# Initialize ROS node (make sure ROS is installed and a roscore is running)
rospy.init_node('teleop_server')

# Create a publisher to send Twist messages to control the robot
cmd_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

async def teleop_server(websocket, path):
    while True:
        command = await websocket.recv()
        print(f"Received command: {command}")
        handle_command(command)

def handle_command(command):
    # Add your logic to interpret the command and control the teleop twist keyboard

    # For simplicity, let's assume 'I', 'J', 'K', 'L' correspond to linear and angular velocities
    twist = Twist()

    if command == 'I':
        twist.linear.x = 0.5  # Move forward
        #print("I")
    elif command == ',':
        twist.linear.x = -0.5  # Move backward
    elif command == 'J':
        twist.angular.z = 0.5  # Turn left
    elif command == 'L':
        twist.angular.z = -0.5  # Turn right
    elif command == 'K':
        # Stop the robot
        twist.linear.x = 0.0
        twist.angular.z = 0.0

    # Publish the Twist message to control the robot
    cmd_vel_publisher.publish(twist)

if __name__ == "__main__":
    # Change the port to 3000
    port = 3000

    # Start the WebSocket server
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(teleop_server, "0.0.0.0", port)
    )

    print(f"WebSocket server listening on ws://localhost:{port}")

    # Keep the server running
    asyncio.get_event_loop().run_forever()