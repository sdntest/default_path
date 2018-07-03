#!/bin/bash
iperf -c 10.0.0.2 -u -b 32M -t 100 &
iperf -c 10.0.0.3 -u -b 26M -t 100 &
iperf -c 10.0.0.4 -u -b 20M -t 100 &
iperf -c 10.0.0.5 -u -b 23M -t 100 &
iperf -c 10.0.0.6 -u -b 22M -t 100 & 
