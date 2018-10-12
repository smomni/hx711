import sys
import time
import logging
import argparse
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                    stream=sys.stdout)
logger = logging.getLogger(__name__)
from hx711 import HX711
parser = argparse.ArgumentParser()
parser.add_argument('--dout', help='Serial Data Output pin number (BCM)', type=int, required=True)
parser.add_argument('--pd_sck', help='Power Down and Serial Clock Input pin number (BCM)', type=int, required=True)


if __name__ == '__main__':
    args = parser.parse_args()
    hx_kwargs = {'dout_pin': args.dout, 'pd_sck_pin': args.pd_sck, 'gain': 128, 'channel': 'A'}
    logger.info(f'Initialize HX711 with {hx_kwargs}')
    hx = HX711(**hx_kwargs)
    #logger.info('Reset HX711')
    #result = hx.reset()
    logger.info(f'Reading values from channel {hx.channel}, press Ctrl-C to quit...')
    try:
        while True:
            voltage = hx.read()
            logger.info(f'CH {hx.channel}: {voltage} V')
            # Pause for half a second
            time.sleep(0.5)
    except KeyboardInterrupt:
        logger.info('Keyboard interrupt detected, exiting...')
