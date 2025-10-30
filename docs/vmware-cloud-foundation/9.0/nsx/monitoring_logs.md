---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes/monitoring-logs.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Monitoring Logs
---

# Monitoring Logs

NSX logging is important and useful for troubleshooting. NSX Manager supports Logging Monitor to control the quality and quantity of logs for internal tests and product environment. The default mode of Logging Monitor is set to the product environment. Logging Monitor leverages the System Health Agent (SHA) framework to keep a check on the log generation rate, infer log file retention time, and generate log duration alarms to indicate abnormal log rotation rates and potential log spews. By monitoring the logs, NSX Manager can find issues before valuable logs are flushed and suggest preventive actions that you can take.

Logging Monitor checks log duration in runtime. It periodically monitors the logging rate (over the last LOG\_RATE\_PERIOD which has a default value of 1 hour) and calculates the estimated duration based on log rotation settings of each log. When the estimated duration is less than desired duration for several threshold (which is configurable) times, Logging Monitor gives an indication of potential log spew and raises log duration alarms for you to take proper actions. Meanwhile, Logging Monitor also generates a report with more details about the problem. In the product environment mode, Logging Monitor raises only one alarm for all abnormal logs.

The mode and log rate period are set in the variables LOG\_MONIOTR\_MODE and LOG\_RATE\_PERIOD respectively that are defined in the sha\_config.yml file.

You can also provide a backup disk and notify to SHA using a plugin profile. The SHA plugin will move the oldest compressed log file of the log to the backup disk when the current total size hits a predefined percentage (50%) of the maximum size. The backup disk should be a directory to which SHA can move the log files.

Note the following conditions for different platforms:

- On UA and edge nodes, ensure that the directory can be written by “nsx-sha” user.
- On ESX, the sub-directory under /var/run/log can be used to set up the backup directory.

The SHA plugin moves the oldest log file to the backup disk and also performs the following functions:

- Monitors the log files size of a given log.
- Calculates the maximum size based on the rotation configuration.
- Renames the oldest log file with a timestamp and move it to the backup disk when the total size hits the predefined percentage (50%).

Files that are moved to the backup disk will not be considered in log duration monitor.