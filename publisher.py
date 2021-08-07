import time

from pydust import core

import pickle
def main():
    # initialises the core with the given block name and the directory where the modules are located (default "./modules")
    dust = core.Core("classify_pub", "./modules")

    # start a background thread responsible for tasks that shouls always be running in the same thread
    dust.cycle_forever()

    # load the core, this includes reading the libraries in the modules directory to check addons and transports are available
    dust.setup()

    # set the path to the configuration file
    dust.parse_configuration_file("configuration.json")

    # connects all channels
    dust.connect()
    time.sleep(1)
    # declare a bytes-like payload object
    with open("demo.jpg", "rb") as image:
        f = image.read()
        f=bytearray(f)

        # publishes the payload to the given channel (as defined by the configuration file)
    payload = "test".encode("ascii")
    dust.publish("publish-mqtt", bytes(f))

    time.sleep(1)

    # disconnects all channels and flushes the addon stack and transport.
    dust.disconnect()

    # stops the background thread started by cycleForever() and wait until the thread has finished its tasks before exiting the application
    dust.cycle_stop()

if __name__ == "__main__":
    main()