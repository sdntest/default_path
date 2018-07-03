#!/bin/bash
vnstat -i s1-eth2 -tr 30 > load_s1-s2 &
vnstat -i s1-eth3 -tr 30 > load_s1-s6 &
vnstat -i s1-eth4 -tr 30 > load_s1-s7 &
vnstat -i s2-eth2 -tr 30 > load_s2-s3 &
vnstat -i s2-eth3 -tr 30 > load_s2-s5 &
vnstat -i s3-eth4 -tr 30 > load_s3-s4 &
vnstat -i s3-eth5 -tr 30 > load_s3-s7 &
vnstat -i s4-eth2 -tr 30 > load_s4-s5 &
vnstat -i s5-eth6 -tr 30 > load_s5-s6 &
vnstat -i s1-eth1 -tr 30 > load_h1-s1 &
vnstat -i s5-eth1 -tr 30 > load_h2-s5 &
vnstat -i s5-eth2 -tr 30 > load_h3-s5 &
vnstat -i s5-eth3 -tr 30 > load_h4-s5 &
vnstat -i s3-eth1 -tr 30 > load_h5-s3 &
vnstat -i s3-eth2 -tr 30 > load_h6-s3 &


