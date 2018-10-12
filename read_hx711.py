import sys
import time
import logging
import argparse
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                    stream=sys.stdout)
logger = logging.getLogger(__name__)
from hx711 import HX711
parser = argparse.ArgumentParser()
parser.add_argument('--dout', help='Serial Data Output pin number (BCM)', type=int, required=True)
parser.add_argument('--pd_sck', help='Power Down and Serial Clock Input pin number (BCM)', type=int, required=True)
parser.add_argument('--V_ref', help='Reference voltage (V) used for converting raw output from HX711 to voltage',
                    type=float, required=True)
parser.add_argument('--scale', help='Scale factor for conversion from voltage (V) to load (N)', type=float,
                    required=True)
parser.add_argument('--level', help='Logging level', type=str, default=logging.INFO)


if __name__ == '__main__':
    args = parser.parse_args()
    # FIXME: Logging level is not set on all loggers
    logger.info(f'Set level to {args.level}')
    logger.setLevel(level=args.level)
    hx_kwargs = {'dout_pin': args.dout, 'pd_sck_pin': args.pd_sck, 'gain': 128, 'channel': 'A'}
    logger.info(f'Initialize HX711 with {hx_kwargs}')
    hx = HX711(**hx_kwargs)
    #logger.info('Reset HX711')
    #result = hx.reset()
    logger.info(f'Reading values from channel {hx.channel}, press Ctrl-C to quit...')
    try:
        while True:
            voltage_V = hx.read_voltage(v_ref=args.V_ref)
            # Convert to load
            load_N = args.scale * voltage_V
            logger.info(f'CH {hx.channel}: {load_N} N ({voltage_V} V)')
            # Pause for half a second
            time.sleep(0.5)
    except KeyboardInterrupt:
        logger.info('Keyboard interrupt detected, exiting...')
