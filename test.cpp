#define CIRCADIAN_TEST
#include "circadian.cpp"
#include <cassert>
int main() {
    assert(day(QDateTime(QDate(2026,3,20),QTime(12,0),QTimeZone::UTC),0,0));
    assert(!day(QDateTime(QDate(2026,3,20),QTime(0,0),QTimeZone::UTC),0,0));
    assert(day(QDateTime(QDate(2026,6,21),QTime(0,0),QTimeZone::UTC),89,0));
    assert(!day(QDateTime(QDate(2026,12,21),QTime(12,0),QTimeZone::UTC),89,0));
    try { coords(91,0,"bad"); return 1; } catch(const std::runtime_error &) {}
    return 0;
}
