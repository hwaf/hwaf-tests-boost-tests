#include <iostream>
#include <string>

#include "boost/version.hpp"
#include "boost/filesystem.hpp"

using namespace boost::filesystem;

int main(int argc, char* argv[])
{
  std::cout << "boost version: [" << BOOST_LIB_VERSION << "]\n";
  std::string fname = argv[0];
  if (argc > 1) {
    fname = argv[1];
  }
  std::cout << argv[1] << " " << file_size(fname) << '\n';
  return 0;
}
