import xml.etree.ElementTree as ET


def extract_lane_ids(net_file):
    tree = ET.parse(net_file)
    root = tree.getroot()

    lane_ids = []
    for lane in root.findall(".//lane"):
        lane_id = lane.get('id')
        if lane_id:
            lane_ids.append(lane_id)

    return lane_ids


def main():
    net_file = 'route.net.xml'
    lane_ids = extract_lane_ids(net_file)

    with open('lane_ids.txt', 'w') as f:
        for lane_id in lane_ids:
            f.write(f"{lane_id}\n")

    print(f"Extracted {len(lane_ids)} lane IDs to lane_ids.txt")


if __name__ == "__main__":
    main()
