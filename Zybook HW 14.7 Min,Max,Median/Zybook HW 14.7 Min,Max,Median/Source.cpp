#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // to use sort()
using namespace std;

const int NUM_VALUES = 5;

// Input NUM_VALUES of TheType into the vector parameter
template<typename TheType> void Read(vector<TheType>& list) {
    for (int j = 0; j < NUM_VALUES; ++j) {
        cin >> list.at(j);
    }
}

// Output the elements of the vector parameter
template<typename TheType> void Write(vector<TheType>& list) {
    long unsigned int j;
    for (j = 0; j < list.size(); ++j) {
        cout << list.at(j) << " ";
    }
}

// Return the min, median, and max of the vector parameter in a new vector
template<typename TheType> vector<TheType> GetStatistics(vector<TheType>& list) {
    
    TheType min, median, max;
    unsigned long int i;

    

    for (i = 0; i < list.size(); ++i) {
        if (i == 0) {
            min = list.at(i);
            max = list.at(i);
            continue;
        }

        if (list.at(i) < min) {
            min = list.at(i);
        }
        if (list.at(i) > max) {
            max = list.at(i);
        }
        if (i == 2) {
            median = list.at(i);
        }
    }
    vector<TheType> newlist;

    newlist.push_back(min);
    newlist.push_back(median);
    newlist.push_back(max);
    
    return newlist;

    
    

}   

// Read values into a vector, sort the vector, output the sorted vector,
// then output the min, median, and max of the sorted vector
template<typename TheType> void Run(vector<TheType>& list) {
    
    Read(list);
    sort(list.begin(), list.end());
    Write(list);
    cout << endl; 
    list = GetStatistics(list);
    Write(list);
    cout << endl;


}

int main() {
    vector<int> integers(NUM_VALUES);
    Run(integers);
    cout << endl;
    
    vector<double> doubles(NUM_VALUES);
    Run(doubles);
    cout << endl;

    vector<string> strings(NUM_VALUES);
    Run(strings);
    
    return 0;
}