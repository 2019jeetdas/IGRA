Integrated Global Radiosonde Archive (IGRA) Version 2 Readme File 

Imke Durre (imke.durre@noaa.gov) - last updated August 2016


TABLE OF CONTENTS

I.    OVERVIEW
II.   WHAT'S NEW IN IGRA 2
III.  DOWNLOAD QUICK START
IV.   CONTENTS  OF FTP DIRECTORY
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

I. OVERVIEW

This file provides guidance for how to navigate the FTP directory for 
Integrated Global Radiosonde Archive (IGRA). It provides a brief overview of 
what is new in IGRA 2, step-by-step instructions for downloading desired data 
and metadata, and an explanation of the contents of the directory and 
all of its subdirectories.
The formats of the various types of files available are described in 
separate documents.

IGRA 2 replaces IGRA 1 as NCDC's baseline upper-air dataset.
IGRA 1 continues to be available in a subdirectory v1 of this FTP directory,
but is no longer updated.

Send any feedback to the IGRA Team at ncei.igra@noaa.gov.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

II. WHAT'S NEW IN IGRA 2

Following is a summary of what is new and different in IGRA 2 compared to 
IGRA 1.

  - More Data: IGRA 2 contains nearly twice as many stations and 30% more 
    soundings than IGRA 1.

  - Longer Records: The earliest year with data in IGRA 2 is 1905, and 
    there are several hundred stations with data before 1946. In IGRA 1, 
    only one station's record extends back to before 1946, and its record 
    begins in 1938.

  - Ships and Ice Islands: IGRA now contains data from 112 floating stations, 
    including 17 fixed weather ships and buoys, 72 mobile ships, and 23 
    Russian ice islands.

  - Additional Variables: 
    1. Reported relative humidity and time elapsed since launch are now 
       provided in the sounding data files whenever they are available. This
       allows for the inclusion of humidity observations prior to 1969,
       the first year with dewpoint depression in IGRA 1.
    2. The derived-parameter files now include both reported and calculated 
       relative humidity. In soundings in which humidity is reported only
       as relative humidity, all moisture-related derived parameters are based
       on the reported relative humidity. In all other soundings, they are
       based on dewpoint depression/calculated relative humidity.
    3. In addition to monthly means of geopotential height, temperature,
       an wind, monthly means of vapor pressure are now also available.
    For details on these variables and associated changes in data format, 
    see the respective format descriptions.

  - Additional Data Sources:
    1. IGRA 2 is constructed from a total of 33 data 
       sources, including 10 of the 11 data sources used in IGRA 1. 
    2. To improve spatial coverage, data received via the Global 
       Telecommunications System (GTS) by the U.S. Air Force 
       14th Weather Squadron replace the less complete NCDC/NCEP-based 
       1973-1999 GTS data which was the largest contributor of data to
       IGRA 1. This change particularly improves the spatial coverage 
       over China in the 1970s and 1980s.
    3. Daily updates now come not only from the GTS, but, for U.S. stations,
       also directly from the U.S. National Weather Service (NWS), resulting
       in higher-precision, higher-vertical resolution data for U.S. 
       stations in near real-time.
    4. Global coverage prior to the 1970s was enhanced primarily by the 
       "C-Cards" and "MIT" datasets from the National Centers for 
       Atmospheric Research as well as Version 1.01 of the Comprehensive 
       Historical Upper Air Network from the Institute for Atmospheric 
       and Climate Science at ETH Zurich in Switzerland.
    5. Additional data sources include pilot balloon observations for 
       the United States that were digitized under the Climate Data 
       Modernization Program (CDMP), radiosonde and pilot balloon 
       observations for several countries in Africa from CDMP and  
       Meteo-France, ship and ice island observations from NCDC's archive, 
       Antarctic radiosonde observations provided by the British Antarctic
       Survey, the Historical Arctic Radiosonde Archive from the National
       Geophysical Data Center, and 1990s Indonesian radiosonde data
       provided by the Japan Agency for Marine-Earth Science and Technology.

  - Eleven-character Station IDs: To accommodate stations other than those
    with world Meteorological Organization (WMO) station numbers, IGRA now 
    uses 11-character station identifiers that consist of a two-character 
    country code, a one-character station network code, and an 
    eight-character station identifier.
    The station IDs for WMO stations, which account for approximately 80% of 
    the IGRA 2 stations, contain a network code of "M" followed by "000" 
    followed by the five-digit WMO identification number. For example, the 
    IGRA 2 station identifier for Key West (WMO# 72201) is USM00072201. 
    The remaining stations are identified by ship call signs (network
    code "V"), Weather Bureau, Army, Navy (WBAN) numbers ("W"), 
    International Civil Aviation Organization call signs ("I"), and 
    specially constructed identifiers ("X"). 
    For more details, see the format description of the station list.

  - Changed station list format: The order of fields in the station list
    has been changed for consistency with some of NCDC's other datasets. In
    addition, the identification of stations as GCOS Upper Air Network (GUAN) 
    and Lanzante/Klein/Seidel (LKS) stations has been removed. Relevant LKS 
    stations are captured within the RATPAC product, and the latest list of 
    GUAN stations is best obtained directly from the WMO.

  - Additional Information in Sounding Headers:
    1. Header records in sounding data files now include two data source codes, 
       one for pressure levels and one for non-pressure levels. 
    2. In order to be able to indicate the position of mobile stations at 
       each observation time, fields for the latitude and longitude have
       been added to the sounding headers in data files. For fixed stations, 
       including moored ships, the coordinates entered into these fields are 
       always the same as those shown in the IGRA station list since the 
       actual position is generally not known on a sounding-by-sounding
       basis at those stations. Coordinates are not included in the sounding 
       headers of the derived-parameter files since sounding-derived 
       parameters are provided only for fixed stations.
    For more details, see the format description of the data files.

  - Soundings Without Observation Hour: Unlike IGRA 1, IGRA 2 contains 
    soundings from some data sources in which the time of day at which 
    an observation was made is indicated only by the release time, i.e., 
    the time at which the balloon was launched, and the 
    nominal/observation hour is missing (= 99). Since conventions for 
    determining the observation hour from the release time vary over
    time and among agencies, no attempt has been made to infer the 
    observation hour from the release time in IGRA 2.

  - Modified Level Type Indicators: The meaning of the first digit of
    the level type indicator in sounding records has changed as follows: 

    Blank is no longer used.
    1 continues to indicate a standard pressure level.
    2 indicates a non-standard pressure level regardless of whether it
      contains thermodynamic data or only wind data.
    3 indicates a non-pressure level, which always only contains wind 
      observations in IGRA 2.

  - Non-Pressure Surface Levels: Unlike in IGRA 1, IGRA 2 contains surface
    levels that do not contain a pressure value. Such levels only appear in
    soundings that consist entirely of data levels whose vertical coordinate is
    identified only by height. 

  - Methodological Changes: 
    1. The process of choosing which data sources contribute to each station 
       record as well as the process of merging multiple data sources into 
       one station record were redesigned to increase automation, accommodate 
       a greater variety of data sources and station identifiers, and preserve 
       a larger number of pilot balloon observations. 
    2. In addition, some minor improvements were made to the quality assurance 
       procedures, including, most notably, the addition of basic checks on 
       elapsed time and relative humidity as well as improved selection of 
       a single surface level within soundings in which multiple levels are 
       identified as surface. 
    3. The compositing procedure was redesigned. Stations are now composited
       when they are within 5 km of each other and their records do not contain
       soundings at concurrent observation times.
    All of these modifications will be described in greater detail in a 
    future article.

  - Additional Station History Information:
    1. The IGRA metadata file, which contains documented information about
       the instrumentation and observing practices at many stations, has been
       augmented with additional records extracted from the Gaffen (1996)
       collection that formed the basis for the original IGRA metadata.
       The additional records are for nearly 700 IGRA 2 stations for 
       which no data was available in IGRA 1. 
    2. To provide information on instrumentation used in recent years for which
       documented station history information is not available in the IGRA
       IGRA metadata file, the WMO radiosonde/sounding system and measuring
       equipment codes contained in Global Telecommunications System messages
       are also supplied in separate files for the years 2000-2013. Note that
       these codes have not been checked for accuracy and are provided 
       as received.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

III. DOWNLOAD QUICK START

Start by downloading "igra2-station-list.txt", which has metadata for all stations
in the dataset. You can find this file in the same location where this README
file resides, i.e., by going to directory pub/data/igra/
at ftp.ncdc.noaa.gov or pointing your browser to
http://www1.ncdc.noaa.gov/pub/data/igra/ .

Then, to find and download the data for a specific station, proceed
as follows:

  - Find the station's name in "igra2-station-list.txt" and note its station
    identification code (e.g., Key West is "USM00072201").

 - Decide which of the following types of data you desire, navigate
   to the appropriate subdirectory, and download the desired 
   ZIP-compressed data file(s) and associated format documentation. 

    For individual soundings for the full period of record, go to
      subdirectory data/data-por and download the file containing the desired
      station ID in its filename (e.g., USM00072201-data.txt).
    For individual soundings from this year only, go to data/data-y2d and
      download the file containing the desired station ID in its filename.
    For period-of-record sounding-derived moisture, stability, and other 
      parameters, go to derived/derived-por and download the file whose name
      contains the desired station ID (e.g., USM00072201-drvd.txt).
    For monthly means for the full period of record, go to monthly/monthly-por
      download the file(s) for the desired variable and nominal hour 
      (e.g., temp_00z-mly.txt.zip for 0000 UTC temperature).
    For monthly means for only the last calendar month, go to 
      monthly/monthly-upd and download the file(s) for the desired variable 
      and nominal hour.
  
  - Uncompress the downloaded file using an uncompressing software (e.g., 
    7-Zip or winzip under Windows or the "gunzip" command under Linux).

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

IV. CONTENTS OF FTP DIRECTORY(ftp.ncdc.noaa.gov/pub/data/igra/)

---------------------------------
Main level (pub/data/igra/):
---------------------------------

data/				contains IGRA 2 sounding data files.
derived/			contains IGRA 2 derived sounding parameters.
history/			contains IGRA 2 station history information.
monthly/			contains IGRA 2 monthly means 
v1/				contains IGRA 1 files (see v1/readme.txt)

igra2-country-list.txt		is a list of country codes used in IGRA 2
				station identifiers.
igra2-list-Format.txt		is the description of the format of the IGRA 2
				station list.
igra2-station-lsit.txt		is the list of all IGRA 2 stations and their
				name, location, period Of record, and 
				number of soundings.
igra2-readme.txt		is this file.
igra2-us-states.txt		is a list of all two-letter state codes shown
				in the IGRA 2 station list.
status.txt                      notes on the current status of IGRA's 
                                online files
---------------------------------
Subdirectory data/ (pub/data/igra/data/):
---------------------------------

data-por/			contains sounding data for the full period 
				of record.
data-y2d/			contains sounding data since January 1 
				of the current or previous year.
igra2-data-format.txt		is the description of the format of the 
				sounding data files.

---------------------------------
Subdirectory derived/ (pub/data/igra/derived/):
---------------------------------

derived-por/			contains sounding-derived parameters for the full period of
record.
igra2-derived-format.txt	is the description of the format of the
                                sounding-derived parameter files.

---------------------------------
Subdirectory history/ (pub/data/igra/history/):
---------------------------------

igra2-metadata.txt		is documented station history information 
				for IGRA 2 stations.
igra2-metadata-readme.txt	is a description of the format and origin of
				the documented station history information.
wmo-history.txt			is a description of the format of the WMO 
				instrument code history files.
wmo-sonde-history.txt		is a list of the radiosonde codes extracted 
				from GTS messages received at NCDC.
wmo-wndeq-history.txt		is a list of the measurement equipment codes 
				extracted from GTS messages received at NCDC.

---------------------------------
Subdirectory monthly/ (pub/data/igra/monthly/):
---------------------------------

monthly-por/			contains monthly means for the full period of 
				record.
monthly-upd/			contains monthly means for the last available 
				month.
igra2-monthly-format.txt	is the description of the format of the
				monthly-mean files.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

