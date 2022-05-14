Here is library for conversion oscillogram files to data, written on C++ and compiled for Python under Linux. 
Windows version in a feature plan. 

This lib I have tested with oscillogram files such devices as:

    Sepam 80 - using COMTRADE standard 2001 года
    ABB REF620 - using COMTRADE standard 1999 года
    ABB REF615 – using COMTRADE standard 1999 года
    
Using this lib with osscillograms different type of devices with standard 1999 possible, but not guaranteed stable work. Because of makers can do some things out of standard in their solutions. 
Using this lib with different standard than 1999-2001 completely not guaranteed. 

Using lib under Linux.

In the same folder, where you run Python file should be placed library file

relaycomtradelib.cpython-36m-x86_64-linux-gnu.so

The simple code on Python:

    import relaycomtradelib

    cfg_file = 'path_to_your_cfg_file_osscillogram'   # Obligatary parameter
    dat_file = 'path_to_your_dat_file_osscillogram'   # Obligatary parameter
    out_csv  = 'path_to_your_output_data_csv'         # Obligatary parameter. Set empty string '' if you planing to use only data, without output data to file

    data = relaycomtradelib.comtrade(cfg_file, dat_file, out_csv)

Variable ‘data’ – the list, that has internal lists of data in string format. 
Because of in oscillogram a lot of types of data – int, float, string, time etc, I decided to use most common format – string.
You have to convert from string to needed data if necessary.

Working example shown in file

start_current.py

Run that file under Linux:

python3 start_current.py

    "Set path to your oscillograms and Enter. Or just press Enter, then programm wiil seek oscillograms in same folder"

The script ask you to point path to oscillogram storage. If just press Enter, script will try to find oscillograms files in the same folder where it was run.

    Set your output folder oscillograms with start currents and Enter. If just Enter there is will not output files, just report.csv

If you need that found files with starting currents to copy somewhere, set the path or folder name for example NEW.
If oscillograms with starting currents will be found, program will make directory NEW and copy there oscillograms, with the same internal structure of directories.
If you do not want to copy this oscillogram files, just simple press Enter.

At the end of work, if oscillogram files with starting currents will be found, the program will make report file in CSV format, where will be paths to found files. 

In the “examples” directory put the output file, which lib can convert data from oscillogram, if you pointed not empty variable – out_csv, in above example code.
