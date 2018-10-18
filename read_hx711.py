import sys
import time
import logging
import argparse
import json
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                    stream=sys.stdout)
logger = logging.getLogger(__name__)
from hx711 import HX711
parser = argparse.ArgumentParser()
parser.add_argument('--dout', help='Serial Data Output pin number (BCM)', type=int, required=True)
parser.add_argument('--pd_sck', help='Power Down and Serial Clock Input pin number (BCM)', type=int, required=True)
parser.add_argument('--level', help='Logging level', type=str, default=logging.INFO)
parser.add_argument('--convert', help='Convert ADC decimal output to load (N). '
                                      'Conversion slope and intercept are stored in calibration.json file.',
                    action='store_true')
# Calibration file example: {'slope': '-0.000409291', 'intercept': '-3.59066'}
calibration_file = 'calibration.json'

if __name__ == '__main__':
    args = parser.parse_args()
    # FIXME: Logging level is not set on all loggers
    logger.info(f'Set level to {args.level}')
    logger.setLevel(level=args.level)
    if args.convert:
        logger.info(f'Read calibration data from {calibration_file}')
        with open(calibration_file) as f:
            calibration_data = json.load(f)
        logger.info(f'Calibration data: {calibration_data}')
        # Convert to float
        for key in ('slope', 'intercept'):
            assert key in calibration_data, f'No "{key}" in {calibration_file}'
            calibration_data[key] = float(calibration_data[key])
        logger.debug(f'Calibration data after type conversion: {calibration_data}')
    hx_kwargs = {'dout_pin': args.dout, 'pd_sck_pin': args.pd_sck, 'gain': 128, 'channel': 'A'}
    logger.info(f'Initialize HX711 with {hx_kwargs}')
    hx = HX711(**hx_kwargs)
    #logger.info('Reset HX711')
    #result = hx.reset()
    logger.info(f'Reading values from channel {hx.channel}, press Ctrl-C to quit...')
    try:
        while True:
            decimal = hx.read_decimal()
            if not args.convert:
                logger.info(f'CH {hx.channel}: {decimal}')
            else:
                load_N = float(calibration_data['slope'])*decimal + float(calibration_data['intercept'])
                logger.info(f'CH {hx.channel}: {load_N} N')
            # Pause for half a second
            time.sleep(0.5)
    except KeyboardInterrupt:
        logger.info('Keyboard interrupt detected, exiting...')
        # TODO: Clear GPIO pins
