#!/bin/bash

echo "install subfinder"
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
echo""
echo "assetfinder"
go install -v github.com/tomnomnom/assetfinder@latest
echo""
echo "install dmut"
go install -v github.com/bp0lr/dmut@latest
echo""
echo "instal katana"
go install github.com/projectdiscovery/katana/cmd/katana@latest
echo""
echo "install waybackurls"
go install github.com/tomnomnom/waybackurls@latest
echo""
echo "install httpx"
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

mv ~/go/bin/* /usr/bin/
