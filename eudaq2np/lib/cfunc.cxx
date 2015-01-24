
#include <stdio.h>
#include "eudaq/FileReader.hh"
#include "eudaq/PluginManager.hh"
#include "eudaq/OptionParser.hh"
#include "eudaq/StandardEvent.hh"

#include <iostream>
#include <vector>
#include <map>

#ifndef WIN32
#include <inttypes.h> 
#endif

#include "cfunc.h"

using namespace eudaq;

void eudaq_data_map(const std::string & filename, unsigned int begin, unsigned int end, std::map<std::string, std::vector<data_row> > & data_map)
{
  // Create a reader for this iframele
  eudaq::FileReader reader(filename);

  eudaq::PluginManager::Initialize(reader.GetDetectorEvent());

  // Display the actual iframelename (argument could have been a run number)
  //std::cout << "Opened file: " << reader.Filename() << std::endl;
  while (reader.NextEvent()) {
      if (reader.GetDetectorEvent().IsEORE()) {
          //std::cout << "End of run detected" << std::endl;
          // Don't try to process if it is an EORE
          break;
      }
      unsigned int eventnumber=reader.GetDetectorEvent().GetEventNumber();
      if (eventnumber<begin){
          continue;
      }
      if (eventnumber>=end){
          break;
      }

      try {
        unsigned int eventnumber=reader.GetDetectorEvent().GetEventNumber();
        eudaq::StandardEvent sev =  eudaq::PluginManager::ConvertToStandard(reader.GetDetectorEvent());
        //std::cout << sev << std::endl;
      
        for(unsigned int iplane = 0; iplane < sev.NumPlanes(); iplane++){
          const StandardPlane & plane = sev.GetPlane(iplane);
            
	        //std::cout<< " sensor=" << plane.Sensor() << " type=" << plane.Type() << "" << std::endl;

	        for(unsigned int iframe = 0; iframe < plane.NumFrames(); iframe++){
		        
		        const std::vector<double> & xv = plane.XVector(iframe);
		        const std::vector<double> & yv = plane.YVector(iframe);
		        const std::vector<double> & pix = plane.PixVector(iframe);
		
		        for(unsigned int ipix = 0; ipix < pix.size(); ipix++){
                      data_row data_pix = {eventnumber,plane.TLUEvent(), iplane, iframe, xv[ipix],  yv[ipix], pix[ipix]};
		              data_map[plane.Type()].push_back(data_pix);
		        }                  
	        }
        }
        
      } catch (const eudaq::Exception & e) {
        //std::cout << "No " << type << " subevent in event "  << reader.GetDetectorEvent().GetEventNumber() << std::endl;
      }
    }
}


