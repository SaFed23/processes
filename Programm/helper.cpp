#include <iostream>
#include <fstream>
#include <wchar.h>
#include <cstring>
using namespace std;

void print_delete_process(wchar_t* str) {
    wfstream file;
    file.open("delete_processes.txt", std::ios::app);
    file << str << L"\n";
    file.close();
}

void print_all_processes(wchar_t* str) {
    wfstream file;
    file.open("all_processes.txt", std::ios::out);
    file << str;
    file.close();
}


extern "C" {
    void print_delete_processes_in_file(wchar_t* str) { print_delete_process(str); };
    void print_all_processes_in_file(wchar_t* str) { print_all_processes(str); };
    wchar_t* message_about_process(wchar_t* str) {
        wcscat(str, L", hello!");
        return str;
    };
}
