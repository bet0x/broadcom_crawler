---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/download-and-deploy-the-vco-va/configuring-the-automation-orchestrator-authentication-provider-with-the-command-line-interface.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Configuring the VCF Operations orchestrator authentication provider with the command line interface
---

# Configuring the VCF Operations orchestrator authentication provider with the command line interface

То use your deployed VCF Operations orchestrator, you must authenticate the deployment through the command line interface (CLI). To use these commands, you must log in to the VCF Operations orchestrator as a root user.

## Retrieving the current authentication provider

You can retrieve the current authentication provider by running the following command:

```
        vracli vro authentication
```

## Configure the authentication provider by using a guided wizard

To configure the authentication provider by using a guided configuration wizard, run the following command:

```
        vracli vro authentication wizard
```

After running the authentication wizard command, you are prompted to provide the necessary authentication provider information such as the type of authentication provider, hostname, and password.

To finish the configuring the authentication provider, restart the the VCF Operations orchestrator server:

```
  kubectl -n prelude delete pods -lapp=vco-app
```

## Configure the authentication provider by using predefined parameters

To configure the authentication provider by using predefined configuration parameters, run the vracli vro authentication set command. The command can have the following parameters:

| Parameter | Importance | Description |
| --- | --- | --- |
| -p or --provider | Required | This parameter defines the authentication provider type. The parameter value can be either tm, vsphere, or vidb depending on the authentication provider - VCF Automation, vSphere, or VCF SSO. |
| -hn or --hostname | Required | The hostname or URL of the authentication provider you want to configure. Both options are applicable. |
| -u or --username | Required | The username of the administrator associated with the authentication provider. |
| --password-file | Optional | The path to a file containing the password of the administrator account for the authentication provider. If left empty, you receive a prompt for adding the password data. The password file must be stored inside the /data/vco/usr/lib/vco directory of the VCF Operations orchestrator appliance. When adding the parameter in the command, exclude the /data/vco part of the filepath. |
| --admin-group | Required for vSphere authetnication providers. Ignored for other authentication providers. | Parameter for adding the VCF Operations orchestrator administrators group of the specified vSphere deployment. |
| --admin-group-domain | Required for vSphere authetnication providers. Ignored for other authentication providers. | This parameter defines the administrator group domain. |
| -k or --ignore-certificate | Optional | Using this parameter, the authentication process is configured to automatically trust the certificate of the authentication provider. |
| -f or --force | Optional | Using this parameter, you are not prompted for confirmation if the specified authentication provider is already configured. |
| --fqdn | Optional | This parameter defines the external address of the VCF Operations orchestrator server.  You can retrieve the FQDN address for your environment by running the nslookup <your\_orchestrator\_IP> command. |

## Example authentication configurations

```
vracli vro authentication set -f -k -p tm -u <username> -hn <vcfa_hostname> --fqdn <deployment_fqdn> --tenant <tenant_ID>
Enter credentials for authentication (could be API token, Bearer Token, Password): *******
The authentication provider has been successfully registered.
```

```
vracli vro authentication set -f -k -p vsphere -u <username> -hn <vsphere_hostname>  --fqdn <deployment_fqdn> --tenant <tenant_ID> --admin-group=<admin_group_ID> --admin-group-domain=<admin_group_domain>
```

To finish the configuring the authentication provider, restart the the VCF Operations orchestrator server:

```
        kubectl -n prelude scale deployment vco-app --replicas=0kubectl -n prelude scale deployment vco-app --replicas=1
```

## Unregister an authentication provider

You can unregister the current authentication provider by running the vracli vro authentication unregister command. This command can have the following parameters:

| Parameter | Importance | Description |
| --- | --- | --- |
| -u or --username | Required | The username of the administrator associated with the authentication provider. |
| --password-file | Optional | The path to a file containing the password of the administrator account for the authentication provider. If left empty, you receive a prompt for adding the password data. The password file must be stored inside the /data/vco/usr/lib/vco directory of the appliance. When including the parameter in the command, exclude the /data/vco part of the filepath. |

## CLI command logs

VCF Operations orchestrator CLI commands print their logs in the /services-logs/prelude/vco-app/file-logs/vco-server-app\_cfg-cli.log file. When a command returns a result different than zero and the standard output does not show a specific error, the exception is visible in this file.