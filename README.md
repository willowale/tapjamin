To simulate touches on the iOS Sim, we leverage Apple's simctl tool, with Python.

For direct touch simulation, simctl does not natively support direct touch simulation.

For this, we will need to integrate with accessibility frameworks, like XCTest, or WebDriverAgent.

We communicate with the AVC of the Linux host over the local network with Python's socket library.

Pre Reqs:

Install WebDriverAgent or use XCTest to control the sim.
WebDriver Agent can be found at https://github.com/facebookarchive/WebDriverAgent.

A Linux machine with an HTTP server will listen for the commands. The script assumes we are sending a JSON payload to the AVC to get a response.

We will need ot install "requests" for HTTP communication. This will be done via "pip install requests".


The script uses the WebDriverAgent or XCTest to perform a touch. Replace the URL with the automation endpoint.

If need be, however our target intended has this setup, "linuxsetup.py" is here in case the Linux machine is not setup to handle incoming commands.


Notes:

Replace the placeholders (SIMULATOR_UDID, IPs, ports, etc) with actual values.

For advanced iOS touch simulation, WebDriverAgent is recommended since simctl doesn't support taps directly.

Both devices need to be on the same network for communication.
