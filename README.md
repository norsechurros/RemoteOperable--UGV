
# Robot Teleoperation System with Web Interface and ROS Integration

## Overview
This repository provides a teleoperation system for controlling a robot through a web interface. It features real-time video streaming, WebSocket communication, and ROS integration, enabling efficient and seamless remote robot operation.

## Features
- **Web Interface**: An HTML-based control panel to send movement commands to the robot.
- **Live Video Feed**: Displays real-time video from the robot's environment.
- **WebSocket Communication**: Lightweight communication between the web client and server.
- **ROS Integration**: Sends ROS Twist messages for robot movement control.

## Technology Stack
- **Frontend**: HTML, JavaScript, CSS
- **Backend**: Python with WebSocket server
- **Robot Middleware**: ROS (Robot Operating System)

---

## Installation and Usage

### Prerequisites
- Python 3.10 or later
- ROS installed with `geometry_msgs` package
- Python WebSocket support (`websockets` package)

### Steps to Run

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Start the ROS Node**
   Ensure your ROS master node is running:
   ```bash
   roscore
   ```

3. **Run the WebSocket Server**
   Start the WebSocket server to process teleoperation commands:
   ```bash
   python3.10 websocket_server.py
   ```

4. **Run the Web Interface**
   Open the `mk1_4.html` file in your browser. Verify that the WebSocket URL matches the server's address and port.

5. **Control the Robot**
   Use the web interface to send movement commands:
   - **I**: Move forward
   - **,**: Move backward
   - **J**: Turn left
   - **L**: Turn right
   - **K**: Stop

---

## Files
- **`mk1_4.html`**: Frontend web interface for robot control.
- **`websocket_server.py`**: WebSocket server for processing commands.
- **Video Feed**: Integrated video feed in the web interface using Flask or a similar setup.

---

## Future Enhancements
- Add user authentication for secure access.
- Integrate advanced features like obstacle detection.
- Enable logging of commands for debugging and analytics.

---

## License
This project is open-source and distributed under the MIT License. Feel free to use, modify, and share for personal or educational purposes.

---

## Contributing
Contributions are welcome! If you want to add features or suggest improvements, please open an issue or submit a pull request.

---

## Resources and Links
- **Documentation**: [ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)
- **Live Demo**: Contact the repository owner for a demo setup.
```

This corrected README maintains a clean structure, includes all necessary information, and avoids redundancy. Let me know if you want further refinements!
