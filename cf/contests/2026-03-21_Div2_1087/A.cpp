#include<stdlib.h>
#include<iostream>
#include<algorithm>
using namespace std;

int main() {
    int t;
    cin>>t;
    while (t-- > 0) {
        long long n,c,k;
        cin>>n;
        cin>>c;
        cin>>k;
        long long arr[n];
        for(int i=0; i<n; i++) cin>>arr[i];

        sort(arr, arr+n);
        for(int i=0; i<n; i++) {
            if (arr[i]>c) break;
            int o = min(1ll*k, c-arr[i]);
            k -= o;
            c += arr[i] + o;
        }

        cout<<c<<endl;
    }
    return 0;
}

/*Upsolved
The constraint that combat power of monsters can be raised
using k and that it can be only raised till a[i]<=C means that
we should sort the array first and then calculate the combat
power value increase for OtterZ using min(k, C-arr[i])
*/