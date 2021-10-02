#include <bits/stdc++.h>
using namespace std;
#define ll long long
void merge1(ll a[], ll na, ll b[], ll nb, ll c[]);
void merge_sort(ll a[], ll n)
{
    ll c[n + 1];
    if (n <= 1)
        return;

    merge_sort(a, n / 2);
    merge_sort(a + (n / 2), n - n / 2);
    merge1(a, n / 2, a + n / 2, n - n / 2, c);

    for (int i = 0; i < n; i++)
        a[i] = c[i];
}
void merge1(ll a[], ll na, ll b[], ll nb, ll c[])
{

    ll i = 0, j = 0, k = 0;
    while (i < na && j < nb)
    {
        if (a[i] < b[j])
            c[k++] = a[i++];
        else
            c[k++] = b[j++];
    }
    while (i < na)
        c[k++] = a[i++];
    while (j < nb)
        c[k++] = b[j++];
}
int main()
{
    ll n;
    cin >> n;
    ll a[n + 1];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    merge_sort(a, n);
    cout << '[';
    for (int i = 0; i < n - 1; i++)
    {
        cout << a[i] << ',';
    }
    cout << a[n - 1] << ']';

    return 0;
}