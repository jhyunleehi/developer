
### apt update failed 
```
The error you are seeing, "certificate verification failed: the certificate chain uses an insecure algorithm", usually occurs when APT attempts to download packages or update from a repository that has SSL certificates that use deprecated or insecure algorithms.
```


Steps to Fix the Issue
#### Option 1
Use HTTP Instead of HTTPS (Not Recommended for Security)

```
sudo nano /etc/apt/sources.list
sudo nano /etc/apt/sources.list.d/custom-repo.list

deb https://example.com/ubuntu focal main
==>
deb http://example.com/ubuntu focal main

```

#### Option 2
: Temporarily Disable SSL Verification (Not Recommended for Security)
This option should only be used temporarily or in environments where security isn't critical. You can disable SSL certificate verification in APT:

Edit APT Configuration:

```
sudo nano /etc/apt/apt.conf.d/99ignore-invalid-cert

==> 다음 라인을 추가 한다.  
Acquire::https::Verify-Peer "false";
```
