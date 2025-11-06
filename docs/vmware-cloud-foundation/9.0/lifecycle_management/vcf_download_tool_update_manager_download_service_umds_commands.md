---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-update-manager-download-service--umds--commands.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > VCF Download Tool Update Manager Download Service (UMDS) Commands
---

# VCF Download Tool Update Manager Download Service (UMDS) Commands

Use the VCF Download Tool UMDS commands to install UMDS and list, download and manage ESX binaries and metadata. You can use this data to create vSphere Lifecycle Manager images in the vSphere Client.

## UMDS Commands

| Command | Description |
| --- | --- |
| install | Installs the UMDS (Update Manager Download Service) tool, which is required to run UMDS-specific operations. Once installed, the UMDS tool enables you to execute various tasks related to UMDS.  Example:  ``` ./vcf-download-tool umds install ``` |
| uninstall | Removes the UMDS tool from the system. Running this command uninstalls UMDS, disabling any further UMDS-specific operations. This command is useful for cleaning up the environment when UMDS is no longer needed or if it needs to be replaced or updated. Example:  ``` ./vcf-download-tool umds uninstall ``` |
| run | After you install UMDS, you can use the run command to configure and run UMDS. |

## UMDS Run Command Options

| Option | Description |
| --- | --- |
| -D, --download | Downloads updates based on the current configuration.  Can use the optional argument -m, --only-metadata to download metadata only. |
| -E, --export | Exports all updates that have been downloaded.  Can use the optional argument -x, --export-store to specify a destination directory for the export operation. This overrides the configured destination directory. |
| -I, --import | Imports all the updates from a given source location and merge to the UMDS patch store.  Arguments:  - -s, --import-store: The source patch store for import operation. - -f, --offline-bundle: The absolute path to an offline zip bundle file to import. |
| -R, --re-download | Re-downloads existing updates that may be corrupted and downloads new updates. Use this command only if you suspect that the UMDS patch store is corrupted.  Can use the optional argument -m, --only-metadata to download metadata only. |
| -S, --set-config | Configures UMDS.  Arguments:  - -u URL, --add-url URL: Adds a URL to the configuration for downloading updates. Requires --url-type. - -r URL\_type, --url-type URL\_type: Specify HOST for ESX 6.x. Use with --add-url. - -l URL, --remove-url URL: Removes a URL from the configuration. - -P patch\_store, --patch-store patch\_store: Configures a location for storing updates after download. - -o export\_store, --default-export-store export\_store: Configures a location for exporting updates. - -p FQDN:port,--proxy FQDN:port: Configures proxy server settings. Use --proxy "" to stop using the proxy server. - -Y, --enable-host: Enables ESX host update downloads for all platforms - -N, --disable-host: Disables ESX host update downloads for all platforms - -e host\_platform, --enable-host-platform host\_platform: Enables ESX host update downloads for specified platforms. Specify multiple platforms separated by whitespace Use -L, --list-host-platforms to list available host platforms. - -d host\_platform, --disable-host-platform host\_platform: Deactivates ESX host update downloads for specified platforms. Specify multiple platforms separated by whitespace - -s token, --add-entitlement-token token: Adds default URLs with entitlement token ID. |
| -G, --get-config | Prints the current UMDS configuration. |
| -v, --version | Prints the UMDS version. |
| -i level, --info-level level | Specifies the level of information shown on the console. You can use this option with:  - -D, --download - -E, --export - -E, --export  Arguments:  - verbose - info |
| -L, --list-host-platforms | Lists all supported ESX platforms for download. |

## Example UMDS Commands and Options

| Command | Description |
| --- | --- |
| ``` ./vcf-download-tool umds run -S --add-url https://hostname/index.xml --url-type HOST ``` | Adds a new ESX host patch depot URL. |
| ``` ./vcf-download-tool umds run -S --remove-url https://hostname/index.xml ``` | Removes an ESX host patch depot URL. |
| ``` ./vcf-download-tool umds run --list-host-platforms ``` | Lists all supported platforms for downloading ESX host updates. |
| ``` ./vcf-download-tool umds run -S --enable-host ``` | Enables downloading of ESX host updates. |
| ``` ./vcf-download-tool umds run -S -e embeddedEsx-8.0.0 ``` | Enables downloading of only ESXi 8.0.0 host updates. |
| ``` ./vcf-download-tool umds run -S -d embeddedEsx-8.0.0 ``` | Deactivates downloading of only ESXi 8.0.0 host updates. |
| ``` ./vcf-download-tool umds run vmware-umds -D ``` | Downloads updates based on the current configuration. |
| ``` ./vcf-download-tool umds run -S --default-export-store F:\UMDS-store ```  ``` ./vcf-download-tool umds run -E ``` | Specifies and new export location and exports all updates that have been downloaded to that location. |