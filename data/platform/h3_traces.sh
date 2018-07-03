#!/bin/bash
iperf -c 10.0.0.5 -u -b 40M -t 100 &
iperf -c 10.0.0.6 -u -b 38M -t 100 &
