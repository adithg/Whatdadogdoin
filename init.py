import bosdyn.client
from bosdyn.client.image import ImageClient
import cv2
from bosdyn.client.sdk import Robot
import numpy as np
from bosdyn.client import spot
from bosdyn.client.sdk import robot_state
from PIL import Image 


sdk = bosdyn.client.create_standard_sdk('spot')
robot = sdk.create_robot('192.168.80.3')
id_client = robot.ensure_client('robot-id')
robot.authenticate('user', 'password')

image_client = robot.ensure_client(ImageClient.default_service_name)
sources = image_client.list_image_sources()
print([source.name for source in sources])

def main():
    # Create a robot object
    sdk = bosdyn.client.create_standard_sdk('MySpotApp')
    robot = sdk.create_robot('your_spot_hostname')
    robot.authenticate('user', 'password')

    # Establish a connection to the robot
    robot.connect()

    # Stand up
    robot.command_spot_stance(spot.BodyControlCommand.STAND, body_height=0.4)

    # Wait for Spot to stand up
    robot_state_client = robot.ensure_client(robot_state.RobotStateClient.default_service_name)
    robot_state_reader = robot_state_client.get_robot_state()
    while not robot_state_reader.is_stand_ready:
        pass

    print("Spot is now standing.")

    # Sit down
    robot.command_spot_stance(spot.BodyControlCommand.SIT, body_height=0.0)

    # Wait for Spot to sit down
    while not robot_state_reader.is_sit_ready:
        pass

    print("Spot is now sitting down.")

    # Disconnect from the robot
    robot.disconnect()
    
    def get_spot_image():
    # Set up the SDK
        sdk = bosdyn.client.create_standard_sdk('MySpotApp')
        
        # Spot's IP address and user credentials
        spot_ip = 'spot-robot-name.local'  # Replace with the actual Spot's hostname or IP
        username = 'username'
        password = 'password'

        # Create a connection to the robot
        robot = sdk.create_robot(spot_ip)
        robot.authenticate(username, password)

        # Establish robot time sync and acquire a lease
        robot.time_sync.wait_for_sync()
        lease_client = robot.ensure_client(Robot)
        lease = lease_client.acquire()

        # Get image from Spot's front left camera
        image_client = robot.ensure_client(ImageClient)
        image_sources = image_client.list_image_sources()
        
        # Find the source name for the front left camera (you may adjust for other cameras)
        for source in image_sources:
            if source.name == 'frontleft_fisheye_image':
                image_source = source
                break
        else:
            print("Front left camera not found.")
            lease.release()
            return
        
        # Request an image from the selected camera
        image_response = image_client.get_image_from_sources([image_source], image_format='jpeg')

        # Convert the received image data to OpenCV format for processing or saving
        image_data = image_response[0].shot.image.data
        nparr = np.frombuffer(image_data, np.uint8)
        image_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Display or save the image
        cv2.imshow('Spot Front Left Camera', image_np)
        cv2.waitKey(0)  # Press any key to close the image window

        # Release the lease and shutdown the SDK
        lease.release()
        cv2.destroyAllWindows()
        sdk.shutdown()
    
    def np_to_jpg(image_np):
   
      pil_image = Image.fromarray(image_np)

      # Save the PIL Image as a JPEG file
      output_file_path = 'spot_image.jpg'  # Set the desired output file path
      pil_image.save(output_file_path, 'JPEG')

      return output_file_path

    np_to_jpg(get_spot_image())
