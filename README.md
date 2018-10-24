HX711
=====

[![PyPi](https://img.shields.io/pypi/v/hx711.svg)](https://pypi.python.org/pypi/hx711)

[![Travis](https://travis-ci.org/mpibpc-mroose/hx711.svg?branch=master)](https://travis-ci.org/mpibpc_mroose/hx711)

Description
-----------
This library allows to drive a HX711 load cess amplifier with a Raspberry Pi. It just provides the capabilities:

* to set a channel gain,
* to read raw values, and
* to convert raw values to load given calibration parameters.

**This package requires RPi.GPIO to be installed in Python 3.**

Getting started
---------------

Just install by ```pip3 install git+https://github.com/smomni/hx711.git@new-feature-branch```. 
A basic usage example is given below:

```python
    #!/usr/bin/python3
    from hx711 import HX711
    

    try:
        # Use BCM numbering for pins
        hx711 = HX711(
            dout_pin=5,
            pd_sck_pin=6,
            channel='A',
            gain=64
        )

        hx711.reset()   # Before we start, reset the HX711 (not obligate)
        measures = hx711.get_raw_data(num_measures=3)
    finally:
        GPIO.cleanup()  # always do a GPIO cleanup in your scripts!

    print("\n".join(measures))
```

You can also run the `read_hx711.py` script:

```bash
    python -m read_hx711
```


License
-------
* Free software: MIT license



Credits
---------

This is a fork of https://github.com/mpibpc-mroose/hx711/.
