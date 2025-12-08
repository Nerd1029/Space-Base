data = {
    "Thrusters": {
        "SpaceX": "Merlin 1A, Merlin 1B, Merlin 1C, Merlin 1D, Merlin 1D Vacuum, Kestrel, Draco, SuperDraco, Raptor 1, Raptor 2, Raptor 3, Raptor Vacuum, Starship cold-gas thrusters, Starship methalox hot-gas RCS thrusters, Starlink krypton Hall-effect thruster, Starlink argon Hall-effect thruster",
        "NASA": "F-1, J-2, J-2X, RS-25 (SSME), RS-68, RL10, XLR99, XRS-2200 (Linear Aerospike), AJ10, R-4D, OMS Engine (OMS-E), RCS thrusters (various models), AR2-3, Apollo Lunar Module Descent Engine (LMDE), Apollo Lunar Module Ascent Engine (LMAE), Saturn H-1, Saturn E-1, Aerojet M-1, Centaur G-Series engines, Pioneer Venus Monoprop thrusters, Voyager hydrazine thrusters, Dawn xenon ion engine (NSTAR), Deep Space 1 ion engine, NEXT ion engine, AEPS (Advanced Electric Propulsion System), SLS Interim Cryogenic Propulsion Stage (ICPS) RL10 variant",
        "Blue Origin": "BE-1, BE-2, BE-3, BE-3U, BE-4, BE-7, New Shepard reaction-control thrusters (hydrogen peroxide RCS), Blue Moon lander attitude-control thrusters (monoprop hydrazine RCS)",
    }
}

Thruster_dict = data["Thrusters"]
SpaceX_Thrusters = Thruster_dict["SpaceX"]
NASA_Thrusters = Thruster_dict["NASA"]
Blue_Thrusters = Thruster_dict["Blue Origin"]


while True:
    promptraw = input("database~$ ")
    prompt = promptraw.lower()

    if prompt == "database.get~thrusters.spacex":
        print("SpaceX's Thrusters: ", SpaceX_Thrusters)

    elif prompt == "database.get~thrusters.nasa":
        print("NASA's Thrusters: ", NASA_Thrusters)

    elif prompt == "database.get~thrusters.blue-origin":
        print("Blue Origin's Thrusters: ", Blue_Thrusters)

    elif prompt == "quit":
        exit("Bye!")

    elif prompt == "help":
        print('''🌌 Space Base

A mini command-line space/rocket database.

Space Base is a lightweight terminal program that lets you look up rocket engines, thrusters, and other parts, as well as entire rockets from SpaceX, NASA, Blue Origin, and more, using simple database-style commands.

⸻

🚀 Features • Built-in database of real aerospace thrusters • Clean command-style interface (database.get~…) • Case-insensitive input • Great starter example for learning Python dictionaries, loops, and user commands

⸻

🧩 How It Works

The program stores all thruster lists in a nested Python dictionary.

The user is dropped into a mini “shell” (database~$).

Typed commands determine what is printed.

Typing quit cleanly exits the program.

⸻

📝 Available Commands

database.get~thrusters.spacex      → Show SpaceX thrusters  
database.get~thrusters.nasa        → Show NASA thrusters  
database.get~thrusters.blue-origin → Show Blue Origin thrusters  
quit                               → Exit Space Base
All commands are not case-sensitive.

⸻

💡 Example Session

SpaceX's Thrusters:  Merlin 1A, Merlin 1B, Merlin 1C, Merlin 1D, ...
    
database~$ database.get~thrusters.nasa
NASA's Thrusters:  F-1, J-2, RS-25 (SSME), RL10, ...

database~$ quit
Bye!
</>

The data's code is as follows:

data = {
    "Thrusters": {
        "SpaceX": "Merlin 1A, Merlin 1B, Merlin 1C, Merlin 1D, Merlin 1D Vacuum, Kestrel, Draco, SuperDraco, Raptor 1, Raptor 2, Raptor 3, Raptor Vacuum, Starship cold-gas thrusters, Starship methalox hot-gas RCS thrusters, Starlink krypton Hall-effect thruster, Starlink argon Hall-effect thruster",
        "NASA": "F-1, J-2, J-2X, RS-25 (SSME), RS-68, RL10, XLR99, XRS-2200 (Linear Aerospike), AJ10, R-4D, OMS Engine (OMS-E), RCS thrusters (various models), AR2-3, Apollo Lunar Module Descent Engine (LMDE), Apollo Lunar Module Ascent Engine (LMAE), Saturn H-1, Saturn E-1, Aerojet M-1, Centaur G-Series engines, Pioneer Venus Monoprop thrusters, Voyager hydrazine thrusters, Dawn xenon ion engine (NSTAR), Deep Space 1 ion engine, NEXT ion engine, AEPS (Advanced Electric Propulsion System), SLS Interim Cryogenic Propulsion Stage (ICPS) RL10 variant",
        "Blue Origin": "BE-1, BE-2, BE-3, BE-3U, BE-4, BE-7, New Shepard reaction-control thrusters (hydrogen peroxide RCS), Blue Moon lander attitude-control thrusters (monoprop hydrazine RCS)",
    }
}

Thruster_dict = data["Thrusters"]
SpaceX_Thrusters = Thruster_dict["SpaceX"]
NASA_Thrusters = Thruster_dict["NASA"]
Blue_Thrusters = Thruster_dict["Blue Origin"]''')