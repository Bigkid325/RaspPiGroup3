import time
from av_nn_tools import NNTools
from av_parse_data import ParseData
SERVO_TEST_SETTING = "data/set_servo_test.json"
SERVO_MODEL = 'models/servo_model.pth'
TEST_DATA = './data/list/final_test.csv'
IMAGE_FILE = "data/images/03_06_2020_0/output_0002/i0000000_s15_m15.jpg"
servo_test = NNTools(SERVO_TEST_SETTING)
servo_test.load_model(SERVO_MODEL)
servo_test.test(TEST_DATA)
start_time = time.time()
servov=servo_test.predict(IMAGE_FILE)
end_time = time.time()
print(servov)
print(end_time-start_time)