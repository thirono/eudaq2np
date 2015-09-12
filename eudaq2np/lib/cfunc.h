#include <stdio.h>
#ifdef WIN32
#include <stdint.h>
#endif

#pragma pack(push, 1)

struct data_row {
  uint32_t eventnumber;
  uint32_t tluevent;
  uint16_t plane;
  uint16_t frame;
  uint16_t x;
  uint16_t y;
  uint16_t val;
};

void eudaq_data_map(const std::string & filename, unsigned int begin, unsigned int end, std::map<std::string, std::vector<data_row> > & data_map);

