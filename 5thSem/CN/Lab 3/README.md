# Configuring Static Routes in a Multiple Router Topology

## Observations/Learnings
1. Creating a multiple router topology by connecting routers through serial ports and PC-router through fast ethernet.
2. Assigning ip addresses(gateway) to routers using the same method as in [lab2](../Lab2) and PCs
3. Pinging PC1 from PC0 at this state gives **destination host unreachable**
4. Viewing the routers ip routes using `show ip route`
5. Adding static routes to the routers using `ip route <dest. network> <subnet mask> <next hop>` in privileged (`enable`) configure (`configure terminal`) mode.
6. Pinging PC1 from PC0 and PC0 from PC1 now works as expected

## Topology
![3router](3router.png)

## End-to-End Ping
![ping1](ping1.png)

## Router 0 IP Route
![iproute1](iproute1.png)

## Router 1 IP Route
![iproute2](iproute2.png)

## Router 2 IP Route
![iproute3](iproute3.png)

