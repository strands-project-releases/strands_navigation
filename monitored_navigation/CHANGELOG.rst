^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package monitored_navigation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.20 (2014-11-21)
-------------------
* fixing typo
* Contributors: Bruno Lacerda

0.0.19 (2014-11-21)
-------------------

0.0.18 (2014-11-21)
-------------------

0.0.17 (2014-11-21)
-------------------

0.0.16 (2014-11-21)
-------------------
* changing logging default back to true (top nav wont log nav recoveries after all)
* making sure everything preempts
* only looking at filtered argv
* Contributors: Bruno Lacerda

0.0.15 (2014-11-19)
-------------------

0.0.14 (2014-11-19)
-------------------

0.0.12 (2014-11-17)
-------------------

0.0.11 (2014-11-14)
-------------------

0.0.10 (2014-11-14)
-------------------
* replanning when failing
* checking correctness of monitored_navigation argument
* Contributors: Bruno Lacerda, Jaime Pulido Fentanes

0.0.9 (2014-11-12)
------------------
* adding monitored_nav to topological_navigation.launch. default is monitored_nav without recovery behaviours
* Contributors: Bruno Lacerda

0.0.8 (2014-11-11)
------------------

0.0.6 (2014-11-06)
------------------
* add backtrack action server launch to monitored navigation launch
* update strands config to add a monitored nav pause monitor
* Contributors: Bruno Lacerda

0.0.5 (2014-11-05)
------------------
* Adding licences and bug fix
* edited readme
* code cleaning
* created strands-specific launch file
* monitors and recoveries can only be added when action server is not running
  Signed-off-by: Bruno Lacerda <b.lacerda@cs.bham.ac.uk>
* edit readme (to be extended later)
* added service definitions for adding and removing monitor and help states to the overall monitored nav state machine
* Merge branch 'hydro-devel' of https://github.com/strands-project/strands_navigation into hydro-devel
* added strands specific config yaml
* monitor and recovery states are now defined via a config yaml file.
* Merge branch 'target' into hydro-devel
  Conflicts:
  monitored_navigation/CMakeLists.txt
* adding monitored nav launch to targets
* Contributors: Bruno Lacerda, Jaime Pulido Fentanes

0.0.4 (2014-10-30)
------------------

0.0.3 (2014-10-29)
------------------
* adding installation of monitored nav launch file
* edited launch file for new launch structure of the ui's
* Contributors: Bruno Lacerda

0.0.2 (2014-10-29)
------------------
* 0.0.1
* added changelogs
* correcting help manager include
* Merge branch 'hydro-devel' of https://github.com/strands-project/strands_navigation into hydro-devel
  Conflicts:
  message_store_map_switcher/CMakeLists.txt
* making monitored_navigation a general smach based repo that allows user to add specific instantiations of smach monitors and smach recovery behaviours
* Adding Missing TopologicalMap.msg and changing maintainer emails, names and Licences for Packages
* changing param defauls;
  aborting when continuous nav action server does not exist
* taking out distinction between local and global plan failure
  first steps to make monitored_nav scitos independent
  always oututs after help
  new action definition
  less management of new goals arriving during execution, as it was buggy
* Renamed ros_datacentre to mongodb_store
  This simply bulk replaces all ros_datacentre strings to mongodb_store strings inside files and also in file names.
  Needs `strands-project/ros_datacentre#76 <https://github.com/strands-project/ros_datacentre/issues/76>`_ to be merged first.
* changing server nave for instrospection
* adding introspection seerver to monitored_navigation
* alternative preemption
* stopped preempting monitored_nav action when help is being offered by human. more edits for proper preemption of continuous nav action
* waiting more time to timeout previous action
* missing logging component
* add logging and making preemption work after recovery
* improving preemption mechanism
* bug fix
* goals are only replaced when the new goal has the same action server name
* sovling time/duration comparisons bug
* disabling backtrack for now
* Adding machine tags to launch files
* Merge branch 'hydro-devel' of https://github.com/BFALacerda/strands_navigation into hydro-devel
* small bug fixes
* monitored navigation now does not cancel move_base when new goal arrives
* use ptu action from scitos_ptu
* Checking for preemption and added a few dependencies for recover states
* monitored navigation now does not ask for help when NavFn fails, as it usually means that the goal pose is blocked by an obstacle
* Added backwards driving behaviour
* adding state to be filled with moving backwards recovery
* - ability to preempt bumper recovery
  - send interaction_service without the prefix
* removed scitos_2d_nav of monitored_nav.launch
* added monitored navigation gui
* code cleaning
* getting preemption to work properly
* making the continuous navigation action server an input to the monitored navigation
* code cleaning
* making human help optional
* adding manager node for human help interfaces - first version
* first version of monitored navigation
* Contributors: BFALacerda, Bob, Bruno Lacerda, Chris Burbridge, Jaime Pulido Fentanes, Lars Kunze, Marc Hanheide, Nick Hawes, Nils Bore, strands
