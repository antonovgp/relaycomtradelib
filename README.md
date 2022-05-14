# relaycomtradelib

Библиотека для конвертации файлов осциллограмм в данные, написанная на С++ и скомпилирована для Python под Linux.
Версию для Windows сделать пока в будущих планах.

Данную библиотеку я протестировал для файлов осциллограмм таких устройств как: 

    Sepam 80 - использует COMTRADE стандарт 2001 года
    ABB REF620 - использует COMTRADE стандарт 1999 года
    ABB REF615 - использует COMTRADE стандарт 1999 года

Использование библиотеки на осциллограммах терминалов с стандартом 1999 года, возможно, но не гарантируется стабильная работа. 
Поскольку производители могут отходить от используемых стандартов в своем изделии. 

Использовании библиотеки на осциллограммах с стандартом отличным от 1999-2001 года, совсем не гарантируется. 

Использование библиотеки под Linux.

В той же папке, откуда вы запускаете файл Python должен лежать файл библиотеки

relaycomtradelib.cpython-36m-x86_64-linux-gnu.so

Простой код на Python:

    import relaycomtradelib

    cfg_file = 'path_to_your_cfg_file_osscillogram'   # Obligatary parameter
    dat_file = 'path_to_your_dat_file_osscillogram'   # Obligatary parameter
    out_csv  = 'path_to_your_output_data_csv'         # Obligatary parameter. Set empty string '' if you planing to use only data, without output data to file

    data = relaycomtradelib.comtrade(cfg_file, dat_file, out_csv)

Переменная 'data' имеет структуру вложенных списков, в которых данные в строковом формате. 
Из-за того, что в осциллограмме много типов данных - int, float, string, time итд, я решил использовать общий формат - строковый.
Используйте конвертацию в нужные данные из строки, если необходимо.

Пример работающей реализации показан в файле 
start_current.py

Запустите файл под Linux:

python3 start_current.py

    "Set path to your oscillograms and Enter. Or just press Enter, then programm wiil seek oscillograms in same folder"

Программа попросит вас указать путь к папке с осциллограммами. Если просто нажать Enter, программа будет пробовать искать файлы с осциллограммами в папке запуска. 

    Set your output folder oscillograms with start currents and Enter. If just Enter there is will not output files, just report.csv

Если нужно, чтобы найденные файлы с пусковыми токами скопировать куда нибудь отдельно, укажить путь или название папки, например NEW.
Если осциллограммы с пусковыми токами будут найдены, программа создаст папку NEW и скопирует туда осциллограммы, сохраняя структуру вложенных папок. 
Если файлы вам копировать не нужно, просто нажмите Enter. 

По завершению работы, если файлы осциллограмм с пусковыми токами будут найдены, программа создаст файл отчета в формате CSV, где будут пути к найденным файлам. 

В папке examples лежит для примера файл, в который библиотека конвертирует данные из осциллограммы, если вы указали непустым - out_csv.



###########################################################
# Enlgish description
###########################################################


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
