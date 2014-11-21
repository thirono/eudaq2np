#include <stdio.h>

struct data_row {
  uint32_t tluevent;
  uint32_t plane;
  uint32_t frame;
  uint32_t id;
  double x;
  double y;
  double val;
};

void eudaq_data_vector(const std::string & file_name, const std::string & type, std::vector<data_row> &);