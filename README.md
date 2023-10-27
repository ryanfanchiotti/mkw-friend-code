# mkw-friend-code

python scripts to find mario kart wii friend codes with patterns (e.g. `1165-6511-5111`) and calculate when to create a mkw profile on wiimmfi so that you will receive one

info: mario kart wii creates friend codes from 9 digit player id numbers which increase by one every time a new profile is made; each player id is displayed as created or not created on wiimmfi's website

important files:

- `pid_tester_dp` is currently the fastest of the pid testers; it will repeatedly check if friend codes close to your target code have been created on wiimmfi

- `current_pid` will find the current pid on the wiimmfi servers

- `list_fc_range` will generate friend codes that correspond to pids and can filter for certain patterns depending on which filter is being used

credits: wiimm and leseratte for pid to fc algorithm and wiimmfi servers/website

notes: you will have to edit and save each file before running to customize output, google chrome must be installed
