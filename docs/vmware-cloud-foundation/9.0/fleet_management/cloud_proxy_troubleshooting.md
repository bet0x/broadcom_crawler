---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/cloud-proxy-troubleshooting.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Cloud Proxy Troubleshooting
---

# Cloud Proxy Troubleshooting

Cloud proxy troubleshooting steps are provided to help you easily resolve issues that you may come across in VCF Operations.

Before you proceed with troubleshooting, see the [Cloud Proxy FAQ](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/cloud-proxy-faq.html#GUID-b2afa731-63fd-4782-9d07-81747f994f25-en_GUID-14DEC7A5-8B08-4CF5-981B-79058E6BF54D).

## Installation and/or First Boot Failure

```
To verify the issue, check if /var/log/firstbootcontains a file named "Succeeded".
```

If not, the following problems could result in VCF Operations installation and/or first boot failure:

1. Unique Registration Key used while deploying Cloud Proxy is invalid. To verify, check the cloud proxy console.

   Solution: Redeploy cloud proxy.

## Cloud Proxy VM is running, but the status is Offline in VCF Operations.

![The status of the cloud proxy is offline in the cloud proxy page.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d6add8fb-c3f9-4966-9d22-90ade179a3d5.original.png)

To verify the connection, use the following commands: (For the complete list of commands, please see [Using the Cloud Proxy Command-Line Interface](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies/upgrading-cloud-proxy/using-the-cloud-proxy-command-line-interface-on-cloud.html#GUID-f0c4e448-9737-4cae-956e-a494847ac28d-en).

```
# Overall status of cloud proxy:cprc-cli -s

# Ping itself:
ip addr
ping <address>

# Ping gateway:
ip route
ping <gateway>

# Verify the connection outside the cloud proxy.
ping 8.8.8.8

Note: If you are using a network proxy,
use the /opt/vmware/share/vami/vami_config_net option#5 command
to ensure you have the correct configuration for the testings.
```

The following problems could result in VCF Operations displaying the status of cloud proxy as offline.

1. Incorrect network proxy information in cloud proxy configuration.

   To verify the connection via a network proxy, use the following:

   ```
   curl -vvv --proxy http(s)://proxy_user:proxy_pass@proxy_ip:proxy_port -H 'Accept: application/json' -H 'Content-Type: application/json' -X GET https://<gateway url>/casa/security/ping (gateway url example - 10238.gw.dev.vrops-ops.com)

   To ignore SSL validation for a proxy server,
   use curl --proxy-insecure. With SSL validation the customer can provide Proxy Server certificate during cloud proxy deployment or re-configuration
   so that provided certificate from customer can be used to check the connection with curl with SSL certificate validation.
   ```

   Solution:
   1. SSH to the cloud proxy VM and set the connectretry to 0 in /storage/db/vmware-vrops-cprc/configuration/cprc.configuration to ensure that the cloud proxy retries to connect.
   2. Shutdown the cloud proxy VM.
   3. Update the network proxy configurations from the vCenter VM options using the vApp options.
   4. Boot the cloud proxy VM.
2. Required ports are not open.

   To verify:

   ```
   openssl s_client -showcerts -connect {address}:443

   curl -v telnet://{address}:443

   # Or, change the address to the machine you want to check:
   python -c "import socket; print(socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(('127.0.0.1', 443)))"

   # If you get a !=0 response, the server is not listening to the port.
   ```

   Solution:
   1. SSH to the cloud proxy VM and set connectretry to 0 in /storage/db/vmware-vrops-cprc/configuration/cprc.configuration to ensure that the cloud proxy retries to connect.
   2. Provide port access as mentioned in the prerequisite section of [Configuring Cloud Proxies in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud.html#GUID-bd1eed2a-5668-4640-8ae3-79ce18f3d081-en)
   3. Boot the cloud proxy VM.
3. Invalid certificate.

   To verify:

   ```
   openssl s_client -showcerts -connect {address}:443
   ```

   Solution:
   1. SSH to the cloud proxy VM and set connectretry to 0 in /storage/db/vmware-vrops-cprc/configuration/cprc.configuration to ensure that the cloud proxy retries to connect.
   2. Follow the steps mentioned in VMware KB Article, [83698](https://kb.vmware.com/s/article/83698).
4. The logs folder /storage/log is running out of partition space.

   Solution: Remove log files to ensure that enough space is available. Note that this is an exceptional case. In normal conditions, log files are auto archived.
5. One or more of the following services are down: httpd-north.service, haproxy.service and collector.service.

   Solution:
   - Check service status by running the following command: systemctl status <service name>.
   - To start service, use the following command: systemctl start <service name>.
6. Unique Registration Key expired.

   Solution: Redeploy cloud proxy with new Unique Registration Key.

## Cloud proxy is online, and state of Cloud Account is Collecting, but the status is Object Down.

![The cloud proxy is collecting data but the object is down and it is unable to connect to the vCenter. ](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/75e8c5c5-5030-49bb-b973-2857fa18eb65.original.png)

The following problem could result in VCF Operations displaying the state of Cloud Account as Collecting, while the status is Object Down.

1. Incorrect account credentials.

   Solution: Check and update the credentials used while setting up the cloud account.

## Cloud proxy status is stuck in Going Online.

![The status of the cloud proxy is going online in the cloud proxy page.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7344e8dc-8066-4bc6-96c0-fea4ff0b34f7.original.png)

It can take up to 20 mins on first reboot, for the cloud proxy to be registered and come online. Wait for the specified time to see if cloud proxy comes online. If it still does not come online, one or more of the following services are down: httpd-north.service, haproxy.service, and collector.service.

Solution:

1. Check service status by running the following command: systemctl status <service name>
2. To start service, use the following command: systemctl start <service name>.

## Cloud proxy does not upgrade automatically, after the upgrade of VCF Operations

There could be a few possible reasons why cloud proxy does not upgrade automatically after an upgrade of VCF Operations.

1. High network latency leading to PAK download failure. Latency of >500ms is not supported.

   Solution: See the VMWare KB article [80590](https://kb.vmware.com/s/article/80590) on how to manually upgrade cloud proxy via CLI.
2. Upgrade status is stuck at Running since the previous upgrade had failed.

   Solution: Follow the steps given below to change the upgrade status.
   1. Stop the casa service: systemctl stop vmware-casa.service.
   2. Change the upgrade status from RUNNING to NONE in the following files:

      ```
      ./storage/db/vmware-vrops-cprc/status/cprc.upgrade.status
      ./storage/db/vmware-vrops-cprc/status/cprc.pak.status
      ```
   3. See the VMware KB article [80590](https://kb.vmware.com/s/article/80590) and run the manual upgrade.

## Cloud proxy gets disconnected at regular intervals

There could be a few possible reasons why cloud proxy gets disconnected at regular intervals.

1. Check the network connectivity and latency.
2. Check if the cloud proxy VM can reach the DNS and use NSlookup to validate the DNS connectivity.