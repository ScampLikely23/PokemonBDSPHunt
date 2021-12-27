# PokemonBDSPHunt
Physical Hardware Needed:
Raspberry Pi (3 or 4 is recommended, I installed Raspberry Pi OS on mine)
HD Capture Card
Nintendo Switch & Dock
Specific to my setup that makes this easier in my opinion: Windows Computer



Physical Setup:
Connect your capture card to your Windows Computer or Raspberry Pi (you will need to modify the code to work for the RPI if you are not using a windows computer)
Connect your switch dock to the capture card
Make sure the raspberry pi has been powered on and connected to your local network that your PC is on

Software Setup:
You will need to install NXBT on the raspberry pi, steps to do so are here: https://github.com/Brikwerk/nxbt
Using a program like OBS Studio, confirm you are able to see the Switch Screen from your PC, your capture card may require additional drivers
Start up the NXBT web app on your RPI following the NXBT documentation
Create a controller and ensure it is connected to the Switch
Paste in the Macro for the code you need to run, adjustments will need to be made based on the Shiny Hunt you are doing. The one I am posting now 12/27 works for the Regi's

For the python script to work you will need to confirm the XY coordinates of the Run Macro and Restart Controller Button as well as the placement of the pokemon on your screen.
I will be creating a more detailed guide on this part specifically, but you will place the mouse over the specific button on your screen and enter get_cords() into the python shell to get the XY coordinates

You may also need to adjust the RGB values, currently it is set to Registeel's grey color, the code tells you what RGB value it checked, so you should be able to use the output from the code to verify it's RGB value.

Please let me know if you have any issues or questions. This is my first public project and I will attempt to keep this as updated and informative as possible

PS The Regi Macro is

HOME 0.2S

2S

Y 0.3S

1.8S

A 0.3S

2.8S

A 0.3S

25.5S

A 0.3S

7S

A 0.3S

16S

A 0.3S

1.8S

A 0.3S

0.4S
