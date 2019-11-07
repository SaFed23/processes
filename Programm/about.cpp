#include <iostream>
#include <fstream>
#include <wchar.h>
#include <cstring>
using namespace std;

class About{
    wchar_t* text;

public:

    wstring getStr() {
        wfstream file("about.txt");
        wstring str;
        wstring buf;
		while(!file.eof()) {
            getline(file, buf);
            str += buf + L"\n";
        }
	    return str;
	}
};

extern "C" {
    About* About_new() { return new About(); }
    wchar_t* getStr(wchar_t* str) {
        About *about = new About();
        wcscat(str, &about->getStr()[0]);
        return str;
     }
}