🌌 Space Base

A mini command-line rocket thruster database.

Space Base is a lightweight terminal program that lets you look up rocket engines and thrusters from SpaceX, NASA, and Blue Origin using simple database-style commands.

⸻

🚀 Features
	•	Built-in database of real aerospace thrusters
	•	Clean command-style interface (database.get~…)
	•	Case-insensitive input
	•	Great starter example for learning Python dictionaries, loops, and user commands

⸻

🧩 How It Works
	1.	The program stores all thruster lists in a nested Python dictionary.
	2.	The user is dropped into a mini “shell” (database~$).
	3.	Typed commands determine what is printed.
	4.	Typing quit cleanly exits the program.

⸻

📝 Available Commands
```
database.get~thrusters.spacex      → Show SpaceX thrusters  
database.get~thrusters.nasa        → Show NASA thrusters  
database.get~thrusters.blue-origin → Show Blue Origin thrusters  
quit                               → Exit Space Base
```
All commands are not case-sensitive.

⸻

💡 Example Session
```database~$ database.get~thrusters.spacex
SpaceX's Thrusters:  Merlin 1A, Merlin 1B, Merlin 1C, Merlin 1D, ...
    
database~$ database.get~thrusters.nasa
NASA's Thrusters:  F-1, J-2, RS-25 (SSME), RL10, ...

database~$ quit
Bye!
```

![This is an image of a kitty](< img src="database-4941301_1280.png" width=10 height=10/>)
The database code is as follows:
