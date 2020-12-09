# swarmbots

Install map merge: `git clone https://github.com/hrnr/m-explore.git`

- run world and initial robots: `roslaunch swarmbots main.launch world:=stage_4 robots:=2`
- toggle swarm orders: `rosrun swarmbots command.py`
- view map in rviz:
  - launch `rviz`
  - set Fixed Frame to `world`
  - Add by topic `/map`
