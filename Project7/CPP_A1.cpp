#include <iostream>
#include <vector>

using namespace std;

//-------------------------------------
//    Printing a Vector - Method
//-------------------------------------

//Prints the vector passed into the function
void printVector(vector<int> v){
	int size = v.size();
	cout << "[";
	for (int i = 0; i < size - 1; i++){
		cout << v[i] << ", ";
	}
	cout << v[size-1] << "]" << endl;
	return;
}

//-------------------------------------
//       Prime Check - Method
//-------------------------------------

// Returns true if number is prime and false if not
bool isPrime(int num){
	bool result = true;
	if (num < 0) { return false; }
	else if (num <= 2) { result = true; }
	else {
		int max = num/2;
		for (int i = max; i > 1; i--){
			if (num%i == 0) {
				result = false;
				break;
			}
		}
	}
	return result;
}

//-------------------------------------
//      Factorize - Method
//-------------------------------------
// Returns all factors of the given number in a vector
// Includes 1 and the number itself
vector<int> factorize(int n){
	vector<int> answer = {1};
	int max = n/2;
	for (int i = 2; i < max; i++){
		if (n%i == 0) {
			answer.insert(answer.end(), i);
		}
	}
	answer.insert(answer.end(), n);
	return answer;
}

//-------------------------------------
//     Prime Factors - Method
//-------------------------------------
// Returns all prime factors of the provided number in a vector
// Includes 1 and number itself if prime
vector<int> primeFactorize(int n){
	vector<int> answer = {1};
	int max = n/2;
	for (int i = 2; i < max; i++){
		if (n%i == 0 && isPrime(i)) {
			answer.insert(answer.end(), i);
		}
	}
	return answer;
}


//-------------------------------------
//    Pascal's Triangle - Method
//-------------------------------------
// Returns a vector containing the values of 
// Pascal's triangle at the given row
vector<int> pascalTriangle(int rows){
	int len = rows+1;
	vector<int> arr1(len);
	vector<int> arr2(len);
	
	arr1[0] = 1;
	arr2[0] = 1;
	for (int i = 0; i < rows; i+=2){
		for (int j = 1; j < len; j++){
			arr2[j] = arr1[j-1] + arr1[j];
		}
		if (rows - 1 == i){
			return arr2;
		}
		for (int j = 1; j < len; j++){
			arr1[j] = arr2[j-1] + arr2[j];
		}
	}
	return arr1;
}

int main(int argc, char *argv[]) {
	//-------------------------------------
	//       Conditional Statement
	//-------------------------------------
	int num1;
	cout << "Enter a number: ";
	cin >> num1;
	switch (num1){
		case -1:
			cout << "Negative One";
			break;
		case 0:
			cout << "Zero";
			break;
		case 1:
			cout << "Positive One";
			break;
		default:
			cout << "Other Value";
			break;
	}
	cout << endl << endl;
	
	// Test vector printing
    //vector<int> arr = {8, 4, 5, 9};
	//printVector(arr);
	
	//-------------------------------------
	//              Fibonacci
	//-------------------------------------
	
	cout << "Fibonacci sequence up to 4,000,000:" << endl;
	
	// initial two values
	int a = 1;
	int b = 2;
	
	// Leapfrog up through the sequence with the two variables
	// until a value of 4,000,000 is exceeded
	while (a < 4000000 && b < 4000000){
		if (a > b) { cout << a << ", "; b += a; }
		else { cout << b << ", "; a += b; }
	}
	
	//-------------------------------------
	//             isPrime()
	//-------------------------------------
	cout << endl << endl;
	// Provided test conditions - return accurately
	cout << "isprime(2) = " << isPrime(2) << endl;
	cout << "isprime(10) = " << isPrime(10) << endl;
	cout << "isprime(17) = " << isPrime(17) << endl;
	
	//-------------------------------------
	//             factorize()
	//-------------------------------------
	// Provided test conditions - return accurately
	cout << "Factors of 2:";
	printVector(factorize(2));
	cout << "Factors of 72:";
	printVector(factorize(72));
	cout << "Factors of 196:";
	printVector(factorize(196));
	cout << endl;
	
	//-------------------------------------
	//          primeFactorize()
	//-------------------------------------
	// Provided test conditions - return accurately
	cout << "Prime factors of 2:";
	printVector(primeFactorize(2));
	cout << "Prime factors of 72:";
	printVector(primeFactorize(72));
	cout << "Prime factors of 196:";
	printVector(primeFactorize(196));
	
	//-------------------------------------
	//          pascalTriangle()
	//-------------------------------------
	// Generate and print the first ten rows of the triangle
	cout << endl << "Pascal's Triangle: First 10 Rows" << endl;
	vector<int> pascal;
	for (int i = 0; i < 10; i++){
		pascal = pascalTriangle(i);
		printVector(pascal);
	}
}



