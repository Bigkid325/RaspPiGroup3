import json
import pandas as pd

from av_nn_tools import NNTools
from av_parse_data import ParseData

TEST_LIST = "data/list/final_test.csv"
SETTINGS = "data/set_accuracy_test.json"

data = pd.read_csv(TEST_LIST)
parsedata = ParseData()
with open(SETTINGS) as fp:
    content = json.load(fp)

    shape = content['shape']
    servo_pred = NNTools(content["servo_setting"])
    servo_pred.load_model(content['servo_model'])

servo_count = 0

for index in range(len(data)):
    _, servo, motor = parsedata.parse_data(data["image"][index])

    pred_servo = servo_pred.predict(data["image"][index])

    if abs(servo - pred_servo) <= content['error_margin']:
        # print(servo)
        servo_count += 1
    # if (servo-15)*(pred_servo-15) >= 0:
    #     # print(servo)
    #     servo_count += 1


    if (index + 1) % 100 == 0:
        print("[%5d] servo: %2.2f " % \
              (index + 1, 100 * servo_count / (index + 1), ))

print("servo: %2.2f" % (100 * servo_count / (index + 1)))