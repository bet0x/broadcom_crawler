---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries/set-up-an-offline-depot-web-server-for-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Set Up an Offline Depot Web Server for VMware Cloud Foundation
---

# Set Up an Offline Depot Web Server for VMware Cloud Foundation

Before you can connect a VCF Instance or VCF fleet to an offline depot, you must configure an internal web server to host binaries and ESX component data.

The offline depot web server must meet the following requirements:

- Photon OS: Download the latest Photos OS OVA image. For more information, see <https://github.com/vmware/photon/wiki/Downloading-Photon-OS>.
- Operating System: A Linux or Windows virtual machine. For Linux, any distribution is supported (for example, CentOS, RHEL, Ubuntu).
- Storage: A dedicated disk for storing offline depot content. Minimum recommended size: 1 TB.
- Web Server and SSL: A web server to serve the offline depot content over HTTP/HTTPS. For HTTPS, the server must support TLSv1.2 and TLSv1.3. The choice of web server is flexible. For example: Apache HTTP Server, NGINX, and so on.
- Networking and Access: The virtual machine must have a static IP address. DNS records for the offline depot server are recommended but not required.
- User Access: A dedicated non-root user on the virtual machine. The user must have read/write access to the offline depot directory and appropriate permissions to run VCF Download Tool commands.

The following procedure describes how to set up an Apache HTTP Server on a Photon OS 5 virtual machine. Depending on your environment, you might need to modify some of the commands. For example, if corporate policies require you to use a different operating system or web server.

The procedure uses /var/www/html as the document root directory for the web server. The directory must exist or you must manually create it by running the mkdir -p /var/www/html command. Alternatively, to use a different document root directory, in the procedure, replace /var/www/html with your preferred root directory.

The following procedure uses depot as an example name of the depot VM and depot.rainpole.io as offline depot URL.

1. Deploy the Photon OS OVA file on a VM.

   Do not power on the VM.
2. Add a harddrive with a capacity of 1 TB or more.
3. Power on and log in to the Photon OS 5 VM.
4. Specify networking details.
   1. Navigate to /etc/systemd/network/ and create a .network file.

      For example, 10-static-en.network.
   2. In an text editor, open the .network file and add the your network configuration.

      For example:

      ```
      [Match]
      Name=eth0

      [Network]
      Address=172.16.10.14/24
      Gateway=172.16.10.1
      DNS=172.16.10.4 172.16.10.5
      ```
   3. Set the correct permissions for the .network file.

      ```
      chmod 644 10-static-en.network
      ```
5. Update the hostname by using the hostnamectl set-hostname offlinedepotURL command, where is offlinedepotURL is your offline depot URL.

   For example:

   ```
   hostnamectl set-hostname depot.rainpole.io
   ```
6. Restart the network and DNS lookup services.

   ```
   systemctl restart systemd-networkd
   systemctl restart systemd-resolved
   ```
7. Install Apache HTTP Server, update the operating system and reboot the VM.

   ```
   tdnf install httpd tar jq --assumeyes
   ```

   ```
   tdnf update --assumeyes
   ```

   ```
   reboot
   ```
8. Format the disk you added to the VM.

   ```
   mkdir -p /var/www/html
   mkfs.ext4 /dev/sdb
   echo "/dev/sdb /var/www/html ext4 defaults 1 1" >> /etc/fstab
   mount -a
   ```
9. Prepare the SSL Certificate.

   By following the commands, you create a directory and the private key.

   ```
   mkdir /root/http-certificates
   ```

   ```
   openssl genpkey -out /root/http-certificates/server.key -algorithm RSA -pkeyopt rsa_keygen_bits:2048
   ```

   1. Provide SAN information, create a configuration file with the required attributes, for example conf.cfg, and add the file to the openssl req command.

      Replace the following example values in the template with your own values: conf.cfg, SE, Stockholm, Stockholm, Rainpole, IT, depot.rainpole.io, and 172.16.10.11.

      OpenSSL does not prompt you for Subject Alternative Names (SANs) during the certificate request (CSR) creation process. SANs are treated as extensions, rather than standard subject information fields.

      ```
      cat << 'EOF' > /root/http-certificates/conf.cfg
      [req]
      distinguished_name = req_distinguished_name
      req_extensions = req_ext
      prompt = no

      [req_distinguished_name]
      C = SE 
      ST = Stockholm
      L = Stockholm
      O = Rainpole
      OU = IT
      CN = depot.rainpole.io

      [req_ext]
      subjectAltName = @alt_names

      [alt_names]
      IP.1 = 172.16.10.11
      DNS.1 = depot.rainpole.io
      EOF
      ```
   2. Create a .csr file by using the .key and .cfg files.

      ```
      openssl req -new -key /root/http-certificates/server.key -out /root/http-certificates/request.csr -config conf.cfg
      ```
10. Sign the certificate.

    | Signing Method | Steps |
    | --- | --- |
    | External Certificate Authority | 1. Sign request.csr using your organization's external certificate authority. 2. Combine the machine, intermediate, and root certificates into one server.crt file (PEM format), in this order:     ```    -----BEGIN CERTIFICATE-----    [Machine Cert]    [Intermediate Cert]    [Root Cert]    -----END CERTIFICATE-----    ``` 3. Copy server.crt to /root/http-certificates/. |
    | VMware Certificate Authority (VMCA) | 1. Transfer request.csr to the vCenter (for example, to /root/). 2. SSH into vCenter as root and run the following commands:     ```    openssl x509 -req -days 365 -in /root/request.csr \     -CA /var/lib/vmware/vmca/root.cer \     -CAkey /var/lib/vmware/vmca/privatekey.pem \     -CAcreateserial -out /root/server.crt -sha256    ```     ```    cat /var/lib/vmware/vmca/root.cer >> /root/server.crt    ``` 3. Copy server.crt to /root/http-certificates/. 4. Clean the .crt certificate files.     ```    rm -f /root/server.crt /root/request.csr    ``` |
11. Move the signed .key and .crt certificate files to the Apache configuration directory.

    ```
    mv server.key server.crt /etc/httpd/conf/
    ```

    ```
    chmod 0400 /etc/httpd/conf/server.key /etc/httpd/conf/server.crt
    ```

    ```
    chown root:root /etc/httpd/conf/server.key /etc/httpd/conf/server.crt
    ```
12. To configure the Apache server, edit the /etc/httpd/conf/httpd.conf and /etc/httpd/conf/extra/httpd-ssl.conf files.
    1. Run the following commands to enable SSL modules and replace the [[email protected]](/cdn-cgi/l/email-protection) and depot.rainpole.io:443 example values with your own.

       ```
       sed -i 's|#LoadModule ssl_module|LoadModule ssl_module|' /etc/httpd/conf/httpd.conf
       ```

       ```
       sed -i 's|#LoadModule socache_shmcb_module|LoadModule socache_shmcb_module|' /etc/httpd/conf/httpd.conf
       ```

       ```
       sed -i 's|#Include conf/extra/httpd-ssl.conf|Include conf/extra/httpd-ssl.conf|' /etc/httpd/conf/httpd.conf
       ```

       ```
       sed -i 's|DocumentRoot "/etc/httpd/html"|DocumentRoot "/var/www/html"|' /etc/httpd/conf/extra/httpd-ssl.conf
       ```

       ```
       sed -i 's|ServerAdmin you@example.com|ServerAdmin [email protected]|' /etc/httpd/conf/extra/httpd-ssl.conf
       ```

       ```
       sed -i 's|ServerName www.example.com:443|ServerName depot.rainpole.io:443|' /etc/httpd/conf/extra/httpd-ssl.conf
       ```
    2. In the /etc/httpd/conf/httpd.conf file, locate the DocumentRoot "/var/www/html" section and change Required all denied to Required all granted.
    3. In the /etc/httpd/conf/extra/httpd-ssl.conf file, locate the </VirtualHost> tag and above the tag, paste the following configuration code.

       ```
       <Directory /var/www/html/PROD/COMP>
               AuthType Basic
               AuthName "Basic Authentication"
               AuthUserFile /etc/httpd/conf/.htpasswd
               require valid-user
       </Directory>
       <Directory /var/www/html/PROD/metadata>
               AuthType Basic
           AuthName "Basic Authentication"
           AuthUserFile /etc/httpd/conf/.htpasswd
           require valid-user
       </Directory>
       <Directory "/var/www/html/PROD/COMP/Compatibility/VxrailCompatibilityData.json">
               # VxRail VVS Cookie Validation (VCF 5.0)
               <If "%{HTTP:Cookie} == 'ngssosession=ngsso-token' ">
               Require all granted
               </If>
       </Directory>
       <Directory /var/www/html/PROD/vsan/hcl>
               Require all granted
       </Directory>
               # Those Alias statements are needed only for VCF 5.1.0.0.
               Alias /products/v1/bundles/lastupdatedtime /var/www/html/PROD/vsan/hcl/lastupdatedtime.json
               Alias /products/v1/bundles/all /var/www/html/PROD/vsan/hcl/all.json
               # Needed only if UMDS downloads are presented
       <Directory /var/www/html/umds-patch-store>
               Require all granted
       </Directory>
       ```
13. Configure the authentication.

    Replace Username with the user name that VCF Operations and SDDC Manager use to authenticate against the depot.

    ```
    htpasswd -c /etc/httpd/conf/.htpasswd Username
    ```

    ```
    chown apache /etc/httpd/conf/.htpasswd
    ```

    ```
    chmod 0400 /etc/httpd/conf/.htpasswd
    ```
14. Test the configuration, enable and start the Apache HTTP server.

    ```
    httpd -t
    ```

    ```
    systemctl start httpd
    ```

    ```
    systemctl status httpd
    ```

    ```
    systemctl enable httpd
    ```
15. To open the HTTPS port in the firewall, edit /etc/systemd/scripts/ip4save file.

    In the file, above COMMIT, add the following text.

    ```
                -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
    -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
    ```

    For example:

    ```
    # init
    *filter
    :INPUT DROP [0:0]
    :FORWARD DROP [0:0]
    :OUTPUT DROP [0:0]
    # Allow local-only connections
    -A INPUT -i lo -j ACCEPT
    -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
    #keep commented till upgrade issues are sorted
    #-A INPUT -j LOG --log-prefix "FIREWALL:INPUT "
    -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
    -A OUTPUT -j ACCEPT
    -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
    -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
    COMMIT
    ```
16. Restart the service.

    ```
    systemctl restart iptables
    ```
17. Open a web browser and verify access to https://<offline-depot-fqdn>/.
18. Clean up the temporary certificate generation files. 

    ```
    rm -rf /root/http-certificates
    ```
19. Remove the default Apache index file.

    ```
    rm -f /var/www/html/index.html
    ```
20. Set ownership and permissions for document root directory.

    ```
    chown apache -R /var/www/html/
    ```

    ```
    find /var/www/html -type d -exec chmod 0500 {} \;
    ```

    ```
    find /var/www/html -type f -exec chmod 0400 {} \;
    ```