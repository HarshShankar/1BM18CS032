# Configure RIP Routing Protocol in Routers

## Observations/Learnings
- Created a topology as shown using 3 routers and 2 pcs
- Connected the routers using _serial ports_ through _DCE_ cables 
- Configured router ip addresses using `ip address <address> <subnet_mask>`
- `encapsulation ppp` and `clock rate 64000` used to specify ppp protocol and clock rate in routers 0 and 1 for the serial ports
- Configured RIP routing using `router rip` then `network <address>` commands, where _address_ refers to the networks directly connected to the router

## Topology
![topology](topology.png)

## Router 0 Config (_10.0.0.10_)
![router0config](router0rip.png)
![router0iproute](router0showiproute.png)

## Router 1 Config
![router1config1](router1rip.png)
![router1config2](router1showiproute.png)

## Router 2 Config (_40.0.0.10_)
![router2config](router2rip.png)
![router2iproute](router2showiproute.png)

## PC0-PC1 Ping (_10.0.0.1_ -> _40.0.0.1_)
![pc0pc1ping](pc0topc1ping.png)