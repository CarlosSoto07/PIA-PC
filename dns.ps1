Write-Host "Se Esta obteniendo el DNS de los puertos..."
$dns1 = Get-DnsClientCache

Write-Host "Se esta obteniendo el cache del DNS..."
$dns2 = ipconfig /displaydns


Write-Host "Creando Txt con DNS ..."
"COMMAND: Get-DnsClientCche `r`n  `r`n", $dns1 | Out-File -FilePath "DNSClientCache.txt"

Write-Host "Creando txt con IpConfig/Dns..."
"COMMAND: ifconfig /displaydns `r`n `r`n", $dns2 | Out-File -FilePath "DNS-DisplayDNS.txt"
