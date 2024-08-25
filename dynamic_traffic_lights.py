import traci
import sumolib
import time

EMERGENCY_VEHICLE_TYPE = "DEFAULT_CONTAINERTYPE"

def is_emergency_vehicle(vehicle_id):
    """Check if the vehicle is an emergency vehicle by its type."""
    vehicle_type = traci.vehicle.getTypeID(vehicle_id)
    return vehicle_type == EMERGENCY_VEHICLE_TYPE

def get_emergency_vehicle_lane(controlled_lanes):
    """Check if there is an emergency vehicle on any of the controlled lanes."""
    for lane_id in controlled_lanes:
        if not lane_id.startswith(':'):  # Skip internal lanes
            vehicles = traci.lane.getLastStepVehicleIDs(lane_id)
            for vehicle_id in vehicles:
                if is_emergency_vehicle(vehicle_id):
                    return lane_id
    return None

def adjust_traffic_lights():
    traffic_lights = traci.trafficlight.getIDList()

    for tl_id in traffic_lights:
        controlled_lanes = traci.trafficlight.getControlledLanes(tl_id)

        # Check if there's an emergency vehicle on any of the lanes
        emergency_lane = get_emergency_vehicle_lane(controlled_lanes)
        if emergency_lane:
            print(f"Emergency vehicle detected on lane: {emergency_lane}")
            current_state = list(traci.trafficlight.getRedYellowGreenState(tl_id))
            controlled_links = traci.trafficlight.getControlledLinks(tl_id)

            for i, links in enumerate(controlled_links):
                if emergency_lane in links[0]:  # Give green light to the lane with emergency vehicle
                    current_state[i] = 'G'
                else:
                    current_state[i] = 'r'

            new_state = ''.join(current_state)
            traci.trafficlight.setRedYellowGreenState(tl_id, new_state)
            print(f"TL {tl_id} - Immediate green light for emergency vehicle: {new_state}")
            continue  # Skip the regular vehicle density check

        # Regular traffic light adjustment based on vehicle density (this part can remain or be removed)
        # lane_vehicle_counts = {}
        # for lane in controlled_lanes:
        #     if not lane.startswith(':'):  # Skip internal lanes
        #         count = get_vehicle_count(lane)
        #         lane_vehicle_counts[lane] = count

        # if lane_vehicle_counts:
        #     max_lane = max(lane_vehicle_counts, key=lane_vehicle_counts.get)
        #     max_vehicles = lane_vehicle_counts[max_lane]
        #     print(f"TL {tl_id} - Busiest lane: {max_lane} with {max_vehicles} vehicles")

        #     current_state = list(traci.trafficlight.getRedYellowGreenState(tl_id))
        #     controlled_links = traci.trafficlight.getControlledLinks(tl_id)

        #     for i, links in enumerate(controlled_links):
        #         if max_lane in links[0]:  # If this link controls the busiest lane
        #             current_state[i] = 'G'
        #         else:
        #             current_state[i] = 'r'

        #     new_state = ''.join(current_state)
        #     traci.trafficlight.setRedYellowGreenState(tl_id, new_state)
        #     print(f"TL {tl_id} - New state: {new_state}")
        # else:
        #     print(f"TL {tl_id} - No vehicles in controlled lanes")

def main():
    sumoCmd = ["sumo-gui", "-c",
               "C:/Users/Pujan/Downloads/Project 1- Emergency vehicle route optimization-T/Project 1- Emergency vehicle route optimization/sumo.sumocfg"]
    traci.start(sumoCmd)

    print("Traffic light IDs:", traci.trafficlight.getIDList())

    try:
        step = 0
        while traci.simulation.getMinExpectedNumber() > 0:
            traci.simulationStep()
            adjust_traffic_lights()  # Adjust traffic lights at every step
            step += 1
    except traci.exceptions.TraCIException as e:
        print(f"TraCI exception: {e}")
    finally:
        traci.close()

if __name__ == "__main__":
    main()
