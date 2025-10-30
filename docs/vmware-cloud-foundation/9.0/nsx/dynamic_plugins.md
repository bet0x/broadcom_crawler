---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/dynamic-plugins.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Dynamic Plugins
---

# Dynamic Plugins

A dynamic plugin is a customized plugin that you can create for any supported transport node, such as ESX host, to check the node’s health.

A dynamic plugin can be installed at runtime. It performs the following functions:

- Write a system log for the affected transport node.
- Execute a command or CLI through the run\_command() function.
- Read existing metrics.
- Export data to wavefront (only in a VMware Cloud environment).

You can create a dynamic plugin if you have expertise in managing NSX. The VMware Support can also create a dynamic plugin.

## Security management

After you have created the plugin, you must submit it to the VMware engineering team that performs a code review of the plugin. After review completion, the engineering team submits the plugin, its review test result, and code changes in a GIT repository for validation. If the dynamic plugin passes the validation, it is committed and a product build is triggered on the GIT repository to create a new build to publish all the dynamic plugins. The following GIT repository details are used:

- GitLab: https://gitlab-vmw.devops.broadcom.net/core-build/nsbu-sha-plugin
- Product: nsx-sha-plugins
- Gitreview supporting: Performed by VMware team

You can get the required plugin from the published files of the build. When you upload a signed plugin to the management plane, the management plane uses a public key to verify the signature and confirm that this plugin is valid. After the management plane validates the plugin, it pushes the files of the plugin to the destination hosts through the secured channels between the management plane and the Central Control Plane (CCP) and between CCP and hosts.

When you restart the System Health Agent (SHA) instance, it gets the plugin files from the management plane again. Since all the files are published through secured channels and no temporary files are used, the risk that hackers can modify scripts is prevented.

Also, to prevent risks of harmful code, SHA uses RestrictedPython to check the plugin python script before executing the script.

## Version management

A plugin might be based on a command or a tool that is not supported in later versions of NSX, so each dynamic plugin must define the supported NSX version in the manifest.yml file. The version should be a REGEX string for all the supported versions. SHA on the host-side checks the version of dynamic plugins and runs only the REGEX matched ones.

Recommended version management policies are:

- Define the supported NSX version of a major release.

  Considering that most of the commands and tools do not change between minor releases in the same major release, the following method is the suggested way to define the version for all minor releases.

  For example,

  version: ^2\.5\.[0-9.]+ <== The custom plugin supporting all NSX 2.5 releases
- When a new major release is published, the VMware engineering team must review all the submitted dynamic plugins.
- The plugin writer must update the script when the related commands or tools change.

## Install a dynamic plugin

The transport node or the edge node on which the plugin is installed must have a minimum of 30-MB memory space. Also, note that you can install only up to 10 plugins. Once the plugin count reaches 10, any further installation of a plugin will fail.

To install the plugin, perform the following tasks:

1. Create the dynamic plugin files in the GIT repository. For more information about the plugin files, see the section Dynamic plugin files.
2. Trigger the product build in the GIT repository to generate the zipped package of the dynamic plugin files and download the package.
3. Create the dynamic plugin by using the following API with the POST method.

   https://<manager\_ip>/api/v1/systemhealth/plugins
4. Upload the plugin zipped package to the management plane using the following API with the POST method. The management plane extracts the uploaded file and perform the required validation.

   /systemhealth/plugins/<plugin-id>/files/<file-name>/data

   The maximum size of the plugin zipped file is 500k.
5. Create a node group with the required transport nodes as members by using the following API with the POST method.

   /<manager\_ip>/api/v1/ns-groups
6. Apply the plugin profile to the node group by creating a new service config by using the following API. The service config framework sends the plugin content to the node group.

   https://<manager\_ip>/api/v1/service-configs

For more information about APIs, see the NSX API Guide documentation.

## Get the plugin status

Once the dynamic plugin is running, it automatically uploads the status to the management plane through the existing message channel. The management plane aggregates the plugin status information and store it into the database. To get the status of all plugins on each node, use the following API with the GET method.

https://<manager\_ip>/api/v1/systemhealth/plugins/status/<transport\_node\_id>

Request Example:

GET https://<manager\_ip>/api/v1/systemhealth/plugins/status/a257b981-1a1c-4b95-b16c-8646

Response Example:

```
{
 "result_count":1,
 "results": [
 {
 "id": "72e1bd4b-6df6-42d0-9c59-a1c31312c9f1",
 "name": "health-check-compute",
 "status": "NORMAL",
 "detail": ""
 }
 ]
 }
```

## Uninstall a dynamic plugin

To uninstall a plugin, remove the service config by using the following API.

https://<manager\_ip>/api/v1/service-configs/<service\_config\_id>

## Other APIs for managing the plugins

The following table lists APIs to manage dynamic plugins. For more information about APIs, see the NSX API Guide documentation.

| Task | Method | API |
| --- | --- | --- |
| Delete a plugin | DELETE | /systemhealth/plugins/<plugin-id> |
| Create a system health profile | POST | /systemhealth/profiles |
| Watch the plugin status | GET | /systemhealth/plugins/status/<node-id> |
| Enable the plugin |  | Enabling a plugin is a two-step process as follows: 1. Use the following API to set the enabled property to true or false. https://<manager\_ip>/api/v1/systemhealth/profiles/ 2. Use the following API to apply the SHA profile to the NS group. https://<manager\_ip>/api/v1/service-configs |
| Change the plugin interval | POST | Changing the plugin interval is a two-step process as follows:   1. Use the following API to set the config property. https://<manager\_ip>/api/v1/systemhealth/profiles/ 2. Use the following API to apply the SHA profile to the NS group. https://<manager\_ip>/api/v1/service-configs |

## Dynamic plugin files

A dynamic plugin comprises the following files:

- Install specification file

  The install specification file, manifest.yml, contains the following information for System Health Agent:
  - Plugin structure
  - Constraints if any
  - How to install and use the plugin
  - Security restrictions for the health check script. For example, permissions the script has and files that the script can access.

  The following table lists fields that are specified in a manifest.yml file.

  | Name | Description | Required/Optional | Example |
  | --- | --- | --- | --- |
  | classes | Specifies classes needed in the plugin script. The classes must be specified in the following format. '<module\_name>.<class\_name>' | Optional | classes: ['datetime.datetime','datetime.date'] |
  | modules | Specifies modules needed in the plugin script. | Optional | modules: ['random', 'math'] |
  | plugin | Specifies the plugin structure as follows:  config: config file name  script: script file name | Required | plugin:  config: plugin.cfg.yml  script: plugin.py |
  | version | Specifies the NSX versions on which this plugin can be installed. | Required | version: '^3\.1\.[0-9.]+' |
  | node\_type | Specifies NSX node types where this plugin can be installed. The available node types are:  - nsx-esx  - nsx-bms  - nsx-edge | Required | node\_type: ['nsx-esx'] |
  | metrics | Specifies metrics which can be consumed in the plugin script. | Optional | metrics: ['nsx.host.host-metrics'] |
  | precondition | Specifies precondition for the plugin. The available precondition is wavefront.  This field is applicable only in a VMware Cloud environment. | Optional | precondition: ['wavefront'] |

  Do not use the following built-in modules:
  - os
  - subprocess
  - sys
  - multiprocessing
  - importlib

  The following table lists the interfaces that you must use in place of built-in functions of the respective modules. These interfaces are system provided. You can use them directly without specifying their module/class in the manifest.yml file.

  | Module | Built-in function | Substitute interface |
  | --- | --- | --- |
  | datetime | datetime.date.strftime(self, fmt) | datetime\_date\_strftime(dt, fmt)  :param dt: date instance  :param fmt: format string |
  | datetime | datetime.date.today() | datetime\_date\_today() |
  | sys | sys.getrecursionlimit() | sys\_getrecursionlimit() |
  | sys | sys.getrefcount(object) | sys\_getrefcount(object) |
  | sys | sys.getsizeof(object, default) | sys\_getsizeof(object, default) |
  | sys | sys.maxsize | sys\_maxsize |
  | sys | sys.path | sys\_path |

  Sample of a manifest.yml file.

  ```
  # specify classes needed in plugin script 
  classes: ['datetime.datetime','datetime.date']
  # specify modules needed in plugin script 
  modules: ['random', 'math']
  # plugin structure
  plugin:
   config: plugin.cfg.yml
   script: plugin.py
  # specify nsx versions on which this plugin can be installed
  version: '^3\.1\.[0-9.]+'
  # specify nsx node type where this plugin can be installed
  node_type: ['nsx-esx']
  # specify metrics which can be consumed in plugin script
  metrics: ['nsx.host.host-metrics']
  # specify precondition for plugin 
  precondition: ['wavefront']
  ```
- Default profile file

  The default profile file, plugin.cfg.yml, is used to configure plugin behavior, such as the execution frequency of the health check script. To change the default configurations, you can create a SHA profile for a specific dynamic plugin and apply it to transport node through NS group by using the management plane to CCP to NestDB channel.

  The following table lists fields that are specified in a plugin.cfg.yml file.

  | Name | Description | Required/Optional | Example |
  | --- | --- | --- | --- |
  | CHECK\_INTERVAL | Specifies the default interval in seconds for plugin script execution. | Required | CHECK\_INTERVAL: 20 |
  | ENABLE | Specifies whether the plugin is enabled by default. | Required | ENABLE: true |

  Sample of a plugin.cfg.yml file.

  ```
  # Required field - default interval (unit: second) between plugin script executions.
  CHECK_INTERVAL: 20

  # Required field - whether plugin is enabled by default
  ENABLE: true

  # Plugin user can add other fields as below if needed to control plugin script logic.
  EXPORT_DATA: true
  ```
- Health check script

  A health check script file, plugin.py, contains a python script to check the health status of a transport node.

  The following table lists system-defined variables and functions that can be used and data that can be read in a plugin.py file.

  | Variable/Data/Function | Description | Type | Example |
  | --- | --- | --- | --- |
  | logger | Writes log information in syslog. The existing system-defined variable, logger, can be used directly in the plugin script. The output log is prefixed with the plugin name and id as shown in the following sample output.  2020-10-28T10:47:43Z nsx-sha: NSX 2101378 - [nsx@6876 comp="nsx-esx" subcomp="nsx-sha" username="root" level="INFO"] [name:hl-esx-002-04][id:a3eb14f1-d185-4bc7-bfaa-6cf888bbeb22] dynamic plugin - not export data | Variable | logger.info("this is a demo log") |
  | data\_store | The existing system-defined dictionary that is used to fetch system-provided data. For example, profile, metric, and host\_id. | Variable | profile = data\_store['profile'] |
  | profile | Profile data is a dictionary parsed from the default profile (plugin.cfg.yml) or the effective SHA profile (user-applied through the NSX Manager API) that is read from data\_store. It has the following format:  {'ENABLE': True, 'CHECK\_INTERVAL': 20, 'EXPORT\_DATA': True} | Data | profile = data\_store['profile'] |
  | metric | Metric is a dictionary with 'value' and 'timestamp' that is read from data\_store. It has the following format:  data\_store['metrics'][<metric\_name>]  Where,  The first key must be 'metrics'.  The second key is an existing metric name. | Data | metric = data\_store['metrics']['nsx.host.host-metrics']  metric is: {  ‘value’:XXX, <== the collected data of the metric  ‘timestamp’: XXX <== timestamp of the data collected  }  Note: The first run of plugin might not return a metric as currently a metric is collected asyncly with the plugin running, so the metric might not have been collected in the first run of the plugin. |
  | host\_id | Host\_id is an instance of class uuid.UUID that is read from data\_store. | Data | host\_id = data\_store['host\_id'] |
  | run\_command | This function runs commands in a list format. It has the following format. run\_command(cmd, timeout=4)  Where,  - cmd: Commands to be executed. Must be in the list format as in the example.  - timeout: Timeout for waiting for the command result. Default timeout is 4s. Timeout should not be set larger than 20s.  This function returns the command execution result. | Function | cmd = ['nsxdp-cli', 'ipfix', 'settings', 'granular', 'get', '--dvs-alias', 'nsxvswitch', '--dvport=dafa09ca-33ed-4e04-ae3d-1c53305d5fe6']  res = run\_command(cmd) |
  | Exportdata | This function exports data to wavefront. Currently, a dynamic plugin supports export to wavefront only. This function is applicable only in a VMware Cloud environment. It has the following format: Exportdata: ExportData(data={}, exports=[], source=host\_uuid)  Where,  data: data to be exported; data should be in dictionary format as example.  exports: destination list for export. In HL, only support wavefront in destination. It is required.  source: source string for export. It is useful only for wavefront destination. It is optional, the default value is NSX host\_uuid.  The function does not return any value. | Function | Exportdata(data={'esx.plugin.stats': {'stats': {'gc-esx-001': data}}}, exports=['wavefront']) |

  Sample of a plugin.py file.

  ```
  def report_test_data(edge_service_status):
      if edge_service_status == 'running':
          data = 2
      else:
          data = 3
      
      # examples on how to report data to wavefront.
      Exportdata(data={'esx.plugin.stats': {'stats': {'esx-dynamic-plugin-001': data}}}, exports=['wavefront'])


  def run():
      # examples on how to write log.
      logger.debug("this is a debug message!")
      logger.info("this is a demo message!")
      
      # examples on how to use specified module in manifest. Take 'random' as an example.
      s_res = random.randint(1,10)
      logger.warn("random.randint(1,10)=%s", s_res)
      
      # examples on how to use specified class in manifest. Take 'datetime' and 'date' as an example.
      logger.info('date.ctime(datetime.now()):{}'.format(date.ctime(datetime.now())))
      
      # examples on how to run cmd via interface run_command
      cmd = ['nsxdp-cli', 'ipfix', 'settings', 'granular', 'get', '--dvs-alias', 'nsxvswitch', '--dvport=dafa09ca-33ed-4e04-ae3d-1c53305d5fe6']
      c_res = run_command(cmd)
      logger.error("run_command(cmd) res:%s", c_res)
      
      # examples on how to read existing metrics from data_store
      m_res = data_store['metrics']['nsx.host.host-metrics']
      # examples on how to read effective profile from data_store
      profile = data_store['profile']
      logger.error("data_store['metrics']['nsx.host.host-metrics']:%s, profile:%s", m_res, profile)
      
      # examples on how to read host_id from data_store
      host_id = data_store['host_id']
      logger.info('host_id:{}'.format(host_id))

      if profile['EXPORT_DATA']:
          report_test_data('running')
          logger.info("dynamic plugin - exported data to wavefront")
      else:
          logger.info("dynamic plugin - not export data ")
      
      # examples on how to use substitute interfaces for sys. 
      logger.info("sys_path:{}".format(sys_path))
      logger.info("sys_getsizeof(1):{}".format(sys_getsizeof(1)))
      logger.info("sys_getrefcount(cmd):{}".format(sys_getrefcount(cmd)))
      logger.info("sys_maxsize:{}".format(sys_maxsize))
      logger.info("sys_getrecursionlimit():{}".format(sys_getrecursionlimit()))
      
      # examples on how to use substitute interfaces for datetime.
      today = datetime_date_today()
      logger.info("datetime today:{}".format(today))
      logger.info("datetime_date_strftime now:{}".format(datetime_date_strftime(datetime.now(), '%H:%M')))
      logger.info('date.ctime(today):{}'.format(date.ctime(today)))


  run()
  ```