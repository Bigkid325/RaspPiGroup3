from av_nn_tools import NNTools

TRAIN_DATA = './data/list/newtrain.csv'
TEST_DATA = './data/list/final_test.csv'

SERVO_TRAIN_SETTING = "data/set_servo_train.json"
SERVO_TEST_SETTING = "data/set_servo_test.json"
SERVO_MODEL = 'models/servo_model.pth'

MOTOR_TRAIN_SETTING = "data/set_motor_train.json"
MOTOR_TEST_SETTING = "data/set_motor_test.json"
MOTOR_MODEL = 'models/motor_model.pth'

#IMAGE_FILE = "data/images/03_06_2020_0/output_0002/i0000000_s15_m15.jpg"

# servo_train = NNTools(SERVO_TRAIN_SETTING)
# servo_train.train(TRAIN_DATA)
# servo_train.save_model(SERVO_MODEL)

servo_test = NNTools(SERVO_TEST_SETTING)
servo_test.load_model(SERVO_MODEL)
servo_test.test(TEST_DATA)