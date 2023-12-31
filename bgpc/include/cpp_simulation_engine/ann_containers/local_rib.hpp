#ifndef LOCAL_RIB_HPP
#define LOCAL_RIB_HPP

#include <memory>
#include <map>
#include <string>
#include "announcement.hpp"

class LocalRIB {
public:
    LocalRIB();

    std::shared_ptr<Announcement> get_ann(const unsigned short int prefix_block_id, const std::shared_ptr<Announcement>& default_ann = nullptr) const;

    void add_ann(const std::shared_ptr<Announcement>& ann);

    void remove_ann(const unsigned short int prefix_block_id);

    const std::map<unsigned short int, std::shared_ptr<Announcement>>& prefix_anns() const;

protected:
    std::map<unsigned short int, std::shared_ptr<Announcement>> _info;
};

#endif // LOCAL_RIB_HPP
