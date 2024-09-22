Nagios Object Types

Nagios Object Types and Usage

Host
Purpose: Defines a physical or virtual machine to monitor.

Service
Purpose: Defines a specific service or aspect of a host to monitor (e.g., HTTP, CPU load).

Hostgroup
Purpose: Groups multiple hosts for easier management and monitoring.

Servicegroup
Purpose: Groups multiple services for better organization and management.

Contact
Purpose: Defines a person or entity to receive notifications about alerts.

Contactgroup
Purpose: Groups multiple contacts for consolidated notification management.

Command
Purpose: Defines commands that Nagios can execute for service checks.

Timeperiod
Purpose: Defines periods during which checks are active or notifications are sent.

Notification
Purpose: Configures how notifications are sent for specific contacts or groups.

Escalation
Purpose: Specifies how notifications should escalate to different contacts.

Eventhandler
Purpose: Defines commands to run in response to specific events.

Hostdependency
Purpose: Establishes dependencies between hosts to prevent alerts if one is down due to another.

Servicedependency
Purpose: Defines dependencies between services to manage alerts based on service status.

Servicetemplate
Purpose: Creates templates for services, allowing shared settings across multiple services.

Hosttemplate
Purpose: Creates templates for hosts, allowing shared settings across multiple hosts.

Comment
Purpose: Adds comments to hosts or services for additional context.