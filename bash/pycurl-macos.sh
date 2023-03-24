brew install openssl
brew install curl-openssl
echo 'export PATH="/usr/local/opt/curl/bin:$PATH"' >> ~/.bash_profile
PYCURL_SSL_LIBRARY=openssl LDFLAGS="-L/usr/local/opt/openssl/lib" CPPFLAGS="-I/usr/local/opt/openssl/include" pip install --no-cache-dir pycurl