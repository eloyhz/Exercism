#include "trinary.h"
#include <regex>

namespace trinary {
    int to_decimal(std::string trinary_number)   {
        if (!std::regex_match(trinary_number, std::regex("[012]+")))    {
            return 0;
        }
        int decimal_value = 0;
        for (auto digit : trinary_number)    {
            decimal_value = 3 * decimal_value + (digit-'0');
        }
        return decimal_value;
    }
}  // namespace trinary
