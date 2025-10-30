---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/understanding-support-bundle-file-paths.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding Support Bundle File Paths
---

# Understanding Support Bundle File Paths

Know the different files collected when you download a support bundle and the features that store logs in these file paths.

## NSX Node Support Bundle

| File Path | Features Using the File Path |
| --- | --- |
| /var/log/syslog | All |
| /var/log/nsx-audit.log | All |
| /var/log/policy/policy.log | All |
| /var/log/policy/policy\_restart.log | All |
| /var/log/policy/policy-tomcat-wrapper.log | All |
| /var/log/proton/activity-stats.log | All |
| /var/log/proton/gc.log | All |
| /var/log/proton/localhost\_access\_log.txt | All |
| /var/log/proton/nsxapi.log | All |
| /var/log/proton/proton\_restart.log | All |
| /var/log/proton/proton-tomcat-wrapper.log | All |
| /var/log/proton-tomcat/nsxapi.log | All |
| /var/log/proxy/gc.log | AAA (Auth) |
| /var/log/proxy/keystore.log | AAA (Auth) |
| /var/log/proxy/localhost.log | AAA (Auth) |
| /var/log/proxy/localhost\_access\_log.txt | AAA (Auth) |
| /var/log/proxy/proxy-tomcat-wrapper.log | AAA (Auth) |
| /var/log/proxy/reverse-proxy.log | AAA (Auth) |
| /var/log/phonehome-coordinator/localhost\_access\_log.txt | Alarm Event Framework, Telemetry, Notification Framework, Capacity Dashboard |
| /var/log/phonehome-coordinator/phonehome-audit-log.txt.0 | Alarm Event Framework, Telemetry, Notification Framework, Capacity Dashboard |
| /var/log/phonehome-coordinator/phonehome-coordinator.log | Alarm Event Framework, Telemetry, Notification Framework, Capacity Dashboard |
| /var/log/cbm/cbm.log | Clustering |
| /var/log/cm-inventory/localhost\_access\_log.txt | CM-inventory (Compute Manager) |
| /var/log/vmware/top-cpu.log | Common - Appliance Health |
| /var/log/vmware/top-mem.log | Common - Appliance Health |
| /var/log/stats | Common - IP, memory, thread stats |
| /var/log/cloudnet/nsx-ccp-transaction.log | Controller |
| /var/log/cloudnet/nsx-ccp.log | Controller |
| /var/log/core | Cores generated |
| /var/log/corfu/corfu.9000.log | Corfu DB |
| /var/log/corfu/corfu-compactor-audit.log | Corfu DB |
| /var/log/corfu-nonconfig/corfu.9040.log | Corfu DB |
| /var/log/corfu-nonconfig/nonconfig-corfu-compactor-audit.log | Corfu DB |
| /var/log/cloudnet/nsx-ccp.log | DNS, Upgrade, IPDiscovery, Groups |
| /var/log/cm-inventory/cm-inventory.log | Endpoint Security, Deployment, NSX Edge Install, Vmotion, Inventory, NCP/Openshift/PKS-windows, Install/Host Upgrade, Install |
| /var/log/async-replicator-service/ar.log | Federation (Local Manager) |
| /var/log/proton/nsx-common-dashboard.log | NCP/Openshift/PKS-windows |
| /var/log/search/elasticsearch\_index\_indexing\_slowlog.log | NCP/Openshift/PKS-windows |
| /var/log/search/search-policy.log | NCP/Openshift/PKS-windows |
| /var/log/migration-coordinator/migration-coordinator.log | Overlay adoption |
| /var/log/policy/localhost\_access\_log.txt | Policy realization |
| /var/run/log/nsxaVim.log | Stateless Hosts/ Transport Node Profile |
| /var/log/search/elasticsearch.log | UI |
| /var/log/intelligence-upgrade-coordinator/localhost\_access\_log.txt | Upgrade |
| /var/log/upgrade | Upgrade |
| /var/log/resume-upgrade.log | Upgrade |
| /var/log/upgrade-coordinator/localhost\_access\_log.txt | Upgrade |
| /var/log/upgrade-coordinator/upgrade-coordinator.log | Upgrade |
| /var/log/nvpapi/api\_server.log | Upgrade, BnR |
| /var/log/upgrade-coordinator/localhost\_access\_log.txt | Upgrade Coordinator |

## NSX Edge Support Bundle

| File Path | Features Using the File Path |
| --- | --- |
| /var/log/syslog | All |
| /controller/data/data\_dump | DHCP |
| /controller/falcon/falcon\_dump | DHCP |
| /controller/span/config\_span\_graph\_dump | DHCP |
| /controller/span/dag\_span\_graph\_dumpContainer\_Dfw\_Canary | DHCP |
| /controller/mediator/mediator\_dump | DHCP |
| /var/log/cloudnet/nsx-ccp.log | DHCP |
| /var/log/proton/nsxapi.log | DHCP |
| /edge/dns\_fdr-all | DNS |
| /edge/dns-forwarder | DNS |
| /edge/service\_binding | DNS |
| /var/log/join\_mp.log | Edge Install, Install, Upgrade |
| /edge/fw-if-ruleset/ | Load Balancer |
| /edge/Lb\_UUID/ | Load Balancer |
| /edge/lb-\* | Load Balancer |
| /var/log/lb/<LB\_UUID>/logs/error.log | Load Balancer |
| /var/log/lb/<LB\_UUID>/logs/ acess\_vipid.log | Load Balancer |
| /var/log/lb/<LB\_UUID>/logs/nginx.conf | Load Balancer |
| /var/log/lb/<LB\_UUID>/lbconf\_gen.log | Load Balancer |
| /var/log/core/ | Load Balancer, L3VPN, L2VPN, Edge HA, Upgrade |
| /var/log/nsx-cli/nsxcli.log | L3VPN,L2VPN,Edge HA, Upgrade |
| /var/log/rcpm/frr-config.log | L3VPN, Upgrade |
| /var/log/rcpm/frr-reload.log | L3VPN, Upgrade |
| /var/log/vmware/top-cpu.log | NCP/Openshift/PKS-windows |
| /var/log/vmware/top-mem.log | NCP/Openshift/PKS-windows |
| /var/log/frr/frr.log | Openstack, Upgrade |
| /opt/vmware/nsx-nestdb/bin/nestdb-cli | Openstack, Upgrade |
| /var/log/nginx/access.log | Openstack |
| /var/log/upgrade | Upgrade |
| /var/log/nvpapi/api\_server.log | Upgrade, BnR |

## NSX Application Platform Support Bundle

The following support bundles include log information for the features that NSX Application Platform hosts. These features are Security Intelligence, vDefend Network Detection and Response, Malware Prevention for vDefend, and NSX Metrics.

| File Path | Features Using the File Path |
| --- | --- |
| /var/log/napp/supportbundle/platform\_service\_dbg.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/kafka\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/zookeeper\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/ spark-app-rawflow-driver\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/authserver\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/cluster-api\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/common-agent\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/projectcontour\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/routing-controller\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/trust-manager\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/upgrade-coordinator\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/postgresql\*.log | NSX Application Platform |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/visualization\*.log | Security Intelligence Visualization |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/recommendation\*.log | Security Intelligence Recommendation |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/rawflowcorrelator\*.log | Security Intelligence |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/ overflowcorrelator\*.log | Security Intelligence |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/\*druid\*.log | Security Intelligence |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/nsx-config\*.log | Security Intelligence |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/redis\*.log | Security Intelligence |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/minio\*.log | Security Intelligence |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/nsx-ndr\*.log | vDefend Network Detection and Response |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/sa-\*.log | Malware Prevention for vDefend |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/malware\*.log | Malware Prevention for vDefend |
| /var/log/napp/supportbundle/<K8s\_worker\_node\_name>/metrics\*.log | NSX Metrics |

## NSX Global Manager Support Bundle

| File Path | Features Using the File Path |
| --- | --- |
| /var/logdata-log.log | Federation |
| /var/log/async-replicator- ar.log | Federation |
| /var/log/connections.log | Federation |
| /var/log/gm.log | Federation |
| /var/log/nvpapi/api\_access.log | Federation |
| /var/log/global-manager/gmanager.log | Grouping |