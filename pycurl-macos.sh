First you need to install OpenSSL via Homebrew:

$ brew install openssl
Curl is normally already installed in MacOs, but to be sure it uses OpenSSL, we need to install it using brew:

$ brew install curl-openssl
Curl is installed keg-only by brew. This means that is installed but not linked. Therefore, we need to instruct pip to use the recently installed curl before installing pycurl. We can do this permanently by changing our bash_profile:

$ echo 'export PATH="/usr/local/opt/curl-openssl/bin:$PATH"' >> ~/.bash_profile
Or temporary in the current shell:

$ export PATH="/usr/local/opt/curl-openssl/bin:$PATH"
Then, we need to install pycurl as follows:

$ PYCURL_SSL_LIBRARY=openssl LDFLAGS="-L/usr/local/opt/openssl/lib" CPPFLAGS="-I/usr/local/opt/openssl/include" pip install --no-cache-dir pycurl
