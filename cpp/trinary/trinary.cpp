#include "trinary.h"

namespace trinary {
    int to_decimal(std::string trinary_number)   {
        int decimal_value = 0;
        for (auto digit : trinary_number)    {
            if (digit > '2' || digit < '0') {
                decimal_value = 0;
                break;
            }
            decimal_value = 3 * decimal_value + (digit-'0');
        }
        return decimal_value;
    }
}  // namespace trinary
