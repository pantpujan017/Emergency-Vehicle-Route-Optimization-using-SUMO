***Emergency Vehicle Route Optimization and Dynamic Traffic Light Control***


**Overview**

This project focuses on optimizing traffic light control to prioritize emergency vehicles at intersections, ensuring they experience minimal delays. Using a simulation environment based on SUMO (Simulation of Urban MObility), the project demonstrates how traffic lights can dynamically adapt in real-time to the presence of emergency vehicles, giving them the highest priority in the traffic flow. The simulation framework can also adjust traffic lights based on general vehicular density, although the primary focus is on emergency vehicle prioritization.

**Features**
- Real-time Emergency Vehicle Detection: The system detects emergency vehicles approaching intersections and instantly changes the traffic light to green for the relevant lane, minimizing delays and ensuring quick passage through intersections.

- Dynamic Traffic Light Control: Traffic lights are dynamically adjusted based on the presence of emergency vehicles, overriding other traffic considerations to prioritize these vehicles.

- Simulation with SUMO: The project leverages the SUMO traffic simulation framework, which provides a realistic environment for testing and visualizing the traffic light control logic.

- Rule-based Traffic Management: The control logic is implemented using a simple yet effective rule-based approach, allowing for immediate response to emergency vehicles without requiring complex algorithms or machine learning models.

**How It Works**

1. Initialization:

The SUMO simulation is started with a specified configuration file, setting up the traffic environment.

2. Emergency Vehicle Detection:

At every simulation step, the system checks the lanes controlled by each traffic light for the presence of emergency vehicles (identified by a specific vehicle type, e.g., DEFAULT_CONTAINERTYPE for red container trucks).

3. Traffic Light Adjustment:

If an emergency vehicle is detected in any lane, the traffic light immediately switches to green for that lane, ensuring the vehicle does not have to wait at the intersection.
If no emergency vehicle is detected, the system could revert to normal traffic light management based on vehicle density (this feature can be customized as needed).

4. Real-time Simulation:

The system runs continuously, adjusting traffic lights at every simulation step to respond to the dynamic traffic conditions in real-time.

**Usage**
To run the project, follow these steps:

1. Prerequisites:

Install SUMO and its Python bindings (traci and sumolib).
Ensure you have a suitable SUMO configuration file (.sumocfg) to run the simulation.

2. Running the Simulation:

Execute the main script, which starts the SUMO simulation and applies the dynamic traffic light control logic.

3. Customization:

Modify the vehicle type identifier to match your emergency vehicles.
Adjust the simulation configuration and traffic light logic as needed to fit different scenarios.

**Project Structure**

- main.py: The main script that initializes the simulation and controls the traffic lights.
- sumo.sumocfg: The SUMO configuration file that sets up the traffic simulation environment.
- README.md: This file, providing an overview of the project.
- 
**Future Work**
  
- Enhanced Vehicle Detection: Integrating more sophisticated vehicle detection techniques using computer vision or sensor data.
- Machine Learning Integration: Exploring machine learning models to optimize traffic light control based on historical traffic patterns and predictive analytics.
- Scalability: Extending the system to handle larger and more complex traffic networks with multiple intersections.

**Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

**License**
This project is licensed under the MIT License - see the LICENSE file for details
